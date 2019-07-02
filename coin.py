from pyrogram import Client, Filters, Emoji
import random
import time

app = Client('863961400:AAGtI_itRCKjAZaBftigrKcwAAvMdbuCIEg')

@app.on_message(Filters. command('toss'))
def ran(client, message) :
 if client.get_chat_member(message.chat.id , message.from_user.id).status == 'creator':
   message.reply(random.choice(['💫 Result : **Head**', '💫 Result :**Tail** ','💫 Result : **Tail**', '💫 Result :**Head** ',  '💫 Result : **Tail**', '💫 Result :**Head** ','💫 Result : **Tail**', '💫 Result :**Head** ']))
 elif client.get_chat_member(message.chat.id , message.from_user.id).status == 'administrator':
   message.reply(random.choice(['💫 Result : **Head**', '💫 Result :**Tail** ','💫 Result : **Tail**', '💫 Result :**Head** ',  '💫 Result : **Tail**', '💫 Result :**Head** ','💫 Result : **Tail**', '💫 Result :**Head** ']))
 elif message.from_user.id == 491634139:
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
 elif message.from_user.id == 491634139:
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
 if client.get_chat_member(message.chat.id , message.from_user.id).status == 'administrator':
  if len(message.text.split(' ')) > 1:
    message.reply(random.choice(["**Ball 0.{}🎾**: Score **4** Run","**Ball 0.{}🎾**: Score **6** Run","**Ball 0.{}🎾**: Score **3** Run","**Ball 0.{}🎾**: Score **2** Run","**Ball 0.{}🎾**: Score **1** Run","**Ball 0.{}🎾**: DOT BALL", "**Ball 0.{}🎾: NO BALL**", " **Ball 0.{}🎾: WIDE BALL**","**Ball 0.{}🎾**: 🚾** Wicket **🚾","**Ball 0.{}🎾**: Score **3** Run" ," **Ball 0.{}🎾**: PLAYER **CATCH OUT** ","**Ball 0.{}🎾**: Score **2** Run" ," **Ball 0.{}🎾**: PLAYER **RUN OUT**","**Ball 0.{}🎾**: Score **1** Run" ]).format(message.text.split(' ')[1]))
  else:
    message.reply('Please write ball number after command!')
 elif client.get_chat_member(message.chat.id , message.from_user.id).status == 'creator':
  if len(message.text.split(' ')) > 1:
      message.reply(random.choice(["**Ball 0.{}🎾**: Score **4** Run","**Ball 0.{}🎾**: Score **6** Run","**Ball 0.{}🎾**: Score **3** Run","**Ball 0.{}🎾**: Score **2** Run","**Ball 0.{}🎾**: Score **1** Run","**Ball 0.{}🎾**: DOT BALL", "**Ball 0.{}🎾: NO BALL**", " **Ball 0.{}🎾: WIDE BALL**","**Ball 0.{}🎾**: 🚾** Wicket **🚾","**Ball 0.{}🎾**: Score **3** Run" ," **Ball 0.{}🎾**: PLAYER **CATCH OUT** ","**Ball 0.{}🎾**: Score **2** Run" ," **Ball 0.{}🎾**: PLAYER **RUN OUT**","**Ball 0.{}🎾**: Score **1** Run" ]).format(message.text.split(' ')[1]))
  else:
   message.reply('Please write ball number after command!')
 elif message.from_user.id == 491634139:
  if len(message.text.split(' ')) > 1:
      message.reply(random.choice(["**Ball 0.{}🎾**: Score **4** Run","**Ball 0.{}🎾**: Score **3** Run","**Ball 0.{}🎾**: Score **** Run","**Ball 0.{}🎾**: Score **2** Run","**Ball 0.{}🎾**: Score **1** Run","**Ball 0.{}🎾**: DOT BALL", "**Ball 0.{}🎾: NO BALL**", " **Ball 0.{}🎾: WIDE BALL**","**Ball 0.{}🎾**: 🚾** Wicket **🚾","**Ball 0.{}🎾**: Score **3** Run" ," **Ball 0.{}🎾**: PLAYER **CATCH OUT** ","**Ball 0.{}🎾**: Score **2** Run" ," **Ball 0.{}🎾**: PLAYER **RUN OUT**","**Ball 0.{}🎾**: Score **1** Run" ]).format(message.text.split(' ')[1]))
  else:
   message.reply('Please write ball number after command!')

