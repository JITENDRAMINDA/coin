from pyrogram import Client, Filters, Emoji
import random
import time

app = Client("session",bot_token="633344746:AAFZpXfgLxbK-kZ4Z0zkQ4I8CJ9WlE0solg",api_id=605563,api_hash="7f2c2d12880400b88764b9b304e14e0b") 

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





2.          🐅""" +  y + """ 

⎯⎯⎯⎯⎯⎯Final⎯⎯⎯⎯⎯⎯""" )
app.run()
