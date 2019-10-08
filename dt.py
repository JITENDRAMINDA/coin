from pyrogram import Client, Filters, Emoji
import random
import time

app = Client("session",bot_token="633344746:AAFZpXfgLxbK-kZ4Z0zkQ4I8CJ9WlE0solg",api_id=605563,api_hash="7f2c2d12880400b88764b9b304e14e0b") 

@app.on_message(Filters.command('rolls'))
def ran(client, message):
 b = client.get_chat_member(message.chat.id , message.from_user.id).status
 if b == 'administrator' or b == "creator":
   mes = message.reply("**⏳ Loading..**")
   time.sleep(2)
   x = str(random.choice(["3","9","7","5","6","4","8","2","10","J","K","A","Q"])) + str(random.choice(["♣️","♥️","♠️","♦️"]))
   y = str(random.choice(["6","3","9","10","2","7","8","4","5","J","K","A","Q"])) + str(random.choice(["♥️","♠️","♦️","♣️"]))
   client.edit_message_text(message.chat.id,mes.message_id,"<b>(1)🐉 " + x +"/n /n (2)🐅 " +  y + "</b>" , parse_mode="html" )
   time.sleep(1)
   x = str(random.choice(["3","9","7","5","6","4","8","2","10","J","K","A","Q"])) + str(random.choice(["♣️","♥️","♠️","♦️"]))
   y = str(random.choice(["6","3","9","10","2","7","8","4","5","J","K","A","Q"])) + str(random.choice(["♥️","♠️","♦️","♣️"]))
   client.edit_message_text(message.chat.id,mes.message_id,"<b>(1)🐉 " + x +"/n /n (2)🐅 " +  y + "</b>" , parse_mode="html" )
   time.sleep(1)
   x = str(random.choice(["3","9","7","5","6","4","8","2","10","J","K","A","Q"])) + str(random.choice(["♣️","♥️","♠️","♦️"]))
   y = str(random.choice(["6","3","9","10","2","7","8","4","5","J","K","A","Q"])) + str(random.choice(["♥️","♠️","♦️","♣️"]))
   client.edit_message_text(message.chat.id,mes.message_id,"<b>(1)🐉 " + x +"/n /n (2)🐅 " +  y + "</b>" , parse_mode="html" )
   time.sleep(1)
   x = str(random.choice(["3","9","7","5","6","4","8","2","10","J","K","A","Q"])) + str(random.choice(["♣️","♥️","♠️","♦️"]))
   y = str(random.choice(["6","3","9","10","2","7","8","4","5","J","K","A","Q"])) + str(random.choice(["♥️","♠️","♦️","♣️"]))
   client.edit_message_text(message.chat.id,mes.message_id,"<b>(1)🐉 " + x +"/n /n (2)🐅 " +  y + "</b>" , parse_mode="html" )
   time.sleep(1)
   x = str(random.choice(["3","9","7","5","6","4","8","2","10","J","K","A","Q"])) + str(random.choice(["♣️","♥️","♠️","♦️"]))
   y = str(random.choice(["6","3","9","10","2","7","8","4","5","J","K","A","Q"])) + str(random.choice(["♥️","♠️","♦️","♣️"]))
   client.edit_message_text(message.chat.id,mes.message_id,"<b>(1)🐉 " + x +"/n /n (2)🐅 " +  y + "</b>" , parse_mode="html" )
   time.sleep(1)
   x = str(random.choice(["3","9","7","5","6","4","8","2","10","J","K","A","Q"])) + str(random.choice(["♣️","♥️","♠️","♦️"]))
   y = str(random.choice(["6","3","9","10","2","7","8","4","5","J","K","A","Q"])) + str(random.choice(["♥️","♠️","♦️","♣️"]))
   client.edit_message_text(message.chat.id,mes.message_id,"<b>(1)🐉 " + x +"/n /n (2)🐅 " +  y + "</b>" , parse_mode="html" )
   time.sleep(1)
   x = str(random.choice(["3","9","7","5","6","4","8","2","10","J","K","A","Q"])) + str(random.choice(["♣️","♥️","♠️","♦️"]))
   y = str(random.choice(["6","3","9","10","2","7","8","4","5","J","K","A","Q"])) + str(random.choice(["♥️","♠️","♦️","♣️"]))
   client.edit_message_text(message.chat.id,mes.message_id,"<b>(1)🐉 " + x +"/n /n (2)🐅 " +  y + "</b>" , parse_mode="html" )
app.run()
