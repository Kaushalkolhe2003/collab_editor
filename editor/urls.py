from django.urls import path
from .views import *
from .views.auth_view import UserRegisterView, UserLoginView, UserLogoutView
from .views.document_views import DocumentListView, DocumentCreateView, DocumentDetailView, DocumentUpdateView, \
    CollaboratorAddView, CollaboratorRemoveView

urlpatterns = [
    # User URLS
    path('', DocumentListView.as_view(), name='document_list'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),

    # Document URLs
    path('documents/', DocumentListView.as_view(), name='document_list'),
    path('documents/create/', DocumentCreateView.as_view(), name='document_create'),
    path('documents/<int:pk>/', DocumentDetailView.as_view(), name='document_detail'),
    path('document/<int:pk>/edit/', DocumentUpdateView.as_view(), name='document_edit'),

    # Collab URLS
    path('documents/<int:pk>/add-collaborator/', CollaboratorAddView.as_view(), name='add_collaborator'),
    path('documents/<int:doc_pk>/remove-collaborator/<int:collab_pk>/', CollaboratorRemoveView.as_view(), name='remove_collaborator'),


]
