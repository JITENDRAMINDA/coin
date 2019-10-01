from telethon import TelegramClient

client = TelegramClient("my",1134067,"f743379074210a6bf6830f77b4ba04ab")

@client.on(events.NewMessage(pattern=r'^/start'))
async def start_respond(e):
 await e.reply('/stort')

with client:
    client.loop.run_until_complete(main())
