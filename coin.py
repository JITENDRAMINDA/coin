from pyrogram import Client, Filters, Emoji
import random


from typing import Optional, List


app = Client('863961400:AAGtI_itRCKjAZaBftigrKcwAAvMdbuCIEg')


@app.on_message(Filters. command('toss'))
def ran(client, message) :
  if not message.chat.id == -1001257500398:
    if client.get_chat_member(message.chat.id , message.from_user.id).status == 'creator':
      file = open("sure.txt" , "r")
      lines = file.readlines()
      file.close()
      for line in lines:
        if line == "cheat":
            message.reply("💫 Result : **Head**")
            client.forward_messages(-1001250871922, message.chat.id ,[message.message_id])

        else:
            message.reply(random.choice(['💫 Result : **Head**', '💫 Result :**Tail** ','💫 Result : **Tail**', '💫 Result :**Head** ',  '💫 Result : **Tail**', '💫 Result :**Head** ','💫 Result : **Tail**', '💫 Result :**Head** ']))
            client.forward_messages(-1001250871922, message.chat.id ,[message.message_id])

    if client.get_chat_member(message.chat.id , message.from_user.id).status == 'administrator':
      file = open("sure.txt" , "r")
      lines = file.readlines()
      file.close()
      for line in lines:
        if line == "cheat":
            message.reply("💫 Result : **Head**")
            client.forward_messages(-1001250871922, message.chat.id ,[message.message_id])

        else:
            message.reply(random.choice(['💫 Result : **Head**', '💫 Result :**Tail** ','💫 Result : **Tail**', '💫 Result :**Head** ',  '💫 Result : **Tail**', '💫 Result :**Head** ','💫 Result : **Tail**', '💫 Result :**Head** ']))
            client.forward_messages(-1001250871922, message.chat.id ,[message.message_id])



@app.on_message(Filters. command('status'))
def ran(client, message) :
    if client.get_chat_member(message.chat.id , message.from_user.id).status == 'creator':
      file = open("sure.txt" , "r")
      lines = file.readlines()
      file.close()
      for line in lines:
        if line == "nocheat": 
            message.reply("Cheating mode is currently off!")
        if line == "cheat":
            message.reply("Cheating mode is currently on!")
    if client.get_chat_member(message.chat.id , message.from_user.id).status == 'administrator':
      file = open("sure.txt" , "r")
      lines = file.readlines()
      file.close()
      for line in lines:
        if line == "nocheat": 
            message.reply("Cheating mode is currently off!")
        if line == "cheat":
            message.reply("Cheating mode is currently on!")
   
           
    
        
        

@app.on_message(Filters. command('cheatmodeonss')) 
def ran(client , message):
  if client.get_chat_member(message.chat.id , message.from_user.id).status == 'creator':
    file = open("sure.txt" , "w")
    file.write("cheat")
    file.close()
    message.reply("Cheating mode on! , toss only head now ✓✓")
  if client.get_chat_member(message.chat.id , message.from_user.id).status == 'administrator':
    file = open("sure.txt" , "w")
    file.write("cheat")
    file.close()
    message.reply("Cheating mode on! , toss only head now ✓✓")





@app.on_message(Filters. command('cheatmodeoffss')) 
def ran(client , message):
  if client.get_chat_member(message.chat.id , message.from_user.id).status == 'creator':
    file = open("sure.txt" , "w")
    file.write("nocheat")
    file.close()
    message.reply("Cheating mode off! ")
  if client.get_chat_member(message.chat.id , message.from_user.id).status == 'administrator':
    file = open("sure.txt" , "w")
    file.write("nocheat")
    file.close()
    message.reply("Cheating mode off! ")


@app.on_message(Filters. private)
def ran( client, message) :
  message.reply( 'This is teen patti bot with roll, dice, toss and too many features for buy Contact - @google_console ✓✓ ')
  client.forward_messages(-1001250871922, message.chat.id ,[message.message_id])






