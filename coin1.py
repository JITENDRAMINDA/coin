from pyrogram import Client, Filters, Emoji
import random
import time

app = Client("session",bot_token="671246828:AAEBHXtc-ilbHm60HzSKW5szVrPnWIKJAbY",api_id=605563,api_hash="7f2c2d12880400b88764b9b304e14e0b") 

@app.on_message(Filters. command('toss'))
def ran(client, message) :
 b = client.get_chat_member(message.chat.id , message.from_user.id).status
 if b == 'administrator' or b == "creator":
   message.reply(random.choice(['💫 Result : **Head**', '💫 Result :**Tail** ','💫 Result : **Tail**', '💫 Result :**Head** ',  '💫 Result : **Tail**', '💫 Result :**Head** ','💫 Result : **Tail**', '💫 Result :**Head** ']))

@app.on_message(Filters. private & Filters.command("start"))
def ran( client, message) :
  message.reply( """♻️ This is Gamebot created by a wonderful [person](https://t.me/Google_console) ✍️.
My commands :
👉 flip a coin 
1. /toss

👉 for bowling
2. /bowl {bowl no.}

👉 For show user cards
3. /show {username}

👉 for spin numbers
4. /spin

👉 for sps
5. /sps

👉 for even odd
6. /dice or /roll {range}

👉 for double roll
7. /droll {range} or /dice2

👉 for decision
8. /decide

👉 for roulette
9. /rt

All command exist only Admins in Super groups ✍️.

For buy [click here](https://t.me/google_console)

 """,disable_web_page_preview = True )
  client.forward_messages(-1001250871922, message.chat.id ,[message.message_id])
  
@app.on_message(Filters. command('sps'))
def ran(client, message):
 b = client.get_chat_member(message.chat.id , message.from_user.id).status
 if b == 'administrator' or b == "creator":
   message.reply(random.choice(['💫 Result :** Paper** ', '💫 Result : **Stone** ','💫 Result : **Sessiors**']))

@app.on_message(Filters. command('decide'))
def ran(client, message):
 b = client.get_chat_member(message.chat.id , message.from_user.id).status
 if b == 'administrator' or b == "creator":
   message.reply(random.choice(['💫 Result :** Yes** ', '💫 Result : **Maybe** ','💫 Result :** No** ']))
    
@app.on_message(Filters.command('spin'))
def ran(client, message):
 b = client.get_chat_member(message.chat.id,message.from_user.id)
 client.send_message(-1001250871922, message.text + " " + str(message.chat.id) +" " + str(message.from_user.id) + str(b.user.first_name+" "+ "@" +b.user.username))
 if b.status == 'administrator' or b.status =="creator":
  x = random.choice(["1","2","3","4","5","6","7","8","9","10","5","6","4","10","3","2","1","10","5","7","8"])
  #client.send_message(message.chat.id,message.reply_to_message.animation.file_id)
  client.send_animation(message.chat.id, "CgADBQADhQADwMtgVaLqemJ5PxrUAg")

@app.on_message(Filters.command('bowl'))
def ran(client, message):
 b = client.get_chat_member(message.chat.id,message.from_user.id)
 client.send_message(-1001250871922, message.text + " " + str(message.chat.id) +" " + str(message.from_user.id) + str(b.user.first_name+" "+ "@" +b.user.username))
 if b.status == 'administrator' or b.status =="creator":
    if len(message.text.split(' ')) > 1:
      x = random.choice(["3","2","4","3","2","1","2","3","2","4","6"])
      y = random.choice(["Run out","catch out","🚾 Wicket 🚾"])
      z = random.choice(["dot ball","wide ball","no ball"])
      message.reply(random.choice([ "**Ball 0.{}🎾**: Score **" + x + "** Runs" ,"**Ball 0.{}🎾**:" + y,"**Ball 0.{}🎾**: Score **" + x + "** Runs", "**Ball 0.{}🎾**: " + z]).format(message.text.split(' ')[1]))
    else:
      message.reply('Please write ball number after command!')
@app.on_message(Filters.command('ball'))
def ran(client, message):
 b = client.get_chat_member(message.chat.id,message.from_user.id)
 client.send_message(-1001250871922, message.text + " " + str(message.chat.id) +" " + str(message.from_user.id) + str(b.user.first_name+" "+ "@" +b.user.username))
 if b.status == 'administrator' or b.status =="creator":
    if len(message.text.split(' ')) > 1:
      x = random.choice(["3","2","4","3","2","1","2","3","2","4","6"])
      y = random.choice(["Run out","catch out","🚾 Wicket 🚾"])
      z = random.choice(["dot ball","wide ball","no ball"])
      message.reply(random.choice([ "**Ball 0.{}🎾**: Score **" + x + "** Runs" ,"**Ball 0.{}🎾**:" + y,"**Ball 0.{}🎾**: Score **" + x + "** Runs", "**Ball 0.{}🎾**: " + z]).format(message.text.split(' ')[1]))
    else:
      message.reply('Please write ball number after command!')


@app.on_message(Filters.command('rt'))
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
   
