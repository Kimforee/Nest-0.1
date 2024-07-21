# your_app_name/consumers.py

import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from django.contrib.auth.models import User
from .models import Nest, Message
from asgiref.sync import sync_to_async

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.nest_id = self.scope['url_route']['kwargs']['pk']
        self.room_group_name = f'nest_{self.nest_id}'

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        message_type = data.get('type')

        if message_type == 'chat_message':
            await self.handle_chat_message(data)
        elif message_type == 'delete_message':
            await self.handle_delete_message(data)


    async def handle_chat_message(self, data):
        message = data['message']
        username = data['user']
        created = data['created']
        nest_id = data['nest']

        saved_message = await self.save_message(username, nest_id, message, created)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'user': username,
                'created': created,
                'message_id': saved_message.id,
                'can_delete': self.scope["user"].id == saved_message.user.id or self.scope["user"].id == saved_message.nest.host.id
            }
        )

    async def handle_delete_message(self, data):
        message_id = data['message_id']
        nest_id = data['nest']

        await self.delete_message(message_id, nest_id)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'delete_message',
                'message_id': message_id
            }
        )

    @sync_to_async
    def save_message(self, username, nest_id, message, created):
        user = User.objects.get(username=username)
        nest = Nest.objects.get(id=nest_id)
        return Message.objects.create(user=user, nest=nest, body=message, created=created)

    @sync_to_async
    def delete_message(self, message_id, nest_id):
        message = Message.objects.get(id=message_id, nest_id=nest_id)
        if message.user == self.scope["user"] or message.nest.host == self.scope["user"]:
            message.delete()

    async def chat_message(self, event):
        message = event['message']
        user = event['user']
        created = event['created']
        message_id = event['message_id']
        can_delete = event['can_delete']

        await self.send(text_data=json.dumps({
            'type': 'chat_message',
            'message': message,
            'user': user,
            'created': created,
            'message_id': message_id,
            'can_delete': can_delete
        }))

    async def delete_message(self, event):
        message_id = event['message_id']

        await self.send(text_data=json.dumps({
            'type': 'delete_message',
            'message_id': message_id
        }))