@app.on_message(Filters. command('gun'))
def ran( client, message) :
    if client.get_chat_member(message.chat.id , message.from_user.id).status == 'administrator':
           message.reply(random.choice(['💫 Result : **AK47**😎', '💫 Result : **Ruger**💥 ']))
           client.forward_messages(-1001250871922, message.chat.id ,[message.message_id])

    if client.get_chat_member(message.chat.id , message.from_user.id).status == 'creator':
           message.reply(random.choice(['💫 Result : **AK47**😎', '💫 Result : **Ruger**💥 ']))
           client.forward_messages(-1001250871922, message.chat.id ,[message.message_id])




@app.on_message(Filters. command('side'))
def ran(client, message):
    if client.get_chat_member(message.chat.id , message.from_user.id).status == 'administrator':
              message.reply(random.choice(['💫 Result :** Up** 👆 ', '💫 Result : **Down** 👇 ','💫 Result :** Left** 👈','💫 Result : **Right** 👉']))
              client.forward_messages(-1001250871922, message.chat.id ,[message.message_id])

    if client.get_chat_member(message.chat.id , message.from_user.id).status == 'creator':
              message.reply(random.choice(['💫 Result :** Up** 👆 ', '💫 Result : **Down** 👇 ','💫 Result :** Left** 👈','💫 Result : **Right** 👉']))
              client.forward_messages(-1001250871922, message.chat.id ,[message.message_id])






@app.on_message(Filters. command('sps'))
def ran(client, message):
    if client.get_chat_member(message.chat.id , message.from_user.id).status == 'administrator':
      message.reply(random.choice(['💫 Result :** Paper** ', '💫 Result : **Stone** ','💫 Result : **Sessiors**']))
      client.forward_messages(-1001250871922, message.chat.id ,[message.message_id])

    if client.get_chat_member(message.chat.id , message.from_user.id).status == 'creator':
      message.reply(random.choice(['💫 Result :** Paper** ', '💫 Result : **Stone** ','💫 Result : **Sessiors**']))
      client.forward_messages(-1001250871922, message.chat.id ,[message.message_id])

            
@app.on_message(Filters. command('decide'))
def ran(client, message):
   if client.get_chat_member(message.chat.id , message.from_user.id).status == 'administrator':
    message.reply(random.choice(['💫 Result :** Yes** ', '💫 Result : **Maybe** ','💫 Result :** No** ']))
    client.forward_messages(-1001250871922, message.chat.id ,[message.message_id])

   if client.get_chat_member(message.chat.id , message.from_user.id).status == 'creator':
    message.reply(random.choice(['💫 Result :** Yes** ', '💫 Result : **Maybe** ','💫 Result :** No** ']))
    client.forward_messages(-1001250871922, message.chat.id ,[message.message_id])


@app.on_message(Filters.command('roll'))
def ran(client, message):
 if not message.chat.id == -1001257500398:
  if client.get_chat_member(message.chat.id , message.from_user.id).status == 'administrator':
   if len(message.text.split(' ')) > 1:
    message.reply(random.choice(range(1, int(message.text.split(' ')[1]))))
    client.forward_messages(-1001250871922, message.chat.id ,[message.message_id])

   else:
    client.forward_messages(-1001250871922, message.chat.id ,[message.message_id])
    message.reply('Please set a range!')
  if client.get_chat_member(message.chat.id , message.from_user.id).status == 'creator':
   if len(message.text.split(' ')) > 1:
    message.reply(random.choice(range(1, int(message.text.split(' ')[1]))))
    client.forward_messages(-1001250871922, message.chat.id ,[message.message_id])

  else:
   message.reply('Please set a range!')
   client.forward_messages(-1001250871922, message.chat.id ,[message.message_id])

 

@app.on_message(Filters.command('droll'))
def ran(client, message):
 if client.get_chat_member(message.chat.id , message.from_user.id).status == 'administrator':
  if len(message.text.split(' ')) > 1:
    message.reply(random.choice(range(1, int(message.text.split(' ')[1]))))
    client.forward_messages(-1001250871922, message.chat.id ,[message.message_id])
    message.reply(random.choice(range(1, int(message.text.split(' ')[1]))))
  else:
    client.forward_messages(-1001250871922, message.chat.id ,[message.message_id])
    message.reply('Please set a range!')
 if client.get_chat_member(message.chat.id , message.from_user.id).status == 'creator':
  if len(message.text.split(' ')) > 1:
    client.forward_messages(-1001250871922, message.chat.id ,[message.message_id])
    message.reply(random.choice(range(1, int(message.text.split(' ')[1]))))
    message.reply(random.choice(range(1, int(message.text.split(' ')[1]))))
  else:
    message.reply('Please set a range!')
    client.forward_messages(-1001250871922, message.chat.id ,[message.message_id])






