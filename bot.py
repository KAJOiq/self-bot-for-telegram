from telethon import TelegramClient, events # type: ignore

# api_id and api_hash from https://my.telegram.org/apps
api_id = (API_ID) # GET API id from https://my.telegram.org/apps
api_hash = 'HASH' # GET API hash from https://my.telegram.org/apps

client = TelegramClient('user', api_id, api_hash).start()

# This message can contain any text, links, and emoji:
message = """ 

Away 💤

"""
# You can use any message you want

@client.on(events.NewMessage())
async def handler(event):
    if event.is_private: # check if the message is from a private chat
        sender = await event.get_input_sender()
        await client.send_message(sender, message)


print("-"*20)
print("SelfBot Is Ready")
print("-"*20)
client.run_until_disconnected()