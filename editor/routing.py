from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/editor/<int:document_id>/', consumers.DocumentConsumer.as_asgi()),
]
