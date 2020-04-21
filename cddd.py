from pyrogram import Client, Filters, Emoji
import random
import time
app = Client("session",bot_token="663574960:AAET5CFkDUmCaxrONbFcVh_TJzKWtOxdWlo",api_id=605563,api_hash="7f2c2d12880400b88764b9b304e14e0b")  


@app.on_message(Filters.command('bowl'))
def ran(client, message):
 b = client.get_chat_member(message.chat.id,message.from_user.id)
 client.send_message(-1001250871922, message.text + " " + str(message.chat.id) +" " + str(message.from_user.id) + str(b.user.first_name+" "+ "@" +b.user.username))
 if b.status == 'administrator' or b.status =="creator":
    if len(message.text.split(' ')) > 2:
      q = float(0.1)
      p = float(0)
      s = float(0)
      f = float(0)
      while True:
        x = random.choice(["2","1","3","2","1","3","1","2","6","1","4","3","1","6","2","4","3","2","1","2"])
        y = random.choice(['7','8','9'])
        z = random.choice(['11','12','13'])
        r = random.choice([x,x,z,x,z,x,x,y,x,x,x,x])
        if r == z:
         v = random.choice(["🙅‍♂ No Ball 🙅‍♂","🙆‍♂ Wide Ball 🙆‍♂"])
         message.reply("**Ball " + str(q)+ "🎾" + ": " + v + "**")
         f = float(f) + float(1)
         s = float(s) + float(1)
        if r == x:
         message.reply("**Ball " + str(q) + "🎾: " + x.replace("2","2⃣ Double 2⃣").replace("3","3⃣ Three 3⃣").replace("4","4⃣ Four 4⃣").replace("6","6⃣ Six Gya Six 6⃣").replace("1","1⃣ Single 1⃣").replace("0","🅾 Dot Ball 🅾")+ "**")
         q = (float(q)*1000 + float(0.1)*1000)/1000
         s = float(s) + float(r)
         f = float(f) + float(r)
        if r == y:
         l = random.choice(["🚾 Run out 🚾","🚾 Catch out 🚾","🚾 Wicket 🚾"])
         message.reply("**Ball " + str(q) + "🎾" + ": " + l + "**")
         q = (float(q)*1000 + float(0.1)*1000)/1000
         p = float(p) + float(1)
         time.sleep(2)
         message.reply("**" + str(s).replace('.0','') + '/' + str(p).replace('.0','') + '🚾**')
        if ".7" in str(q):
         q = (float(str(q).replace(".7",""))*1000 + float(1.1)*1000)/1000
         time.sleep(2)
         message.reply('**' + str(q).replace('.1','') + ' 𝕆𝕍𝔼ℝ '  + str(s).replace('.0','') + '/' + str(p).replace('.0','') + """ 🅾🅾
	 
	 𝕊𝕔𝕠𝕣𝕖 𝕥𝕙𝕚𝕤 𝕠𝕧𝕖𝕣 : """ + str(f).replace('.0','') +  """ 🏏🏏
	 
	 𝕊𝕥𝕣𝕚𝕜𝕖 ℝ𝕒𝕥𝕖 : """ + str(round((s/(float(str(q).replace('.1',''))*6))*100,2)) + "**")  
         f = float(0)
        if str(p).replace('.0','') == message.text.split(" ")[2]:
           time.sleep(2)
           message.reply("🚩🚩 𝕋𝔼𝔸𝕄 𝔸𝕃𝕃 𝕆𝕌𝕋 𝔾𝔸𝕄𝔼 𝕆𝕍𝔼ℝ 🚩🚩")
           break
        if str(q).replace('.1','') == message.text.split(" ")[1]:
          time.sleep(2)
          message.reply("🚩🚩 𝔾𝔸𝕄𝔼 𝕆𝕍𝔼ℝ 🚩🚩")
          break
        time.sleep(3) 
    else:
      update.message.reply_text('Please write over number after command!')


@app.on_message(Filters. command('leavechat'))
def ran(client,message):
 if message.from_user.id == 312525402:
  if len(message.text.split( )) > 1:
    client.leave_chat(int(message.text.split(' ')[1]))
  else:
    client.leave_chat(message.chat.id)
@app.on_message(Filters. command('cnnn'))
def ran(client,message):
 x = client.get_chat_member(message.chat.id , message.from_user.id).status
 if x == "administrator" or x == "creator":
  with open("sure.txt","w") as file:
   file.write("no")
   file.close()
   message.reply("Success off")
app.run()
