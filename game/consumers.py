import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import JsonWebsocketConsumer

from .views import play_tile


class GameConsumer(JsonWebsocketConsumer):
    def connect(self):
        self.game_pk = self.scope['url_route']['kwargs']['game_pk']
        self.user = self.scope['user']
        self.accept()

    def receive_json(self, content):
        print(content)

        new_state = {}
        if content['action'] == 'play_tile':
            print("{} {} {}".format(self.game_pk, self.user, content['body']['tile']))
            new_state = play_tile(self.game_pk, self.user, content['body']['tile'])
        else:
            logger.error("In receive got unknown action {} body {}".format(content['action'], content['body']))

        print(new_state)
        self.send_json(new_state)


    def disconnect(self, close_code):
        print("Socket to {} closed".format(self.user))
        pass


# class ChatConsumer(WebsocketConsumer):
#     def connect(self):
#         self.room_name = self.scope['url_route']['kwargs']['room_name']
#         self.room_group_name = 'chat_%s' % self.room_name
#         self.user = self.scope["user"]

#         # Join room group
#         async_to_sync(self.channel_layer.group_add)(
#             self.room_group_name,
#             self.channel_name
#         )

#         self.accept()

#     def disconnect(self, close_code):
#         # Leave room group
#         async_to_sync(self.channel_layer.group_discard)(
#             self.room_group_name,
#             self.channel_name
#         )

#     # Receive message from WebSocket
#     def receive(self, text_data):
#         print(text_data)
#         text_data_json = json.loads(text_data)

#         action = text_data_json['action']
#         body = text_data_json['body']

#         if action == 'play_tile':
#             print("{} {} {}".format(self.room_name, self.user, body['tile']))
#             new_state = play_tile(self.room_name, self.user, body['tile'])
#         else:
#             logger.error("In receive got unknown action {} body {}".format(action, body))

#         print(new_state)
#         # Send action to room group
#         async_to_sync(self.channel_layer.group_send)(
#             self.room_group_name,
#             {
#                 'type': 'chat_message',
#                 'action': action,
#                 'new_state': json.dumps(new_state),
#             }
#         )

#     # Receive message from room group
#     def chat_message(self, event):
#         message = event['message']

#         # Send message to WebSocket
#         self.send(text_data=json.dumps({
#             'message': message
#         }))
