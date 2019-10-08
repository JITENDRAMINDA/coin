from pyrogram import Client, Filters, Emoji
import random
import time

app = Client("session",bot_token="981972366:AAEvUMrd-CwuZRbjzD6zY9ycnJjah3OiCdc",api_id=605563,api_hash="7f2c2d12880400b88764b9b304e14e0b") 

@app.on_message(Filters.command('rolls'))
def ran(client, message):
 b = client.get_chat_member(message.chat.id , message.from_user.id).status
 if b == 'administrator' or b == "creator":
   mes = message.reply("⏳ Loading..")
   time.sleep(2)
   x = str(random.choice(["3⃣","9⃣","7⃣","5⃣","6⃣","4⃣","8⃣","2⃣","🔟","🇯","🇰","🇦","🇶"])) + str(random.choice(["♣️","♥️","♠️","♦️"]))
   y = str(random.choice(["6⃣","3⃣","9⃣","🔟","2⃣","7⃣","8⃣","4⃣","5⃣","🇯","🇰","🇦","🇶"])) + str(random.choice(["♥️","♠️","♦️","♣️"]))
   client.edit_message_text(message.chat.id,mes.message_id,"1. 🐉          " + x + """





2. 🐅          """ +  y + """ 

⎯⎯⎯⎯⎯Loading⎯⎯⎯⎯⎯""" )
   time.sleep(1)
   x = str(random.choice(["3⃣","9⃣","7⃣","5⃣","6⃣","4⃣","8⃣","2⃣","🔟","🇯","🇰","🇦","🇶"])) + str(random.choice(["♣️","♥️","♠️","♦️"]))
   y = str(random.choice(["6⃣","3⃣","9⃣","🔟","2⃣","7⃣","8⃣","4⃣","5⃣","🇯","🇰","🇦","🇶"])) + str(random.choice(["♥️","♠️","♦️","♣️"]))
   client.edit_message_text(message.chat.id,mes.message_id,"1. 🐉          " + x + """





2. 🐅          """ +  y + """ 

⎯⎯⎯⎯⎯Loading⎯⎯⎯⎯⎯""" )
   time.sleep(1)
   x = str(random.choice(["3⃣","9⃣","7⃣","5⃣","6⃣","4⃣","8⃣","2⃣","🔟","🇯","🇰","🇦","🇶"])) + str(random.choice(["♣️","♥️","♠️","♦️"]))
   y = str(random.choice(["6⃣","3⃣","9⃣","🔟","2⃣","7⃣","8⃣","4⃣","5⃣","🇯","🇰","🇦","🇶"])) + str(random.choice(["♥️","♠️","♦️","♣️"]))
   client.edit_message_text(message.chat.id,mes.message_id,"1. 🐉          " + x + """





2. 🐅          """ +  y + """ 

⎯⎯⎯⎯⎯Loading⎯⎯⎯⎯⎯""" )
   time.sleep(1)
   x = str(random.choice(["3⃣","9⃣","7⃣","5⃣","6⃣","4⃣","8⃣","2⃣","🔟","🇯","🇰","🇦","🇶"])) + str(random.choice(["♣️","♥️","♠️","♦️"]))
   y = str(random.choice(["6⃣","3⃣","9⃣","🔟","2⃣","7⃣","8⃣","4⃣","5⃣","🇯","🇰","🇦","🇶"])) + str(random.choice(["♥️","♠️","♦️","♣️"]))
   client.edit_message_text(message.chat.id,mes.message_id,"1. 🐉          " + x + """





2. 🐅          """ +  y + """ 

⎯⎯⎯⎯⎯Loading⎯⎯⎯⎯⎯""" )
   time.sleep(1)
   x = str(random.choice(["3⃣","9⃣","7⃣","5⃣","6⃣","4⃣","8⃣","2⃣","🔟","🇯","🇰","🇦","🇶"])) + str(random.choice(["♣️","♥️","♠️","♦️"]))
   y = str(random.choice(["6⃣","3⃣","9⃣","🔟","2⃣","7⃣","8⃣","4⃣","5⃣","🇯","🇰","🇦","🇶"])) + str(random.choice(["♥️","♠️","♦️","♣️"]))
   client.edit_message_text(message.chat.id,mes.message_id,"1. 🐉          " + x + """





2. 🐅          """ +  y + """ 

⎯⎯⎯⎯⎯Loading⎯⎯⎯⎯⎯""" )
   time.sleep(1)
   x = str(random.choice(["3⃣","9⃣","7⃣","5⃣","6⃣","4⃣","8⃣","2⃣","🔟","🇯","🇰","🇦","🇶"])) + str(random.choice(["♣️","♥️","♠️","♦️"]))
   y = str(random.choice(["6⃣","3⃣","9⃣","🔟","2⃣","7⃣","8⃣","4⃣","5⃣","🇯","🇰","🇦","🇶"])) + str(random.choice(["♥️","♠️","♦️","♣️"]))
   client.edit_message_text(message.chat.id,mes.message_id,"1. 🐉          " + x + """





2. 🐅          """ +  y + """ 

⎯⎯⎯⎯⎯Loading⎯⎯⎯⎯⎯""" )
   time.sleep(1)
   x = str(random.choice(["3⃣","9⃣","7⃣","5⃣","6⃣","4⃣","8⃣","2⃣","🔟","🇯","🇰","🇦","🇶"])) + str(random.choice(["♣️","♥️","♠️","♦️"]))
   y = str(random.choice(["6⃣","3⃣","9⃣","🔟","2⃣","7⃣","8⃣","4⃣","5⃣","🇯","🇰","🇦","🇶"])) + str(random.choice(["♥️","♠️","♦️","♣️"]))
   client.edit_message_text(message.chat.id,mes.message_id,"1. 🐉          " + x +"""





2. 🐅         """ +  y + """ 

⎯⎯⎯⎯⎯⎯Final⎯⎯⎯⎯⎯⎯""" )
@app.on_message(Filters. command('leavechat'))
def ran(client,message):
 if message.from_user.id == 491634139:
  if len(message.text.split( )) > 1:
    client.leave_chat(int(message.text.split(' ')[1]))
  else:
    client.leave_chat(message.chat.id)
    
@app.on_message(Filters. private & Filters.command("start"))
def ran( client, message) :
  message.reply( """♻️ This is Roulatte created by a wonderful [person](https://t.me/Google_console) ✍️.
My commands :
👉 For D & T
1. /dt
All command exist only Admins in Super groups ✍️.
For buy [click here](https://t.me/google_console)
 """,disable_web_page_preview = True )

app.run()
