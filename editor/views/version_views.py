from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from ..models import DocumentVersion, Document

class DocumentVersionListView(LoginRequiredMixin, ListView):
    model = DocumentVersion
    template_name = 'editor/document_versions.html'
    context_object_name = 'versions'

    def get_queryset(self):
        document = get_object_or_404(Document, pk=self.kwargs['pk'])
        return DocumentVersion.objects.filter(document=document).order_by('-timestamp')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['document'] = get_object_or_404(Document, pk=self.kwargs['pk'])
        return context