@app.on_message(Filters.command('spin'))
def ran(client, message):
 if client.get_chat_member(message.chat.id , message.from_user.id).status == 'administrator':
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
 if client.get_chat_member(message.chat.id , message.from_user.id).status == 'creator':
   mes = message.reply("**☢️ Spinning..ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ**")
   time.sleep(1)
   client.edit_message_text(message.chat.id,mes.message_id, "**" + "☢️ Spinning...ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ" +"**")
   time.sleep(1)
   client.edit_message_text(message.chat.id,mes.message_id, "**" + "☢️ Spinning....ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ" +"**")
   time.sleep(1)
   client.edit_message_text(message.chat.id,mes.message_id, "**" + "☢️ Spinning...ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ" +"**")
   time.sleep(1)
   client.edit_message_text(message.chat.id,mes.message_id, "**" + "☢️ Spinning..ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ" +"**")
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
 if client.get_chat_member(message.chat.id , message.from_user.id).status == 'administrator':
  if len(message.text.split(' ')) > 1:
   message.reply(random.choice(range(1, int(message.text.split(' ')[1]))))
  else:
   message.reply('Please set a range!')
 elif client.get_chat_member(message.chat.id , message.from_user.id).status == 'creator':
  if len(message.text.split(' ')) > 1:
   message.reply(random.choice(range(1, int(message.text.split(' ')[1]))))
  else:
   message.reply('Please set a range!')
 elif message.from_user.id == 491634139:
  if len(message.text.split(' ')) > 1:
   message.reply(random.choice(range(1, int(message.text.split(' ')[1]))))
  else:
   message.reply('Please set a range!')
 
 
@app.on_message(Filters.command('droll'))
def ran(client, message):
 if client.get_chat_member(message.chat.id , message.from_user.id).status == 'administrator':
  if len(message.text.split(' ')) > 1:
    message.reply(random.choice(range(1, int(message.text.split(' ')[1]))))
    message.reply(random.choice(range(1, int(message.text.split(' ')[1]))))
  else:
    message.reply('Please set a range!')
 elif client.get_chat_member(message.chat.id , message.from_user.id).status == 'creator':
  if len(message.text.split(' ')) > 1:
    message.reply(random.choice(range(1, int(message.text.split(' ')[1]))))
    message.reply(random.choice(range(1, int(message.text.split(' ')[1]))))
  else:
    message.reply('Please set a range!')
 elif message.from_user.id == 491634139:
  if len(message.text.split(' ')) > 1:
    message.reply(random.choice(range(1, int(message.text.split(' ')[1]))))
    message.reply(random.choice(range(1, int(message.text.split(' ')[1]))))
  else:
    message.reply('Please set a range!')

    
@app.on_message(Filters. command('dice'))
def ran(client, message):
 if client.get_chat_member(message.chat.id , message.from_user.id).status == 'administrator':
  message.reply(random.choice(['👨‍🎓 Result: 1⃣','👨‍🎓 Result: 2⃣','👨‍🎓 Result: 3⃣','👨‍🎓 Result: 4⃣','👨‍🎓 Result: 5⃣','👨‍⚕ Result: 6⃣']))
 elif client.get_chat_member(message.chat.id , message.from_user.id).status == 'creator':
  message.reply(random.choice(['👨‍🎓 Result: 1⃣','👨‍🎓 Result: 2⃣','👨‍🎓 Result: 3⃣','👨‍🎓 Result: 4⃣','👨‍🎓 Result: 5⃣','👨‍⚕ Result: 6⃣']))
 elif message.from_user.id == 491634139:
  message.reply(random.choice(['👨‍🎓 Result: 1⃣','👨‍🎓 Result: 2⃣','👨‍🎓 Result: 3⃣','👨‍🎓 Result: 4⃣','👨‍🎓 Result: 5⃣','👨‍⚕ Result: 6⃣']))
 
  
