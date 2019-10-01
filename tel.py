@client.on(events.NewMessage(pattern=r'^/start'))
async def start_respond(e):
 await e.reply('/stort')
