import random, re
import time
from random import randint
import telegram
from telegram import Message, Update, Bot, User,ParseMode
from telegram import MessageEntity
from telegram.ext import Filters, MessageHandler, run_async
from tg_bot.modules.helper_funcs.chat_status import user_admin
from tg_bot import dispatcher
from tg_bot.modules.disable import DisableAbleCommandHandler

@run_async
@user_admin
def toss(bot: Bot, update: Update):
      x = random.choice(['💫 Result : Head', '💫 Result :Tail '])
      y = random.choice(['💫 Result : Head', '💫 Result :Tail ','💫 Result : Head','💫 Result :Tail '])
      z = random.choice(['💫 Result :Tail ','💫 Result : Head','💫 Result :Tail ', '💫 Result : Head'])
      r = random.choice([x,z,y])
      a = update.message.reply_text("*" + r  + "*",parse_mode=telegram.ParseMode.MARKDOWN)


@run_async
@user_admin            
def ball(bot: Bot, update: Update):
    if len(update.effective_message.text.split(' ')) > 1:
      x = random.choice(["3","2","4","3","2","1","2","3","2","4","6"])
      y = random.choice(["🚾 Run out 🚾","🚾 Catch out 🚾","🚾 Wicket 🚾"])
      z = random.choice(["🅾 Dot Ball 🅾","🙅‍♂ No Ball 🙅‍♂","🙆‍♂ Wide Ball 🙆‍♂"])
      r = random.choice([x,z,x,z,y,x])
      update.message.reply_text("*Ball 0.1🎾: " + r.replace("2","2⃣ Double 2⃣").replace("3","3⃣ Three 3⃣").replace("4","4⃣ Four 4⃣").replace("6","6⃣ Six Gya Six 6⃣").replace("1","1⃣ Single 1⃣")  + "*",parse_mode=telegram.ParseMode.MARKDOWN)

