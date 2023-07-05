from telethon.sync import TelegramClient
from telethon.tl.functions.contacts import ResolveUsernameRequest
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.tl.types import InputChannel,  MessageMediaDocument, DocumentAttributeFilename, MessageMediaPhoto
from telethon.errors import SessionPasswordNeededError
import sys
import os

api_id = 21518307
api_hash = '0c3d16f2b71e5be100746c6b78828963'

if len(sys.argv) > 1:
    url = sys.argv[1]
else:
    print("Please provide a URL")
    sys.exit(1)

phone_number = ''
files = [f for f in os.listdir('.') if f.endswith('.session')]

if len(files) == 0:
    phone_number = input("Phone Number: ")
elif len(files) == 1:
    phone_number = files[0].removesuffix('.session')
else:
    print("Multiple sessions found, select session")
    i = 0
    for file in files:
            print('[{}] '.format(i+1) +file.removesuffix('.session'))
            i+=1
    print('[q] to quit')
    i = input("Select session: ")
    if i == 'q':
        sys.exit(0)
    phone_number = files[int(i)-1].removesuffix('.session')
    
channel = url.split('/')[3]
message_id = int(url.split('/')[4])

client = TelegramClient(phone_number, api_id, api_hash)
client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone_number)
    try:
        client.sign_in(phone_number, input('Enter the code: '))
    except SessionPasswordNeededError:
        client.sign_in(password=input('Enter the two-step verification password: '))

    
entity = client.get_entity(channel)

# messages = client.get_messages(entity, limit=3)
# for message in messages:
#     print(message.id, message.text)
#     if message.media:
#         # print('Message ID:', message.id)
#         # print('Message text:', message.text)
#         # print('Media:', message.media)
#         filename = message.id
#         if isinstance(message.media, MessageMediaDocument):
#             for attribute in message.media.document.attributes:
#                 if isinstance(attribute, DocumentAttributeFilename):
#                     filename = attribute.file_name
#                     print('Filename:', filename)
#         message.download_media(filename)

message = client.get_messages(channel, ids=message_id)
if message.media:
    filename = '{}_'.format(message.id)
    if(isinstance(message.media, MessageMediaPhoto)):
        filename += '{}.jpg'.format(message.media.photo.id)
    if isinstance(message.media, MessageMediaDocument):
        for attribute in message.media.document.attributes:
            if isinstance(attribute, DocumentAttributeFilename):
                filename = attribute.file_name
                print('Filename:', filename)
    message.download_media(filename)
    print('Finish: {}'.format(filename)

sys.exit(0)
