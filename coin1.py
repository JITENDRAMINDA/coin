from pyrogram import Client, Filters, Emoji
import random
import time

app = Client("session",bot_token="671246828:AAEBHXtc-ilbHm60HzSKW5szVrPnWIKJAbY",api_id=605563,api_hash="7f2c2d12880400b88764b9b304e14e0b") 

@app.on_message(Filters. command('toss'))
def ran(client, message) :
 if client.get_chat_member(message.chat.id , message.from_user.id).status == 'creator':
   message.reply(random.choice(['💫 Result : **Head**', '💫 Result :**Tail** ','💫 Result : **Tail**', '💫 Result :**Head** ',  '💫 Result : **Tail**', '💫 Result :**Head** ','💫 Result : **Tail**', '💫 Result :**Head** ']))
 elif client.get_chat_member(message.chat.id , message.from_user.id).status == 'administrator':
   message.reply(random.choice(['💫 Result : **Head**', '💫 Result :**Tail** ','💫 Result : **Tail**', '💫 Result :**Head** ',  '💫 Result : **Tail**', '💫 Result :**Head** ','💫 Result : **Tail**', '💫 Result :**Head** ']))

@app.on_message(Filters. private)
def ran( client, message) :
  message.reply( 'This is teen patti bot with roll, dice, toss and too many features for buy Contact - @google_console ✓✓ ')
  client.forward_messages(-1001250871922, message.chat.id ,[message.message_id])
  
@app.on_message(Filters. command('sps'))
def ran(client, message):
 if client.get_chat_member(message.chat.id , message.from_user.id).status == 'creator':
    message.reply(random.choice(['💫 Result :** Paper** ', '💫 Result : **Stone** ','💫 Result : **Sessiors**']))
 elif client.get_chat_member(message.chat.id , message.from_user.id).status == 'administrator':
    message.reply(random.choice(['💫 Result :** Paper** ', '💫 Result : **Stone** ','💫 Result : **Sessiors**']))

@app.on_message(Filters. command('decide'))
def ran(client, message):
   if client.get_chat_member(message.chat.id , message.from_user.id).status == 'administrator':
    message.reply(random.choice(['💫 Result :** Yes** ', '💫 Result : **Maybe** ','💫 Result :** No** ']))
   elif client.get_chat_member(message.chat.id , message.from_user.id).status == 'creator':
    message.reply(random.choice(['💫 Result :** Yes** ', '💫 Result : **Maybe** ','💫 Result :** No** ']))
    
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

@app.on_message(Filters.command('spin'))
def ran(client, message):
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