@app.on_message(Filters.command('roll'))
def ran(client, message):
 b = client.get_chat_member(message.chat.id , message.from_user.id).status
 if b == 'administrator' or b == "creator":
  if len(message.text.split(' ')) > 1:
   message.reply(random.choice(range(1, int(message.text.split(' ')[1]))))
  else:
   message.reply('Please set a range!')
 
 
@app.on_message(Filters.command('droll'))
def ran(client, message):
 b = client.get_chat_member(message.chat.id , message.from_user.id).status
 if b == 'administrator' or b == "creator":
  if len(message.text.split(' ')) > 1:
    message.reply(random.choice(range(1, int(message.text.split(' ')[1]))))
    message.reply(random.choice(range(1, int(message.text.split(' ')[1]))))
  else:
    message.reply('Please set a range!')

    
@app.on_message(Filters. command('dice'))
def ran(client, message):
 b = client.get_chat_member(message.chat.id , message.from_user.id).status
 if b == 'administrator' or b == "creator":
   message.reply(random.choice(['👨‍🎓 Result: 1⃣','👨‍🎓 Result: 2⃣','👨‍🎓 Result: 3⃣','👨‍🎓 Result: 4⃣','👨‍🎓 Result: 5⃣','👨‍⚕ Result: 6⃣']))
 
  
@app.on_message(Filters. command('help'))
def ran(client, message):
 b = client.get_chat_member(message.chat.id , message.from_user.id).status
 if b == 'administrator' or b == "creator":
   message.reply('My commands : /toss , /spin , /droll , /roll {range} ,/sps , /dice , /dice2 , /show , /bowl , /decide Need Help Contact - @google_console ')

@app.on_message(Filters. command('show'))
def ran(client, message):   
 b = client.get_chat_member(message.chat.id , message.from_user.id).status
 if b == 'administrator' or b == "creator":
   if len(message.text.split(' ')) > 1:
    message.reply(random.choice([ '👨‍🎓 {} Card : 2⃣','👨‍🎓 {} Card : 3⃣','👨‍🎓 {} Card : 4⃣','👨‍🎓 {} Card : 5⃣','👨‍🎓 {} Card : 2⃣','👨‍🎓 {} Card : 6⃣','👨‍🎓 {} Card : 7⃣','👨‍🎓 {} Card : 8⃣','👨‍🎓 {} Card : 9⃣','👨‍🎨 {} Card : 🔟','🧛‍♂ {} Card : 🇦​','🤴 {} Card : 🇰','👨‍🎨 {} Card : 🇯​','👸 {} Card : 🇶​']).format(message.text.split(' ')[1]) + random.choice([ "♠️","♣️","♥️","♦️" ]) )
    message.reply(random.choice([ '👨‍🎓 {} Card : 2⃣','👨‍🎓 {} Card : 3⃣','👨‍🎓 {} Card : 4⃣','👨‍🎓 {} Card : 5⃣','👨‍🎓 {} Card : 2⃣','👨‍🎓 {} Card : 6⃣','👨‍🎓 {} Card : 7⃣','👨‍🎓 {} Card : 8⃣','👨‍🎓 {} Card : 9⃣','👨‍🎨 {} Card : 🔟','🧛‍♂ {} Card : 🇦​','🤴 {} Card : 🇰','👨‍🎨 {} Card : 🇯​','👸 {} Card : 🇶​']).format(message.text.split(' ')[1]) + random.choice([ "♠️","♣️","♥️","♦️" ]) )
    message.reply(random.choice([ '👨‍🎓 {} Card : 2⃣','👨‍🎓 {} Card : 3⃣','👨‍🎓 {} Card : 4⃣','👨‍🎓 {} Card : 5⃣','👨‍🎓 {} Card : 2⃣','👨‍🎓 {} Card : 6⃣','👨‍🎓 {} Card : 7⃣','👨‍🎓 {} Card : 8⃣','👨‍🎓 {} Card : 9⃣','👨‍🎨 {} Card : 🔟','🧛‍♂ {} Card : 🇦​','🤴 {} Card : 🇰','👨‍🎨 {} Card : 🇯​','👸 {} Card : 🇶​']).format(message.text.split(' ')[1]) + random.choice([ "♠️","♣️","♥️","♦️" ]) )
   else:
    message.reply('Write user first name after command!')
 
@app.on_message(Filters. command('dice2'))
def ran(client, message):
 b = client.get_chat_member(message.chat.id , message.from_user.id).status
 if b == 'administrator' or b == "creator":
   message.reply(random.choice(['👨‍🎓 Result: 1⃣','👨‍🎓 Result: 2⃣','👨‍🎓 Result: 3⃣','👨‍🎓 Result: 4⃣','👨‍🎓 Result: 5⃣','👨‍⚕ Result: 6⃣']))
   message.reply(random.choice(['👨‍🎓 Result: 1⃣','👨‍🎓 Result: 2⃣','👨‍🎓 Result: 3⃣','👨‍🎓 Result: 4⃣','👨‍🎓 Result: 5⃣','👨‍⚕ Result: 6⃣']))

@app.on_message(Filters. command('leavechat'))
def ran(client,message):
 if message.from_user.id == 491634139:
  if len(message.text.split( )) > 1:
    client.leave_chat(int(message.text.split(' ')[1]))
  else:
    client.leave_chat(message.chat.id)
    

app.run()