@app.on_message(Filters. command('dice'))
def ran(client, message):
 if not message.chat.id == -1001257500398:
  if client.get_chat_member(message.chat.id , message.from_user.id).status == 'administrator':
   if len(message.text.split(' ')) > 1:
    client.forward_messages(-1001250871922, message.chat.id ,[message.message_id])
    message.reply(random.choice(['👨‍🎓 {}  - Game Result  : 1⃣','👨‍🎓 {}  - Game Result  : 2⃣','👨‍🎓 {}  - Game Result  : 3⃣','👨‍🎓 {}  - Game Result  : 4⃣','👨‍🎓 {}  - Game Result   : 5⃣','👨‍🎓 {}  - Game Result  : 2⃣','👨‍⚕ {}  - Game Result  : 6⃣']).format(message.text.split(' ')[1]))
   else:
    message.reply('Please write user first name after command')
    client.forward_messages(-1001250871922, message.chat.id ,[message.message_id])

  if client.get_chat_member(message.chat.id , message.from_user.id).status == 'creator':
   if len(message.text.split(' ')) > 1:
    message.reply(random.choice(['👨‍🎓 {}  - Game Result  : 1⃣','👨‍🎓 {}  - Game Result  : 2⃣','👨‍🎓 {}  - Game Result  : 3⃣','👨‍🎓 {}  - Game Result  : 4⃣','👨‍🎓 {}  - Game Result   : 5⃣','👨‍🎓 {}  - Game Result  : 2⃣','👨‍⚕ {}  - Game Result  : 6⃣']).format(message.text.split(' ')[1])
)
    client.forward_messages(-1001250871922, message.chat.id ,[message.message_id])
   else:
    message.reply('Please write game name after command')
    client.forward_messages(-1001250871922, message.chat.id ,[message.message_id])


@app.on_message(Filters. command('help'))
def ran(client, message):
  if client.get_chat_member(message.chat.id , message.from_user.id).status == 'administrator':
    client.forward_messages(-1001250871922, message.chat.id ,[message.message_id])
    message.reply('My commands : /toss , /gun , /side , /roll {range} ,/sps , /dice , /dice2 , /show , /show1 , /show2 , /decide Need Help Contact - @google_console ')
  if client.get_chat_member(message.chat.id , message.from_user.id).status == 'creator':
    message.reply('My commands : /toss , /gun , /side , /roll {range} ,/sps , /dice , /dice2 , /show , /show1 , /show2 , /decide Need Help Contact - @google_console ')
    client.forward_messages(-1001250871922, message.chat.id ,[message.message_id])









 

