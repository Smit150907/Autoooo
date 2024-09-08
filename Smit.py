from telethon import TelegramClient, events
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

# Define your API ID, API hash, and bot token
API_ID = '21476260'
API_HASH = 'ec9654f315ce63225cf7b69263347f96'
BOT_TOKEN = '7200915875:AAGIN0zVDisYlwr8rdcRVlOGjEr-0V6cGjg'
CHANNEL_ID = -1002353235156  # Channel ID

# Create a new client instance
client = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

@client.on(events.ChatAction())
async def handler(event):
    if event.chat_id == CHANNEL_ID and event.user_added:
        user = await event.get_user()
        first_name = user.first_name
        message = f"Hello 👋 {first_name} Do you want free 150$?"
        await client.send_message(user.id, message)

# Start the client
client.start()
client.run_until_disconnected()
