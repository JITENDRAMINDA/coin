from pyrogram import Client, Filters, Emoji
import random
import time

app = Client("session",bot_token="863961400:AAG3kaHMrOsklKBP3fGEn7T4rTyC1dXkRTc",api_id=605563,api_hash="7f2c2d12880400b88764b9b304e14e0b") 

@app.on_message(Filters.command('rolls'))
def ran(client, message):
 b = client.get_chat_member(message.chat.id , message.from_user.id).status
 if b == 'administrator' or b == "creator":
   mes = message.reply("**☢️ Spinning..ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ**")
   time.sleep(1)
   client.edit_message_text(message.chat.id,mes.message_id, "**" + "☢️ Spinning...ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ ㅤ" +"**")
   time.sleep(1)
   client.edit_message_text(message.chat.id,mes.message_id, "**" + "☢️ Spinning....ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ" +"**")
   time.sleep(1)
   client.edit_message_text(message.chat.id,mes.message_id, "**" + "☢️ Spinning...ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ" +"**")
   time.sleep(1)
   client.edit_message_text(message.chat.id,mes.message_id, "**" + "☢️ Spinning..ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ" +"**")
   time.sleep(1)
   z = str(random.choice(range(0,36)))
   mod = int(z) % 2 
   if mod > 0:
    client.edit_message_text(message.chat.id,mes.message_id, "**" + "☢️ Spinner Stopped at " + z +" " +"🔴ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ" +"**")
   elif int(z) == 0:
    client.edit_message_text(message.chat.id,mes.message_id, "**" + "☢️ Spinner Stopped at " + z +" " +"Jackpot Number 🤑🤑ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ" +"**")
   else:
    client.edit_message_text(message.chat.id,mes.message_id, "**" + "☢️ Spinner Stopped at " + z +" " +"⚫ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ" +"**")  
app.run()
