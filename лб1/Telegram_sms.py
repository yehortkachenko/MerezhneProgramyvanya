from telethon import TelegramClient

api_id = 'tvoy_api_id'  
api_hash = 'tvoy_api_hash_id' 
phone = 'tvoy_nomer'

client = TelegramClient('session_name', api_id, api_hash)
async def send_message_to_user_or_chat(target, message):
    await client.start(phone=phone)
    try:
        await client.send_message(target, message)
        print(f"Повідомлення надіслано: {message}")
    except Exception as e:
        print(f"Помилка при надсиланні повідомлення: {e}")

async def main():
    target = 'chat_username або silka_kanala "https://t.me/"' 
    message = "Привіт! "
    
    await send_message_to_user_or_chat(target, message)

with client:
    client.loop.run_until_complete(main())
