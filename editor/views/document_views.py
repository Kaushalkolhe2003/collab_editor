from django.shortcuts import get_object_or_404, redirect
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.contrib import messages
from ..forms import CollaboratorForm
from ..models import Document, Collaborator, DocumentVersion


class DocumentListView(LoginRequiredMixin, ListView):
    model = Document
    template_name = 'editor/document_list.html'
    context_object_name = 'documents'

    def get_queryset(self):
        user = self.request.user
        owned_docs = Document.objects.filter(owner=user)
        shared_docs = Document.objects.filter(collaborators__user=user)
        return (owned_docs | shared_docs).distinct()

class DocumentCreateView(LoginRequiredMixin, CreateView):
    model = Document
    fields = ['title', 'content']
    template_name = 'editor/document_create.html'
    success_url = reverse_lazy('document_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class DocumentDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Document
    template_name = 'editor/document_detail.html'
    context_object_name = 'document'

    def test_func(self):
        doc = self.get_object()
        return doc.owner == self.request.user or doc.collaborators.filter(user=self.request.user).exists()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        document = self.get_object()
        user = self.request.user

        # Check if user is owner or editor
        can_edit = (
                document.owner == user or
                document.collaborators.filter(user=user, role='editor').exists()
        )
        context['can_edit'] = can_edit
        return context


class DocumentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Document
    fields = ['title', 'content']
    template_name = 'editor/document_edit.html'

    def test_func(self):
        doc = self.get_object()
        return doc.owner == self.request.user or doc.collaborators.filter(user=self.request.user, role='editor').exists()

    def form_valid(self, form):
        # Get the current document before update
        old_document = self.get_object()

        # Save a version BEFORE updating content
        DocumentVersion.objects.create(
            document=old_document,
            content=old_document.content,
            edited_by=self.request.user
        )

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('document_detail', kwargs={'pk': self.object.pk})


class CollaboratorAddView(LoginRequiredMixin, FormView):
    template_name = 'editor/add_collaborator.html'
    form_class = CollaboratorForm

    def dispatch(self, request, *args, **kwargs):
        self.document = get_object_or_404(Document, pk=kwargs['pk'])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        collaborator = form.save(commit=False)
        collaborator.document = self.document

        # Avoid duplicate collaborator entries
        if self.document.collaborators.filter(user=collaborator.user).exists():
            messages.warning(self.request, "This user is already a collaborator.")
        else:
            collaborator.save()
            messages.success(self.request, "Collaborator added successfully.")

        return redirect('document_detail', pk=self.document.pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['document'] = self.document
        return context

class CollaboratorRemoveView(LoginRequiredMixin, View):
    def post(self, request, doc_pk, collab_pk):
        document = get_object_or_404(Document, pk=doc_pk)
        if document.owner != request.user:
            return redirect('document_detail', pk=doc_pk)

        collaborator = get_object_or_404(Collaborator, pk=collab_pk, document=document)
        collaborator.delete()
        messages.success(request, "Collaborator removed.")
        return redirect('document_detail', pk=doc_pk)
