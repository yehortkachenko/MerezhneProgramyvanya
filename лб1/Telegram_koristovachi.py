from telethon import TelegramClient
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch

api_id = 'tvoy_api_id'  
api_hash = 'tvoy_api_hash_id'  
phone = 'tvoy_nomer'  
chat_username = 'silka_kanala "https://t.me/"'  

client = TelegramClient('session_name', api_id, api_hash)
async def get_chat_members(chat_username):
    await client.start(phone=phone)
    chat = await client.get_entity(chat_username)
    participants = []
    async for user in client.iter_participants(chat):
        participants.append({'id': user.id, 'username': user.username, 'first_name': user.first_name})
    return participants
async def main():
    members = await get_chat_members(chat_username)
    for member in members:
        print(f"ID: {member['id']}, Username: {member['username']}, Name: {member['first_name']}")
with client:
    client.loop.run_until_complete(main())