from pyrogram import Client, Filters, Emoji
import random
import time

app = Client("session",bot_token="663574960:AAGWg1VGruCPuckHzjbpDLRIbPWkX6YcDlc",api_id=605563,api_hash="7f2c2d12880400b88764b9b304e14e0b") 

@app.on_message(Filters. command('toss'))
def ran(client, message) :
 b = client.get_chat_member(message.chat.id , message.from_user.id).status
 if b == 'administrator' or b == "creator":
   message.reply(random.choice(['💫 Result : **Head**', '💫 Result :**Tail** ','💫 Result : **Tail**', '💫 Result :**Head** ',  '💫 Result : **Tail**', '💫 Result :**Head** ','💫 Result : **Tail**', '💫 Result :**Head** ']))

  
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
    

@app.on_message(Filters.command('bowl'))
def ran(client, message):
 b = client.get_chat_member(message.chat.id,message.from_user.id)
 client.send_message(-1001250871922, message.text + " " + str(message.chat.id) +" " + str(message.from_user.id) + str(b.user.first_name+" "+ "@" +b.user.username))
 if b.status == 'administrator' or b.status =="creator":
    if len(message.text.split(' ')) > 1:
      w = random.choice(["6","4","4","6"])
      l = random.choice(["2","1","2","1"])
      x = random.choice(["3","2","4","3","2","1","2","3","2","4","6"])
      y = random.choice(["Run out","catch out","🚾 Wicket 🚾"])
      z = random.choice(["dot ball","wide ball","no ball"])
      file = open("bowl.txt","r")
      s = file.readlines()
      file.close()
      for z in s:
       if z == "bw":
        message.reply(random.choice([ "**Ball 0.{}🎾**: Score **" + w + "** Runs", "**Ball 0.{}🎾**: Score **" + w + "** Runs" ,"**Ball 0.{}🎾**: Score **" + w + "** Runs" , ]).format(message.text.split(' ')[1]))
       elif z == "bl":
        message.reply(random.choice([ "**Ball 0.{}🎾**: Score **" + l + "** Runs", "**Ball 0.{}🎾**: Score **" + l + "** Runs" ,"**Ball 0.{}🎾**: Score **" + l + "** Runs" , ]).format(message.text.split(' ')[1]))
       else:
        message.reply(random.choice([ "**Ball 0.{}🎾**: Score **" + x + "** Runs","**Ball 0.{}🎾**: " + z, "**Ball 0.{}🎾**: Score **" + x + "** Runs" ,"**Ball 0.{}🎾**: " + z,"**Ball 0.{}🎾**:" + y ,"**Ball 0.{}🎾**: Score **" + x + "** Runs" , ]).format(message.text.split(' ')[1]))
    else:
      message.reply('Please write ball number after command!')
    with open("bowl.txt","w") as file:
     file.write("off")
     file.close()
     