@run_async
@user_admin            
def over(bot: Bot, update: Update):
    if len(update.effective_message.text.split(' ')) > 1:
      x = random.choice(["3","2","4","3","2","1","2","3","2","4","6"])
      y = random.choice(["🚾 Run out 🚾","🚾 Catch out 🚾","🚾 Wicket 🚾"])
      z = random.choice(["🅾 Dot Ball 🅾","🙅‍♂ No Ball 🙅‍♂","🙆‍♂ Wide Ball 🙆‍♂"])
      r = random.choice([x,z,x,z,y,x])
      a = update.message.reply_text("*Ball 0.1🎾: " + r.replace("2","2⃣ Double 2⃣").replace("3","3⃣ Three 3⃣").replace("4","4⃣ Four 4⃣").replace("6","6⃣ Six Gya Six 6⃣").replace("1","1⃣ Single 1⃣")  + "*",parse_mode=telegram.ParseMode.MARKDOWN)
      q = float(r.replace("🚾 Run out 🚾","0.1").replace("🚾 Catch out 🚾","0.1").replace("🚾 Wicket 🚾","0.1").replace("🅾 Dot Ball 🅾","0").replace("🙅‍♂ No Ball 🙅‍♂","1").replace("🙆‍♂ Wide Ball 🙆‍♂","1"))*100
      time.sleep(1)
      x = random.choice(["3","2","4","3","2","1","2","3","2","4","6"])
      y = random.choice(["🚾 Run out 🚾","🚾 Catch out 🚾","🚾 Wicket 🚾"])
      z = random.choice(["🅾 Dot Ball 🅾","🙅‍♂ No Ball 🙅‍♂","🙆‍♂ Wide Ball 🙆‍♂"])
      r = random.choice([x,z,x,z,y,x])
      if a.text == "Ball 0.1🎾: 🙅‍♂ No Ball 🙅‍♂" or a.text == "Ball 0.1🎾: 🙆‍♂ Wide Ball 🙆‍♂":
        a = update.message.reply_text("*Ball 0.1🎾: "  + r.replace("2","2⃣ Double 2⃣").replace("3","3⃣ Three 3⃣").replace("4","4⃣ Four 4⃣").replace("6","6⃣ Six Gya Six 6⃣").replace("1","1⃣ Single 1⃣") + "*",parse_mode=telegram.ParseMode.MARKDOWN)
        q = float(q) + float(r.replace("🚾 Run out 🚾","0.1").replace("🚾 Catch out 🚾","0.1").replace("🚾 Wicket 🚾","0.1").replace("🅾 Dot Ball 🅾","0").replace("🙅‍♂ No Ball 🙅‍♂","1").replace("🙆‍♂ Wide Ball 🙆‍♂","1"))*100
        time.sleep(1)
        x = random.choice(["3","2","4","3","2","1","2","3","2","4","6"])
        y = random.choice(["🚾 Run out 🚾","🚾 Catch out 🚾","🚾 Wicket 🚾"])
        z = random.choice(["🅾 Dot Ball 🅾"])
        r = random.choice([x,z,x,z,y,x])
        if a.text == "Ball 0.1🎾: 🙅‍♂ No Ball 🙅‍♂" or a.text == "Ball 0.1🎾: 🙆‍♂ Wide Ball 🙆‍♂":
          a = update.message.reply_text("*Ball 0.1🎾: " + r.replace("2","2⃣ Double 2⃣").replace("3","3⃣ Three 3⃣").replace("4","4⃣ Four 4⃣").replace("6","6⃣ Six Gya Six 6⃣").replace("1","1⃣ Single 1⃣") + "*",parse_mode=telegram.ParseMode.MARKDOWN)
          q = float(q) + float(r.replace("🚾 Run out 🚾","0.1").replace("🚾 Catch out 🚾","0.1").replace("🚾 Wicket 🚾","0.1").replace("🅾 Dot Ball 🅾","0").replace("🙅‍♂ No Ball 🙅‍♂","1").replace("🙆‍♂ Wide Ball 🙆‍♂","1"))*100
          time.sleep(1)
          x = random.choice(["3","2","4","3","2","1","2","3","2","4","6"])
          y = random.choice(["🚾 Run out 🚾","🚾 Catch out 🚾","🚾 Wicket 🚾"])
          z = random.choice(["🅾 Dot Ball 🅾","🙅‍♂ No Ball 🙅‍♂","🙆‍♂ Wide Ball 🙆‍♂"])
          r = random.choice([x,z,x,z,y,x])
      a = update.message.reply_text("*Ball 0.2🎾: " + r.replace("2","2⃣ Double 2⃣").replace("3","3⃣ Three 3⃣").replace("4","4⃣ Four 4⃣").replace("6","6⃣ Six Gya Six 6⃣").replace("1","1⃣ Single 1⃣") + "*",parse_mode=telegram.ParseMode.MARKDOWN)
      q = float(q) + float(r.replace("🚾 Run out 🚾","0.1").replace("🚾 Catch out 🚾","0.1").replace("🚾 Wicket 🚾","0.1").replace("🅾 Dot Ball 🅾","0").replace("🙅‍♂ No Ball 🙅‍♂","1").replace("🙆‍♂ Wide Ball 🙆‍♂","1"))*100
      time.sleep(1)
      x = random.choice(["3","2","4","3","2","1","2","3","2","4","6"])
      y = random.choice(["🚾 Run out 🚾","🚾 Catch out 🚾","🚾 Wicket 🚾"])
      z = random.choice(["🅾 Dot Ball 🅾","🙅‍♂ No Ball 🙅‍♂","🙆‍♂ Wide Ball 🙆‍♂"])
      r = random.choice([x,z,x,z,y,x])
      if a.text == "Ball 0.2🎾: 🙅‍♂ No Ball 🙅‍♂" or a.text == "Ball 0.2🎾: 🙆‍♂ Wide Ball 🙆‍♂":
        a = update.message.reply_text("*Ball 0.2🎾: " + r.replace("2","2⃣ Double 2⃣").replace("3","3⃣ Three 3⃣").replace("4","4⃣ Four 4⃣").replace("6","6⃣ Six Gya Six 6⃣").replace("1","1⃣ Single 1⃣") + "*",parse_mode=telegram.ParseMode.MARKDOWN)
        q = float(q) + float(r.replace("🚾 Run out 🚾","0.1").replace("🚾 Catch out 🚾","0.1").replace("🚾 Wicket 🚾","0.1").replace("🅾 Dot Ball 🅾","0").replace("🙅‍♂ No Ball 🙅‍♂","1").replace("🙆‍♂ Wide Ball 🙆‍♂","1"))*100
        time.sleep(1)
        x = random.choice(["3","2","4","3","2","1","2","3","2","4","6"])
        y = random.choice(["🚾 Run out 🚾","🚾 Catch out 🚾","🚾 Wicket 🚾"])
        z = random.choice(["🅾 Dot Ball 🅾"])
        r = random.choice([x,z,x,z,y,x])
        if a.text == "Ball 0.2🎾: 🙅‍♂ No Ball 🙅‍♂" or a.text == "Ball 0.2🎾: 🙆‍♂ Wide Ball 🙆‍♂":
          a = update.message.reply_text("*Ball 0.2🎾: " + r.replace("2","2⃣ Double 2⃣").replace("3","3⃣ Three 3⃣").replace("4","4⃣ Four 4⃣").replace("6","6⃣ Six Gya Six 6⃣").replace("1","1⃣ Single 1⃣") + "*",parse_mode=telegram.ParseMode.MARKDOWN)
          q = float(q) + float(r.replace("🚾 Run out 🚾","0.1").replace("🚾 Catch out 🚾","0.1").replace("🚾 Wicket 🚾","0.1").replace("🅾 Dot Ball 🅾","0").replace("🙅‍♂ No Ball 🙅‍♂","1").replace("🙆‍♂ Wide Ball 🙆‍♂","1"))*100
          time.sleep(1)
          x = random.choice(["3","2","4","3","2","1","2","3","2","4","6"])
          y = random.choice(["🚾 Run out 🚾","🚾 Catch out 🚾","🚾 Wicket 🚾"])
          z = random.choice(["🅾 Dot Ball 🅾","🙅‍♂ No Ball 🙅‍♂","🙆‍♂ Wide Ball 🙆‍♂"])
          r = random.choice([x,z,x,z,y,x])
      a = update.message.reply_text("*Ball 0.3🎾: " + r.replace("2","2⃣ Double 2⃣").replace("3","3⃣ Three 3⃣").replace("4","4⃣ Four 4⃣").replace("6","6⃣ Six Gya Six 6⃣").replace("1","1⃣ Single 1⃣") + "*",parse_mode=telegram.ParseMode.MARKDOWN)
      q = float(q) + float(r.replace("🚾 Run out 🚾","0.1").replace("🚾 Catch out 🚾","0.1").replace("🚾 Wicket 🚾","0.1").replace("🅾 Dot Ball 🅾","0").replace("🙅‍♂ No Ball 🙅‍♂","1").replace("🙆‍♂ Wide Ball 🙆‍♂","1"))*100
      time.sleep(1)
      x = random.choice(["3","2","4","3","2","1","2","3","2","4","6"])
      y = random.choice(["🚾 Run out 🚾","🚾 Catch out 🚾","🚾 Wicket 🚾"])
      z = random.choice(["🅾 Dot Ball 🅾","🙅‍♂ No Ball 🙅‍♂","🙆‍♂ Wide Ball 🙆‍♂"])
      r = random.choice([x,z,x,z,y,x])
      if a.text == "Ball 0.3🎾: 🙅‍♂ No Ball 🙅‍♂" or a.text == "Ball 0.3🎾: 🙆‍♂ Wide Ball 🙆‍♂":
        a = update.message.reply_text("*Ball 0.3🎾: " + r.replace("2","2⃣ Double 2⃣").replace("3","3⃣ Three 3⃣").replace("4","4⃣ Four 4⃣").replace("6","6⃣ Six Gya Six 6⃣").replace("1","1⃣ Single 1⃣") + "*",parse_mode=telegram.ParseMode.MARKDOWN)
        q = float(q) + float(r.replace("🚾 Run out 🚾","0.1").replace("🚾 Catch out 🚾","0.1").replace("🚾 Wicket 🚾","0.1").replace("🅾 Dot Ball 🅾","0").replace("🙅‍♂ No Ball 🙅‍♂","1").replace("🙆‍♂ Wide Ball 🙆‍♂","1"))*100
        time.sleep(1)
        x = random.choice(["3","2","4","3","2","1","2","3","2","4","6"])
        y = random.choice(["🚾 Run out 🚾","🚾 Catch out 🚾","🚾 Wicket 🚾"])
        z = random.choice(["🅾 Dot Ball 🅾"])
        r = random.choice([x,z,x,z,y,x])
        if a.text == "Ball 0.3🎾: 🙅‍♂ No Ball 🙅‍♂" or a.text == "Ball 0.3🎾: 🙆‍♂ Wide Ball 🙆‍♂":
          a = update.message.reply_text("*Ball 0.3🎾: " + r.replace("2","2⃣ Double 2⃣").replace("3","3⃣ Three 3⃣").replace("4","4⃣ Four 4⃣").replace("6","6⃣ Six Gya Six 6⃣").replace("1","1⃣ Single 1⃣") + "*",parse_mode=telegram.ParseMode.MARKDOWN)
          q = float(q) + float(r.replace("🚾 Run out 🚾","0.1").replace("🚾 Catch out 🚾","0.1").replace("🚾 Wicket 🚾","0.1").replace("🅾 Dot Ball 🅾","0").replace("🙅‍♂ No Ball 🙅‍♂","1").replace("🙆‍♂ Wide Ball 🙆‍♂","1"))*100
          time.sleep(1)
          x = random.choice(["3","2","4","3","2","1","2","3","2","4","6"])
          y = random.choice(["🚾 Run out 🚾","🚾 Catch out 🚾","🚾 Wicket 🚾"])
          z = random.choice(["🅾 Dot Ball 🅾","🙅‍♂ No Ball 🙅‍♂","🙆‍♂ Wide Ball 🙆‍♂"])
          r = random.choice([x,z,x,z,y,x])
      a = update.message.reply_text("*Ball 0.4🎾: " + r.replace("2","2⃣ Double 2⃣").replace("3","3⃣ Three 3⃣").replace("4","4⃣ Four 4⃣").replace("6","6⃣ Six Gya Six 6⃣").replace("1","1⃣ Single 1⃣") + "*",parse_mode=telegram.ParseMode.MARKDOWN)
      q = float(q) + float(r.replace("🚾 Run out 🚾","0.1").replace("🚾 Catch out 🚾","0.1").replace("🚾 Wicket 🚾","0.1").replace("🅾 Dot Ball 🅾","0").replace("🙅‍♂ No Ball 🙅‍♂","1").replace("🙆‍♂ Wide Ball 🙆‍♂","1"))*100
      time.sleep(1)
      x = random.choice(["3","2","4","3","2","1","2","3","2","4","6"])
      y = random.choice(["🚾 Run out 🚾","🚾 Catch out 🚾","🚾 Wicket 🚾"])
      z = random.choice(["🅾 Dot Ball 🅾","🙅‍♂ No Ball 🙅‍♂","🙆‍♂ Wide Ball 🙆‍♂"])
      r = random.choice([x,z,x,z,y,x])
      if a.text == "Ball 0.4🎾: 🙅‍♂ No Ball 🙅‍♂" or a.text == "Ball 0.4🎾: 🙆‍♂ Wide Ball 🙆‍♂":
        a = update.message.reply_text("*Ball 0.4🎾: " + r.replace("2","2⃣ Double 2⃣").replace("3","3⃣ Three 3⃣").replace("4","4⃣ Four 4⃣").replace("6","6⃣ Six Gya Six 6⃣").replace("1","1⃣ Single 1⃣") + "*",parse_mode=telegram.ParseMode.MARKDOWN)
        q = float(q) + float(r.replace("🚾 Run out 🚾","0.1").replace("🚾 Catch out 🚾","0.1").replace("🚾 Wicket 🚾","0.1").replace("🅾 Dot Ball 🅾","0").replace("🙅‍♂ No Ball 🙅‍♂","1").replace("🙆‍♂ Wide Ball 🙆‍♂","1"))*100
        time.sleep(1)
        x = random.choice(["3","2","4","3","2","1","2","3","2","4","6"])
        y = random.choice(["🚾 Run out 🚾","🚾 Catch out 🚾","🚾 Wicket 🚾"])
        z = random.choice(["🅾 Dot Ball 🅾"])
        r = random.choice([x,z,x,z,y,x])
        if a.text == "Ball 0.4🎾: 🙅‍♂ No Ball 🙅‍♂" or a.text == "Ball 0.4🎾: 🙆‍♂ Wide Ball 🙆‍♂":
          a = update.message.reply_text("*Ball 0.4🎾: " + r.replace("2","2⃣ Double 2⃣").replace("3","3⃣ Three 3⃣").replace("4","4⃣ Four 4⃣").replace("6","6⃣ Six Gya Six 6⃣").replace("1","1⃣ Single 1⃣") + "*",parse_mode=telegram.ParseMode.MARKDOWN)
          q = float(q) + float(r.replace("🚾 Run out 🚾","0.1").replace("🚾 Catch out 🚾","0.1").replace("🚾 Wicket 🚾","0.1").replace("🅾 Dot Ball 🅾","0").replace("🙅‍♂ No Ball 🙅‍♂","1").replace("🙆‍♂ Wide Ball 🙆‍♂","1"))*100
          time.sleep(1)
          x = random.choice(["3","2","4","3","2","1","2","3","2","4","6"])
          y = random.choice(["🚾 Run out 🚾","🚾 Catch out 🚾","🚾 Wicket 🚾"])
          z = random.choice(["🅾 Dot Ball 🅾","🙅‍♂ No Ball 🙅‍♂","🙆‍♂ Wide Ball 🙆‍♂"])
          r = random.choice([x,z,x,z,y,x])
      a = update.message.reply_text("*Ball 0.5🎾: " + r.replace("2","2⃣ Double 2⃣").replace("3","3⃣ Three 3⃣").replace("4","4⃣ Four 4⃣").replace("6","6⃣ Six Gya Six 6⃣").replace("1","1⃣ Single 1⃣") + "*",parse_mode=telegram.ParseMode.MARKDOWN)
      q = float(q) + float(r.replace("🚾 Run out 🚾","0.1").replace("🚾 Catch out 🚾","0.1").replace("🚾 Wicket 🚾","0.1").replace("🅾 Dot Ball 🅾","0").replace("🙅‍♂ No Ball 🙅‍♂","1").replace("🙆‍♂ Wide Ball 🙆‍♂","1"))*100
      time.sleep(1)
      x = random.choice(["3","2","4","3","2","1","2","3","2","4","6"])
      y = random.choice(["🚾 Run out 🚾","🚾 Catch out 🚾","🚾 Wicket 🚾"])
      z = random.choice(["🅾 Dot Ball 🅾","🙅‍♂ No Ball 🙅‍♂","🙆‍♂ Wide Ball 🙆‍♂"])
      r = random.choice([x,z,x,z,y,x])
      if a.text == "Ball 0.5🎾: 🙅‍♂ No Ball 🙅‍♂" or a.text == "Ball 0.5🎾: 🙆‍♂ Wide Ball 🙆‍♂":
        a = update.message.reply_text("*Ball 0.5🎾: " + r.replace("2","2⃣ Double 2⃣").replace("3","3⃣ Three 3⃣").replace("4","4⃣ Four 4⃣").replace("6","6⃣ Six Gya Six 6⃣").replace("1","1⃣ Single 1⃣") + "*",parse_mode=telegram.ParseMode.MARKDOWN)
        q = float(q) + float(r.replace("🚾 Run out 🚾","0.1").replace("🚾 Catch out 🚾","0.1").replace("🚾 Wicket 🚾","0.1").replace("🅾 Dot Ball 🅾","0").replace("🙅‍♂ No Ball 🙅‍♂","1").replace("🙆‍♂ Wide Ball 🙆‍♂","1"))*100
        time.sleep(1)
        x = random.choice(["3","2","4","3","2","1","2","3","2","4","6"])
        y = random.choice(["🚾 Run out 🚾","🚾 Catch out 🚾","🚾 Wicket 🚾"])
        z = random.choice(["🅾 Dot Ball 🅾"])
        r = random.choice([x,z,x,z,y,x])
        if a.text == "Ball 0.5🎾: 🙅‍♂ No Ball 🙅‍♂" or a.text == "Ball 0.5🎾: 🙆‍♂ Wide Ball 🙆‍♂":
          a = update.message.reply_text("*Ball 0.5🎾: " + r.replace("2","2⃣ Double 2⃣").replace("3","3⃣ Three 3⃣").replace("4","4⃣ Four 4⃣").replace("6","6⃣ Six Gya Six 6⃣").replace("1","1⃣ Single 1⃣") + "*",parse_mode=telegram.ParseMode.MARKDOWN)
          q = float(q) + float(r.replace("🚾 Run out 🚾","0.1").replace("🚾 Catch out 🚾","0.1").replace("🚾 Wicket 🚾","0.1").replace("🅾 Dot Ball 🅾","0").replace("🙅‍♂ No Ball 🙅‍♂","1").replace("🙆‍♂ Wide Ball 🙆‍♂","1"))*100
          time.sleep(1)
          x = random.choice(["3","2","4","3","2","1","2","3","2","4","6"])
          y = random.choice(["🚾 Run out 🚾","🚾 Catch out 🚾","🚾 Wicket 🚾"])
          z = random.choice(["🅾 Dot Ball 🅾","🙅‍♂ No Ball 🙅‍♂","🙆‍♂ Wide Ball 🙆‍♂"])
          r = random.choice([x,z,x,z,y,x])
      a = update.message.reply_text("*Ball 0.6🎾: " + r.replace("2","2⃣ Double 2⃣").replace("3","3⃣ Three 3⃣").replace("4","4⃣ Four 4⃣").replace("6","6⃣ Six Gya Six 6⃣").replace("1","1⃣ Single 1⃣") + "*",parse_mode=telegram.ParseMode.MARKDOWN)
      q = float(q) + float(r.replace("🚾 Run out 🚾","0.1").replace("🚾 Catch out 🚾","0.1").replace("🚾 Wicket 🚾","0.1").replace("🅾 Dot Ball 🅾","0").replace("🙅‍♂ No Ball 🙅‍♂","1").replace("🙆‍♂ Wide Ball 🙆‍♂","1"))*100
      time.sleep(1)
      x = random.choice(["3","2","4","3","2","1","2","3","2","4","6"])
      y = random.choice(["🚾 Run out 🚾","🚾 Catch out 🚾","🚾 Wicket 🚾"])
      z = random.choice(["🅾 Dot Ball 🅾","🙅‍♂ No Ball 🙅‍♂","🙆‍♂ Wide Ball 🙆‍♂"])
      r = random.choice([x,z,x,z,y,x])
      if a.text == "Ball 0.6🎾: 🙅‍♂ No Ball 🙅‍♂" or a.text == "Ball 0.6🎾: 🙆‍♂ Wide Ball 🙆‍♂":
        a = update.message.reply_text("*Ball 0.6🎾: " + r.replace("2","2⃣ Double 2⃣").replace("3","3⃣ Three 3⃣").replace("4","4⃣ Four 4⃣").replace("6","6⃣ Six Gya Six 6⃣").replace("1","1⃣ Single 1⃣") + "*",parse_mode=telegram.ParseMode.MARKDOWN)
        q = float(q) + float(r.replace("🚾 Run out 🚾","0.1").replace("🚾 Catch out 🚾","0.1").replace("🚾 Wicket 🚾","0.1").replace("🅾 Dot Ball 🅾","0").replace("🙅‍♂ No Ball 🙅‍♂","1").replace("🙆‍♂ Wide Ball 🙆‍♂","1"))*100
        time.sleep(1)
        x = random.choice(["3","2","4","3","2","1","2","3","2","4","6"])
        y = random.choice(["🚾 Run out 🚾","🚾 Catch out 🚾","🚾 Wicket 🚾"])
        z = random.choice(["🅾 Dot Ball 🅾"])
        r = random.choice([x,z,x,z,y,x])
        if a.text == "Ball 0.6🎾: 🙅‍♂ No Ball 🙅‍♂" or a.text == "Ball 0.6🎾: 🙆‍♂ Wide Ball 🙆‍♂":
          a = update.message.reply_text("*Ball 0.6🎾: " + r.replace("2","2⃣ Double 2⃣").replace("3","3⃣ Three 3⃣").replace("4","4⃣ Four 4⃣").replace("6","6⃣ Six Gya Six 6⃣").replace("1","1⃣ Single 1⃣") + "*")
          q = float(q) + float(r.replace("🚾 Run out 🚾","0.1").replace("🚾 Catch out 🚾","0.1").replace("🚾 Wicket 🚾","0.1").replace("🅾 Dot Ball 🅾","0").replace("🙅‍♂ No Ball 🙅‍♂","1").replace("🙆‍♂ Wide Ball 🙆‍♂","1"))*100
          time.sleep(1)
      update.message.reply_text("*" + update.message.text.split(' ')[1] + " Score :  " + str(float(q)/100).replace('.','/') + " 🅾🅾*",parse_mode=ParseMode.MARKDOWN)
    else:
      update.message.reply_text('Please write over number after command!')
		
__help__ = """
 - /shrug : get shrug XD.
 - /table : get flip/unflip :v.
 - /decide : Randomly answers yes/no/maybe
 - /abuse : Abuses the cunt
 - /tts <any text> : Converts text to speech
 - /rlg : Join ears,nose,mouth and create an emo ;-;
 - /zal <any text> : zalgofy! your tex Lyrics Plugin will take some moar time to come up.t
 - /send <any text>:  echo something (admin only)
 - /react : get a reaction
 - /gps <place> : get gps location
"""

__mod_name__ = "Extras"

OVER_HANDLER = DisableAbleCommandHandler("over", over)
TOSS_HANDLER = DisableAbleCommandHandler("toss",toss)
BALL_HANDLER = DisableAbleCommandHandler("ball",ball)
dispatcher.add_handler(OVER_HANDLER)
dispatcher.add_handler(TOSS_HANDLER)
dispatcher.add_handler(BALL_HANDLER)
