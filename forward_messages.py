from telethon import TelegramClient, events

# Replace with your own values from my.telegram.org
api_id = 26622985
api_hash = '81e765499baf33201e09c78ae1ad0ad9'

# Replace with your Telegram account credentials
phone_number = '+94781279881'
username = 'fuck2027'
password = '656656'  # or 'two_step_verification_code' if enabled

# Target channel or chat where you want to forward messages
target_username = 'hello21598'

# Create the client and connect
client = TelegramClient(username, api_id, api_hash)

async def main():
    await client.start(phone_number, password)
    
    # Event handler for new messages
    @client.on(events.NewMessage)
    async def handler(event):
        # Example: Forward messages from private chats and groups
        if event.is_private or event.is_group:
            # Forward message to the target channel or chat
            await client.forward_messages(target_username, event.message)

    print(f"Bot is running... Forwarding messages to {target_username}")
    await client.run_until_disconnected()

# Run the script
with client:
    client.loop.run_until_complete(main())
