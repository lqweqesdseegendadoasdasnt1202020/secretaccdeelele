import asyncio
from telethon import TelegramClient, events

# Настройки
api_id = '20909352'
api_hash = 'a3be2584a77447cfc0c7d1595076e9dc'
phone_number = '+923559486166'

# ID каналов
source_channel_id = -1002452764624
target_channel_id = -1002212238461

# Создание клиента
client = TelegramClient('session_name', api_id, api_hash)

@client.on(events.NewMessage(chats=source_channel_id))
async def handler(event):
    message = event.message.message
    if "A new limited gift has appeared" in message or "A new gift has appeared" in message:
        await client.send_message(target_channel_id, message)

async def main():
    await client.start(phone=phone_number)
    print("Client Created")
    await client.run_until_disconnected()

if __name__ == '__main__':
    asyncio.run(main())