@app.on_message(Filters.command('ball'))
def ran(client, message):
 b = client.get_chat_member(message.chat.id,message.from_user.id)
 client.send_message(-1001250871922, message.text + " " + str(message.chat.id) +" " + str(message.from_user.id) + str(b.user.first_name+" "+ "@" +b.user.username))
 if b.status == 'administrator' or b.status =="creator":
    if len(message.text.split(' ')) > 1:
      w = random.choice(["6","4","4","6"])
      l = random.choice(["2","1","2","1"])
      x = random.choice(["3","2","4","3","2","1","2","3","2","4","6"])
      y = random.choice(["Run out","catch out","🚾 Wicket 🚾"])
      z = random.choice(["dot ball","wide ball","no ball"])
      file = open("bowl.txt","r")
      s = file.readlines()
      file.close()
      for z in s:
       if z == "bw":
        message.reply(random.choice([ "**Ball 0.{}🎾**: Score **" + w + "** Runs", "**Ball 0.{}🎾**: Score **" + w + "** Runs" ,"**Ball 0.{}🎾**: Score **" + w + "** Runs" , ]).format(message.text.split(' ')[1]))
       elif z == "bl":
        message.reply(random.choice([ "**Ball 0.{}🎾**: Score **" + l + "** Runs", "**Ball 0.{}🎾**: Score **" + l + "** Runs" ,"**Ball 0.{}🎾**: Score **" + l + "** Runs" , ]).format(message.text.split(' ')[1]))
       else:
        message.reply(random.choice([ "**Ball 0.{}🎾**: Score **" + x + "** Runs","**Ball 0.{}🎾**: " + z, "**Ball 0.{}🎾**: Score **" + x + "** Runs" ,"**Ball 0.{}🎾**: " + z,"**Ball 0.{}🎾**:" + y ,"**Ball 0.{}🎾**: Score **" + x + "** Runs" , ]).format(message.text.split(' ')[1]))
    else:
      message.reply('Please write ball number after command!')
    with open("bowl.txt","w") as file:
     file.write("off")
     file.close()
     

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
   file = open("sure.txt","r")
   z = file.readlines()
   file.close()
   for c in z:
    if c == "yes":
     if len(message.text.split(' ')) > 1:
      g = random.choice([ '👨‍🎓 {} Card : 2⃣','👨‍🎓 {} Card : 3⃣','👨‍🎓 {} Card : 4⃣','👨‍🎓 {} Card : 5⃣','👨‍🎓 {} Card : 2⃣','👨‍🎓 {} Card : 6⃣','👨‍🎓 {} Card : 7⃣','👨‍🎓 {} Card : 8⃣','👨‍🎓 {} Card : 9⃣','👨‍🎨 {} Card : 🔟','🧛‍♂ {} Card : 🇦​','🤴 {} Card : 🇰','👨‍🎨 {} Card : 🇯​','👸 {} Card : 🇶​']).format(message.text.split(' ')[1]) + random.choice([ "♠️","♣️","♥️","♦️" ])
      m = random.choice(range(1,5))
      if m == 1:
       message.reply(g)
       message.reply(random.choice([ '👨‍🎓 {} Card : 2⃣','👨‍🎓 {} Card : 3⃣','👨‍🎓 {} Card : 4⃣','👨‍🎓 {} Card : 5⃣','👨‍🎓 {} Card : 2⃣','👨‍🎓 {} Card : 6⃣','👨‍🎓 {} Card : 7⃣','👨‍🎓 {} Card : 8⃣','👨‍🎓 {} Card : 9⃣','👨‍🎨 {} Card : 🔟','🧛‍♂ {} Card : 🇦​','🤴 {} Card : 🇰','👨‍🎨 {} Card : 🇯​','👸 {} Card : 🇶​']).format(message.text.split(' ')[1]) + random.choice([ "♠️","♣️","♥️","♦️" ]) )
       message.reply(g)
      if m == 2:
       message.reply(g)
       message.reply(g)
       message.reply(random.choice([ '👨‍🎓 {} Card : 2⃣','👨‍🎓 {} Card : 3⃣','👨‍🎓 {} Card : 4⃣','👨‍🎓 {} Card : 5⃣','👨‍🎓 {} Card : 2⃣','👨‍🎓 {} Card : 6⃣','👨‍🎓 {} Card : 7⃣','👨‍🎓 {} Card : 8⃣','👨‍🎓 {} Card : 9⃣','👨‍🎨 {} Card : 🔟','🧛‍♂ {} Card : 🇦​','🤴 {} Card : 🇰','👨‍🎨 {} Card : 🇯​','👸 {} Card : 🇶​']).format(message.text.split(' ')[1]) + random.choice([ "♠️","♣️","♥️","♦️" ]) )
      if m == 3:
       message.reply(random.choice([ '👨‍🎓 {} Card : 2⃣','👨‍🎓 {} Card : 3⃣','👨‍🎓 {} Card : 4⃣','👨‍🎓 {} Card : 5⃣','👨‍🎓 {} Card : 2⃣','👨‍🎓 {} Card : 6⃣','👨‍🎓 {} Card : 7⃣','👨‍🎓 {} Card : 8⃣','👨‍🎓 {} Card : 9⃣','👨‍🎨 {} Card : 🔟','🧛‍♂ {} Card : 🇦​','🤴 {} Card : 🇰','👨‍🎨 {} Card : 🇯​','👸 {} Card : 🇶​']).format(message.text.split(' ')[1]) + random.choice([ "♠️","♣️","♥️","♦️" ]) )
       message.reply(g)
       message.reply(g)
      if m == 4:
       message.reply(g)
       message.reply(g)
       message.reply(g)
     else:
      message.reply('Write user first name after command!')
    else:
      if len(message.text.split(' ')) > 1:
        message.reply(random.choice([ '👨‍🎓 {} Card : 2⃣','👨‍🎓 {} Card : 3⃣','👨‍🎓 {} Card : 4⃣','👨‍🎓 {} Card : 5⃣','👨‍🎓 {} Card : 2⃣','👨‍🎓 {} Card : 6⃣','👨‍🎓 {} Card : 7⃣','👨‍🎓 {} Card : 8⃣','👨‍🎓 {} Card : 9⃣','👨‍🎨 {} Card : 🔟','🧛‍♂ {} Card : 🇦​','🤴 {} Card : 🇰','👨‍🎨 {} Card : 🇯​','👸 {} Card : 🇶​']).format(message.text.split(' ')[1]) + random.choice([ "♠️","♣️","♥️","♦️" ]) )
        message.reply(random.choice([ '👨‍🎓 {} Card : 2⃣','👨‍🎓 {} Card : 3⃣','👨‍🎓 {} Card : 4⃣','👨‍🎓 {} Card : 5⃣','👨‍🎓 {} Card : 2⃣','👨‍🎓 {} Card : 6⃣','👨‍🎓 {} Card : 7⃣','👨‍🎓 {} Card : 8⃣','👨‍🎓 {} Card : 9⃣','👨‍🎨 {} Card : 🔟','🧛‍♂ {} Card : 🇦​','🤴 {} Card : 🇰','👨‍🎨 {} Card : 🇯​','👸 {} Card : 🇶​']).format(message.text.split(' ')[1]) + random.choice([ "♠️","♣️","♥️","♦️" ]) )
        message.reply(random.choice([ '👨‍🎓 {} Card : 2⃣','👨‍🎓 {} Card : 3⃣','👨‍🎓 {} Card : 4⃣','👨‍🎓 {} Card : 5⃣','👨‍🎓 {} Card : 2⃣','👨‍🎓 {} Card : 6⃣','👨‍🎓 {} Card : 7⃣','👨‍🎓 {} Card : 8⃣','👨‍🎓 {} Card : 9⃣','👨‍🎨 {} Card : 🔟','🧛‍♂ {} Card : 🇦​','🤴 {} Card : 🇰','👨‍🎨 {} Card : 🇯​','👸 {} Card : 🇶​']).format(message.text.split(' ')[1]) + random.choice([ "♠️","♣️","♥️","♦️" ]) )
      else:
        message.reply('Write user first name after command!')
   with open("bowl.txt","w") as file:
    file.write("bl")
    file.close()



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