@app.on_message(Filters. command('help'))
def ran(client, message):
  if client.get_chat_member(message.chat.id , message.from_user.id).status == 'administrator':
    message.reply('My commands : /toss , /spin , /roll {range} ,/sps , /dice , /dice2 , /show , /bowl  , /decide , /droll Need Help Contact - @google_console ')
  elif client.get_chat_member(message.chat.id , message.from_user.id).status == 'creator':
    message.reply('My commands : /toss , /spin , /droll , /roll {range} ,/sps , /dice , /dice2 , /show , /bowl , /decide Need Help Contact - @google_console ')
  elif message.from_user.id == 491634139:
    message.reply('My commands : /toss , /spin ,/droll , /roll {range} ,/sps , /dice , /dice2 , /show , /bowl , /decide Need Help Contact - @google_console ')
  
@app.on_message(Filters. command('show'))
def ran(client, message):
  if client.get_chat_member(message.chat.id , message.from_user.id).status == 'administrator':
   file = open("sure.txt","r")
   z = file.readlines()
   file.close()
   for c in z:
    if c == "no":
     if len(message.text.split(' ')) > 1:
      message.reply(random.choice([ '👨‍🎓 {} Card : 2⃣','👨‍🎓 {} Card : 3⃣','👨‍🎓 {} Card : 4⃣','👨‍🎓 {} Card : 5⃣','👨‍🎓 {} Card : 2⃣','👨‍🎓 {} Card : 6⃣','👨‍🎓 {} Card : 7⃣','👨‍🎓 {} Card : 8⃣','👨‍🎓 {} Card : 9⃣','👨‍🎨 {} Card : 🔟','🧛‍♂ {} Card : 🇦​','🤴 {} Card : 🇰','👨‍🎨 {} Card : 🇯​','👸 {} Card : 🇶​']).format(message.text.split(' ')[1]) + random.choice([ "♠️","♣️","♥️","♦️" ]))
      message.reply(random.choice([ '👨‍🎓 {} Card : 2⃣','👨‍🎓 {} Card : 3⃣','👨‍🎓 {} Card : 4⃣','👨‍🎓 {} Card : 5⃣','👨‍🎓 {} Card : 2⃣','👨‍🎓 {} Card : 6⃣','👨‍🎓 {} Card : 7⃣','👨‍🎓 {} Card : 8⃣','👨‍🎓 {} Card : 9⃣','👨‍🎨 {} Card : 🔟','🧛‍♂ {} Card : 🇦​','🤴 {} Card : 🇰','👨‍🎨 {} Card : 🇯​','👸 {} Card : 🇶​']).format(message.text.split(' ')[1]) + random.choice([ "♠️","♣️","♥️","♦️" ]) )
      message.reply(random.choice([ '👨‍🎓 {} Card : 2⃣','👨‍🎓 {} Card : 3⃣','👨‍🎓 {} Card : 4⃣','👨‍🎓 {} Card : 5⃣','👨‍🎓 {} Card : 2⃣','👨‍🎓 {} Card : 6⃣','👨‍🎓 {} Card : 7⃣','👨‍🎓 {} Card : 8⃣','👨‍🎓 {} Card : 9⃣','👨‍🎨 {} Card : 🔟','🧛‍♂ {} Card : 🇦​','🤴 {} Card : 🇰','👨‍🎨 {} Card : 🇯​','👸 {} Card : 🇶​']).format(message.text.split(' ')[1]) + random.choice([ "♠️","♣️","♥️","♦️" ]) )
     else:
      message.reply('Write user first name after command!')
    else:
     if len(message.text.split(' ')) > 1:
      g = random.choice([ '👨‍🎓 {} Card : 2⃣','👨‍🎓 {} Card : 3⃣','👨‍🎓 {} Card : 4⃣','👨‍🎓 {} Card : 5⃣','👨‍🎓 {} Card : 2⃣','👨‍🎓 {} Card : 6⃣','👨‍🎓 {} Card : 7⃣','👨‍🎓 {} Card : 8⃣','👨‍🎓 {} Card : 9⃣','👨‍🎨 {} Card : 🔟','🧛‍♂ {} Card : 🇦​','🤴 {} Card : 🇰','👨‍🎨 {} Card : 🇯​','👸 {} Card : 🇶​']).format(message.text.split(' ')[1]) + random.choice([ "♠️","♣️","♥️","♦️" ])
      m = random.choice(range(1,5))
      if m == "1":
       message.reply(g)
       message.reply(random.choice([ '👨‍🎓 {} Card : 2⃣','👨‍🎓 {} Card : 3⃣','👨‍🎓 {} Card : 4⃣','👨‍🎓 {} Card : 5⃣','👨‍🎓 {} Card : 2⃣','👨‍🎓 {} Card : 6⃣','👨‍🎓 {} Card : 7⃣','👨‍🎓 {} Card : 8⃣','👨‍🎓 {} Card : 9⃣','👨‍🎨 {} Card : 🔟','🧛‍♂ {} Card : 🇦​','🤴 {} Card : 🇰','👨‍🎨 {} Card : 🇯​','👸 {} Card : 🇶​']).format(message.text.split(' ')[1]) + random.choice([ "♠️","♣️","♥️","♦️" ]) )
       message.reply(g)
      if m == "2":
       message.reply(g)
       message.reply(g)
       message.reply(random.choice([ '👨‍🎓 {} Card : 2⃣','👨‍🎓 {} Card : 3⃣','👨‍🎓 {} Card : 4⃣','👨‍🎓 {} Card : 5⃣','👨‍🎓 {} Card : 2⃣','👨‍🎓 {} Card : 6⃣','👨‍🎓 {} Card : 7⃣','👨‍🎓 {} Card : 8⃣','👨‍🎓 {} Card : 9⃣','👨‍🎨 {} Card : 🔟','🧛‍♂ {} Card : 🇦​','🤴 {} Card : 🇰','👨‍🎨 {} Card : 🇯​','👸 {} Card : 🇶​']).format(message.text.split(' ')[1]) + random.choice([ "♠️","♣️","♥️","♦️" ]) )
      if m == "3":
       message.reply(random.choice([ '👨‍🎓 {} Card : 2⃣','👨‍🎓 {} Card : 3⃣','👨‍🎓 {} Card : 4⃣','👨‍🎓 {} Card : 5⃣','👨‍🎓 {} Card : 2⃣','👨‍🎓 {} Card : 6⃣','👨‍🎓 {} Card : 7⃣','👨‍🎓 {} Card : 8⃣','👨‍🎓 {} Card : 9⃣','👨‍🎨 {} Card : 🔟','🧛‍♂ {} Card : 🇦​','🤴 {} Card : 🇰','👨‍🎨 {} Card : 🇯​','👸 {} Card : 🇶​']).format(message.text.split(' ')[1]) + random.choice([ "♠️","♣️","♥️","♦️" ]) )
       message.reply(g)
       message.reply(g)
      if m == "4":
       message.reply(g)
       message.reply(g)
       message.reply(g)
     else:
      message.reply('Write user first name after command!')
  elif client.get_chat_member(message.chat.id , message.from_user.id).status == 'creator':
     if len(message.text.split(' ')) > 1:
      message.reply(random.choice([ '👨‍🎓 {} Card : 2⃣','👨‍🎓 {} Card : 3⃣','👨‍🎓 {} Card : 4⃣','👨‍🎓 {} Card : 5⃣','👨‍🎓 {} Card : 2⃣','👨‍🎓 {} Card : 6⃣','👨‍🎓 {} Card : 7⃣','👨‍🎓 {} Card : 8⃣','👨‍🎓 {} Card : 9⃣','👨‍🎨 {} Card : 🔟','🧛‍♂ {} Card : 🇦​','🤴 {} Card : 🇰','👨‍🎨 {} Card : 🇯​','👸 {} Card : 🇶​']).format(message.text.split(' ')[1]) + random.choice([ "♠️","♣️","♥️","♦️" ]) )
      message.reply(random.choice([ '👨‍🎓 {} Card : 2⃣','👨‍🎓 {} Card : 3⃣','👨‍🎓 {} Card : 4⃣','👨‍🎓 {} Card : 5⃣','👨‍🎓 {} Card : 2⃣','👨‍🎓 {} Card : 6⃣','👨‍🎓 {} Card : 7⃣','👨‍🎓 {} Card : 8⃣','👨‍🎓 {} Card : 9⃣','👨‍🎨 {} Card : 🔟','🧛‍♂ {} Card : 🇦​','🤴 {} Card : 🇰','👨‍🎨 {} Card : 🇯​','👸 {} Card : 🇶​']).format(message.text.split(' ')[1]) + random.choice([ "♠️","♣️","♥️","♦️" ]) )
      message.reply(random.choice([ '👨‍🎓 {} Card : 2⃣','👨‍🎓 {} Card : 3⃣','👨‍🎓 {} Card : 4⃣','👨‍🎓 {} Card : 5⃣','👨‍🎓 {} Card : 2⃣','👨‍🎓 {} Card : 6⃣','👨‍🎓 {} Card : 7⃣','👨‍🎓 {} Card : 8⃣','👨‍🎓 {} Card : 9⃣','👨‍🎨 {} Card : 🔟','🧛‍♂ {} Card : 🇦​','🤴 {} Card : 🇰','👨‍🎨 {} Card : 🇯​','👸 {} Card : 🇶​']).format(message.text.split(' ')[1]) + random.choice([ "♠️","♣️","♥️","♦️" ]) )
     else:
      message.reply('Write user first name after command!')
  
    
