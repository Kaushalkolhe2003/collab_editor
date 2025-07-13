# editor/consumers.py

import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from django.contrib.auth.models import User
from .models import Document, Collaborator

class DocumentConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.document_id = self.scope['url_route']['kwargs']['document_id']
        self.room_group_name = f'document_{self.document_id}'
        self.user = self.scope['user']

        if self.user.is_authenticated and await self.user_has_access():
            await self.channel_layer.group_add(self.room_group_name, self.channel_name)
            await self.accept()
        else:
            await self.close()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        content = data.get('content')
        typing = data.get('typing')

        if content is not None:
            await self.save_document_content(content)
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'document_edit',
                    'content': content,
                    'sender': self.user.get_full_name() or self.user.username,
                }
            )

        if typing:
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'user_typing',
                    'user': self.user.get_full_name() or self.user.username,
                }
            )

    async def document_edit(self, event):
        await self.send(text_data=json.dumps({
            'type': 'edit',
            'content': event['content'],
            'sender': event['sender'],
        }))

    async def user_typing(self, event):
        await self.send(text_data=json.dumps({
            'type': 'typing',
            'user': event['user'],
        }))

    @database_sync_to_async
    def user_has_access(self):
        doc = Document.objects.get(pk=self.document_id)
        return doc.owner == self.user or doc.collaborators.filter(user=self.user).exists()

    @database_sync_to_async
    def save_document_content(self, content):
        doc = Document.objects.get(pk=self.document_id)
        doc.content = content
        doc.save()