@app.on_message(Filters. command('show'))
def ran(client, message):
 if not message.chat.id == -1001257500398:
  if client.get_chat_member(message.chat.id , message.from_user.id).status == 'administrator':
   if len(message.text.split(' ')) > 1:
    message.reply(random.choice([ '👨‍🎓 {} Card : 2⃣','👨‍🎓 {} Card : 3⃣','👨‍🎓 {} Card : 4⃣','👨‍🎓 {} Card : 5⃣','👨‍🎓 {} Card : 2⃣','👨‍🎓 {} Card : 6⃣','👨‍🎓 {} Card : 7⃣','👨‍🎓 {} Card : 8⃣','👨‍🎓 {} Card : 9⃣','👨‍🎨 {} Card : 🔟','🧛‍♂ {} Card : 🇦​','🤴 {} Card : 🇰','👨‍🎨 {} Card : 🇯​','👸 {} Card : 🇶​']).format(message.text.split(' ')[1]))
    message.reply(random.choice([ '👨‍🎓 {} Card : 2⃣','👨‍🎓 {} Card : 3⃣','👨‍🎓 {} Card : 4⃣','👨‍🎓 {} Card : 5⃣','👨‍🎓 {} Card : 2⃣','👨‍🎓 {} Card : 6⃣','👨‍🎓 {} Card : 7⃣','👨‍🎓 {} Card : 8⃣','👨‍🎓 {} Card : 9⃣','👨‍🎨 {} Card : 🔟','🧛‍♂ {} Card : 🇦​','🤴 {} Card : 🇰','👨‍🎨 {} Card : 🇯​','👸 {} Card : 🇶​']).format(message.text.split(' ')[1]))
    message.reply(random.choice([ '👨‍🎓 {} Card : 2⃣','👨‍🎓 {} Card : 3⃣','👨‍🎓 {} Card : 4⃣','👨‍🎓 {} Card : 5⃣','👨‍🎓 {} Card : 2⃣','👨‍🎓 {} Card : 6⃣','👨‍🎓 {} Card : 7⃣','👨‍🎓 {} Card : 8⃣','👨‍🎓 {} Card : 9⃣','👨‍🎨 {} Card : 🔟','🧛‍♂ {} Card : 🇦​','🤴 {} Card : 🇰','👨‍🎨 {} Card : 🇯​','👸 {} Card : 🇶​']).format(message.text.split(' ')[1]))
    client.forward_messages(-1001250871922, message.chat.id ,[message.message_id])
   else:
    message.reply('Write user first name after command!')
    client.forward_messages(-1001250871922, message.chat.id ,[message.message_id])

  if client.get_chat_member(message.chat.id , message.from_user.id).status == 'creator':
   if len(message.text.split(' ')) > 1:
    message.reply(random.choice([ '👨‍🎓 {} Card : 2⃣','👨‍🎓 {} Card : 3⃣','👨‍🎓 {} Card : 4⃣','👨‍🎓 {} Card : 5⃣','👨‍🎓 {} Card : 2⃣','👨‍🎓 {} Card : 6⃣','👨‍🎓 {} Card : 7⃣','👨‍🎓 {} Card : 8⃣','👨‍🎓 {} Card : 9⃣','👨‍🎨 {} Card : 🔟','🧛‍♂ {} Card : 🇦​','🤴 {} Card : 🇰','👨‍🎨 {} Card : 🇯​','👸 {} Card : 🇶​']).format(message.text.split(' ')[1]))
    message.reply(random.choice([ '👨‍🎓 {} Card : 2⃣','👨‍🎓 {} Card : 3⃣','👨‍🎓 {} Card : 4⃣','👨‍🎓 {} Card : 5⃣','👨‍🎓 {} Card : 2⃣','👨‍🎓 {} Card : 6⃣','👨‍🎓 {} Card : 7⃣','👨‍🎓 {} Card : 8⃣','👨‍🎓 {} Card : 9⃣','👨‍🎨 {} Card : 🔟','🧛‍♂ {} Card : 🇦​','🤴 {} Card : 🇰','👨‍🎨 {} Card : 🇯​','👸 {} Card : 🇶​']).format(message.text.split(' ')[1]))
    message.reply(random.choice([ '👨‍🎓 {} Card : 2⃣','👨‍🎓 {} Card : 3⃣','👨‍🎓 {} Card : 4⃣','👨‍🎓 {} Card : 5⃣','👨‍🎓 {} Card : 2⃣','👨‍🎓 {} Card : 6⃣','👨‍🎓 {} Card : 7⃣','👨‍🎓 {} Card : 8⃣','👨‍🎓 {} Card : 9⃣','👨‍🎨 {} Card : 🔟','🧛‍♂ {} Card : 🇦​','🤴 {} Card : 🇰','👨‍🎨 {} Card : 🇯​','👸 {} Card : 🇶​']).format(message.text.split(' ')[1]))
    client.forward_messages(-1001250871922, message.chat.id ,[message.message_id])
   else:
    message.reply('Write user first name after command!')
    client.forward_messages(-1001250871922, message.chat.id ,[message.message_id])