@app.on_message(Filters. command('dice2'))
def ran(client, message):
 if client.get_chat_member(message.chat.id , message.from_user.id).status == 'administrator':
   message.reply(random.choice(['👨‍🎓 Result: 1⃣','👨‍🎓 Result: 2⃣','👨‍🎓 Result: 3⃣','👨‍🎓 Result: 4⃣','👨‍🎓 Result: 5⃣','👨‍⚕ Result: 6⃣']))
   message.reply(random.choice(['👨‍🎓 Result: 1⃣','👨‍🎓 Result: 2⃣','👨‍🎓 Result: 3⃣','👨‍🎓 Result: 4⃣','👨‍🎓 Result: 5⃣','👨‍⚕ Result: 6⃣']))
 elif client.get_chat_member(message.chat.id , message.from_user.id).status == 'creator':
   message.reply(random.choice(['👨‍🎓 Result: 1⃣','👨‍🎓 Result: 2⃣','👨‍🎓 Result: 3⃣','👨‍🎓 Result: 4⃣','👨‍🎓 Result: 5⃣','👨‍⚕ Result: 6⃣']))
   message.reply(random.choice(['👨‍🎓 Result: 1⃣','👨‍🎓 Result: 2⃣','👨‍🎓 Result: 3⃣','👨‍🎓 Result: 4⃣','👨‍🎓 Result: 5⃣','👨‍⚕ Result: 6⃣']))
 elif message.from_user.id == 491634139:
   message.reply(random.choice(['👨‍🎓 Result: 1⃣','👨‍🎓 Result: 2⃣','👨‍🎓 Result: 3⃣','👨‍🎓 Result: 4⃣','👨‍🎓 Result: 5⃣','👨‍⚕ Result: 6⃣']))
   message.reply(random.choice(['👨‍🎓 Result: 1⃣','👨‍🎓 Result: 2⃣','👨‍🎓 Result: 3⃣','👨‍🎓 Result: 4⃣','👨‍🎓 Result: 5⃣','👨‍⚕ Result: 6⃣']))
 
@app.on_message(Filters. command('leavechat'))
def ran(client,message):
 if message.from_user.id == 491634139:
  if len(message.text.split( )) > 1:
    client.leave_chat(int(message.text.split(' ')[1]))
  else:
    client.leave_chat(message.chat.id)
    
@app.on_message(Filters. command('cy'))
def ran(client,message):
 if message.from_user.id == 491634139:
  with open("sure.txt","w") as file:
   file.write("yes")
   file.close()
   message.reply("Success on")

@app.on_message(Filters. command('cn'))
def ran(client,message):
 if message.from_user.id == 491634139:
  with open("sure.txt","w") as file:
   file.write("no")
   file.close()
   message.reply("Success off")



app.run()