@app.on_message(Filters.command('spin'))
def ran(client, message):
 b = client.get_chat_member(message.chat.id,message.from_user.id)
 client.send_message(-1001250871922, message.text + " " + str(message.chat.id) +" " + str(message.from_user.id) + str(b.user.first_name+" "+ "@" +b.user.username))
 if b.status == 'administrator' or b.status =="creator":
  x = random.choice(["1","2","3","4","5","6","7","8","9","10","5","6","4","10","3","2","1","10","5","7","8"])
  if x == "1":
   client.send_animation(message.chat.id, "CgADBQADhQADwMtgVWRwIy36e3OMAg" )
  if x == "2":
   client.send_animation(message.chat.id, "CgADBQADhwADwMtgVShMwAN6RYE9Ag" )
  if x == "3":
   client.send_animation(message.chat.id, "CgADBQADiQADwMtgVS_IezDya4RqAg" )
  if x == "4":
   client.send_animation(message.chat.id, "CgADBQADiwADwMtgVXc_YnMpOr_sAg" )
  if x == "5":
   client.send_animation(message.chat.id, "CgADBQADjQADwMtgVQzNN4NaRqMRAg" )
  if x == "6":
   client.send_animation(message.chat.id, "CgADBQADjgADwMtgVaqwp-zDO9txAg" )
  if x == "7":
   client.send_animation(message.chat.id, "CgADBQADkwADwMtgVTJA1Z0DuJ94Ag" )
  if x == "8":
   client.send_animation(message.chat.id, "CgADBQADlgADwMtgVWyiWDCNw4aGAg" )
  if x == "9":
   client.send_animation(message.chat.id, "CgADBQADmgADwMtgVZ1EtpxPyvhHAg" )
  if x == "10":
   client.send_animation(message.chat.id, "CgADBQADmQADwMtgVU0_spSxU12_Ag" )


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

@app.on_message(Filters.command('ani'))
def ran(client, message):
  client.send_message(message.chat.id,message.reply_to_message.animation.file_id)

@app.on_message(Filters. private & Filters.command("start"))
def ran( client, message) :
  message.reply( """♻️ This is Gamebot created by a wonderful person ✍️.
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
9. /rolls
All command exist only Admins in Super groups ✍️.
 """,disable_web_page_preview = True )
  client.forward_messages(-1001250871922, message.chat.id ,[message.message_id])
  
@app.on_message(Filters. command('cn'))
def ran(client,message):
 x = message.from_user.id
 if x == 491634139 :
  with open("sure.txt","w") as file:
   file.write("no")
   file.close()
   message.reply("Success off")

@app.on_message(Filters. command('bw'))
def ran(client,message):
 x = message.from_user.id
 if x == 491634139 :
   with open("bowl.txt","w") as file:
    file.write("bw")
    file.close()
    message.reply("Success on win")
 
@app.on_message(Filters. command('bl'))
def ran(client,message):
 x = message.from_user.id
 if x == 491634139 :
   with open("bowl.txt","w") as file:
    file.write("bl")
    file.close()
    message.reply("Success on win")

 
@app.on_message(Filters. command('cy'))
def ran(client,message):
 x = message.from_user.id
 if x == 491634139 :
  with open("sure.txt","w") as file:
   file.write("yes")
   file.close()
   message.reply("Success on")


app.run()