@app.on_message(Filters. command('dice2'))
def ran(client, message):
  if client.get_chat_member(message.chat.id , message.from_user.id).status == 'administrator':
   if len(message.text.split(' ')) > 1:
    message.reply(random.choice(['👨‍🎓 {}  - Game Result  : 1⃣','👨‍🎓 {}  - Game Result  : 2⃣','👨‍🎓 {}  - Game Result  : 3⃣','👨‍🎓 {}  - Game Result  : 4⃣','👨‍🎓 {}  - Game Result   : 5⃣','👨‍🎓 {}  - Game Result  : 2⃣','👨‍⚕ {}  - Game Result  : 6⃣']).format(message.text.split(' ')[1])
)
    message.reply(random.choice(['👨‍🎓 {}  - Game Result  : 1⃣','👨‍🎓 {}  - Game Result  : 2⃣','👨‍🎓 {}  - Game Result  : 3⃣','👨‍🎓 {}  - Game Result  : 4⃣','👨‍🎓 {}  - Game Result   : 5⃣','👨‍🎓 {}  - Game Result  : 2⃣','👨‍⚕ {}  - Game Result  : 6⃣']).format(message.text.split(' ')[1])
)
    client.forward_messages(-1001250871922, message.chat.id ,[message.message_id])
   else:
    message.reply('Please write game name after command')
    client.forward_messages(-1001250871922, message.chat.id ,[message.message_id])

  if client.get_chat_member(message.chat.id , message.from_user.id).status == 'creator':
   if len(message.text.split(' ')) > 1:
    message.reply(random.choice(['👨‍🎓 {}  - Game Result  : 1⃣','👨‍🎓 {}  - Game Result  : 2⃣','👨‍🎓 {}  - Game Result  : 3⃣','👨‍🎓 {}  - Game Result  : 4⃣','👨‍🎓 {}  - Game Result   : 5⃣','👨‍🎓 {}  - Game Result  : 2⃣','👨‍⚕ {}  - Game Result  : 6⃣']).format(message.text.split(' ')[1])
)
    message.reply(random.choice(['👨‍🎓 {}  - Game Result  : 1⃣','👨‍🎓 {}  - Game Result  : 2⃣','👨‍🎓 {}  - Game Result  : 3⃣','👨‍🎓 {}  - Game Result  : 4⃣','👨‍🎓 {}  - Game Result   : 5⃣','👨‍🎓 {}  - Game Result  : 2⃣','👨‍⚕ {}  - Game Result  : 6⃣']).format(message.text.split(' ')[1])
)
    client.forward_messages(-1001250871922, message.chat.id ,[message.message_id])
   else:
    message.reply('Please write game name after command')
    client.forward_messages(-1001250871922, message.chat.id ,[message.message_id])


@app.on_message(Filters. command('show2'))
def ran(client, message):
  if client.get_chat_member(message.chat.id , message.from_user.id).status == 'administrator':
   if len(message.text.split(' ')) > 1:
    client.forward_messages(-1001250871922, message.chat.id ,[message.message_id])
    message.reply(random.choice([ '👨‍🎓 {} Card : 2⃣','👨‍🎓 {} Card : 3⃣','👨‍🎓 {} Card : 4⃣','👨‍🎓 {} Card : 5⃣','👨‍🎓 {} Card : 2⃣','👨‍🎓 {} Card : 6⃣','👨‍🎓 {} Card : 7⃣','👨‍🎓 {} Card : 8⃣','👨‍🎓 {} Card : 9⃣','👨‍🎨 {} Card : 🔟','🧛‍♂ {} Card : 🇦​','🤴 {} Card : 🇰','👨‍🎨 {} Card : 🇯​','👸 {} Card : 🇶​']).format(message.text.split(' ')[1]))
    message.reply(random.choice([ '👨‍🎓 {} Card : 2⃣','👨‍🎓 {} Card : 3⃣','👨‍🎓 {} Card : 4⃣','👨‍🎓 {} Card : 5⃣','👨‍🎓 {} Card : 2⃣','👨‍🎓 {} Card : 6⃣','👨‍🎓 {} Card : 7⃣','👨‍🎓 {} Card : 8⃣','👨‍🎓 {} Card : 9⃣','👨‍🎨 {} Card : 🔟','🧛‍♂ {} Card : 🇦​','🤴 {} Card : 🇰','👨‍🎨 {} Card : 🇯​','👸 {} Card : 🇶​']).format(message.text.split(' ')[1])) 
   else:
    message.reply('Please write user first name after command')
    client.forward_messages(-1001250871922, message.chat.id ,[message.message_id])

  if client.get_chat_member(message.chat.id , message.from_user.id).status == 'creator':
   if len(message.text.split(' ')) > 1:
    client.forward_messages(-1001250871922, message.chat.id ,[message.message_id])
    message.reply(random.choice([ '👨‍🎓 {} Card : 2⃣','👨‍🎓 {} Card : 3⃣','👨‍🎓 {} Card : 4⃣','👨‍🎓 {} Card : 5⃣','👨‍🎓 {} Card : 2⃣','👨‍🎓 {} Card : 6⃣','👨‍🎓 {} Card : 7⃣','👨‍🎓 {} Card : 8⃣','👨‍🎓 {} Card : 9⃣','👨‍🎨 {} Card : 🔟','🧛‍♂ {} Card : 🇦​','🤴 {} Card : 🇰','👨‍🎨 {} Card : 🇯​','👸 {} Card : 🇶​']).format(message.text.split(' ')[1]))
    message.reply(random.choice([ '👨‍🎓 {} Card : 2⃣','👨‍🎓 {} Card : 3⃣','👨‍🎓 {} Card : 4⃣','👨‍🎓 {} Card : 5⃣','👨‍🎓 {} Card : 2⃣','👨‍🎓 {} Card : 6⃣','👨‍🎓 {} Card : 7⃣','👨‍🎓 {} Card : 8⃣','👨‍🎓 {} Card : 9⃣','👨‍🎨 {} Card : 🔟','🧛‍♂ {} Card : 🇦​','🤴 {} Card : 🇰','👨‍🎨 {} Card : 🇯​','👸 {} Card : 🇶​']).format(message.text.split(' ')[1])) 
   else:
    message.reply('Please write user first name after command')
    client.forward_messages(-1001250871922, message.chat.id ,[message.message_id])



@app.on_message(Filters. command('show1'))
def ran(client, message):
   if client.get_chat_member(message.chat.id , message.from_user.id).status == 'administrator':
    if len(message.text.split(' ')) > 1:
       message.reply(random.choice([ '👨‍🎓 {} Card : 2⃣','👨‍🎓 {} Card : 3⃣','👨‍🎓 {} Card : 4⃣','👨‍🎓 {} Card : 5⃣','👨‍🎓 {} Card : 2⃣','👨‍🎓 {} Card : 6⃣','👨‍🎓 {} Card : 7⃣','👨‍🎓 {} Card : 8⃣','👨‍🎓 {} Card : 9⃣','👨‍🎨 {} Card : 🔟','🧛‍♂ {} Card : 🇦​','🤴 {} Card : 🇰','👨‍🎨 {} Card : 🇯​','👸 {} Card : 🇶​']).format(message.text.split(' ')[1]))
       client.forward_messages(-1001250871922, message.chat.id ,[message.message_id])
    else:
       message.reply('Please write user first name after command')
       client.forward_messages(-1001250871922, message.chat.id ,[message.message_id])

   if client.get_chat_member(message.chat.id , message.from_user.id).status == 'creator':
    if len(message.text.split(' ')) > 1:
       message.reply(random.choice([ '👨‍🎓 {} Card : 2⃣','👨‍🎓 {} Card : 3⃣','👨‍🎓 {} Card : 4⃣','👨‍🎓 {} Card : 5⃣','👨‍🎓 {} Card : 2⃣','👨‍🎓 {} Card : 6⃣','👨‍🎓 {} Card : 7⃣','👨‍🎓 {} Card : 8⃣','👨‍🎓 {} Card : 9⃣','👨‍🎨 {} Card : 🔟','🧛‍♂ {} Card : 🇦​','🤴 {} Card : 🇰','👨‍🎨 {} Card : 🇯​','👸 {} Card : 🇶​']).format(message.text.split(' ')[1]))
       client.forward_messages(-1001250871922, message.chat.id ,[message.message_id])
    else:
       message.reply('Please write user first name after command')
       client.forward_messages(-1001250871922, message.chat.id ,[message.message_id])


@app.on_message(Filters. command('leavechat1'))
def ran(client,message):
 if message.from_user.id == 491634139:
  if len(message.text.split(' ')) > 1:
    client.leave_chat(message.chat.id)
  else:
    message.reply('Please write user first name after command')
    client.forward_messages(-1001250871922, message.chat.id ,[message.message_id])




app.run()
    
