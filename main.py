#!/usr/bin/env python
# -*- coding: utf-8 -*-

#@Cadet_Helper_bot
#import telethon(soon...)
import telebot
import config
import random

from telebot import types

bot = telebot.TeleBot(config.TOKEN)
#Adding new buttons and keyboards
#Keyboard for arrived people
who = types.InlineKeyboardMarkup(row_width=3)
button1 = types.InlineKeyboardButton("name", callback_data='NK')
button2 = types.InlineKeyboardButton("name", callback_data='tup')
button3 = types.InlineKeyboardButton("name", callback_data='sport')
button4 = types.InlineKeyboardButton("name", callback_data='fat')
button5 = types.InlineKeyboardButton("name", callback_data='poh')
button6 = types.InlineKeyboardButton("name", callback_data='pzdc')
button7 = types.InlineKeyboardButton("name", callback_data='nothing')
#Adding our buttons to our new keyboard
#Adding another buttons and keyboard for leaved people
who.add(button1, button2, button3, button4, button5, button6, button7)
who1 = types.InlineKeyboardMarkup(row_width=3)
button11 = types.InlineKeyboardButton("name", callback_data='NK1')
button21 = types.InlineKeyboardButton("name", callback_data='tup1')
button31 = types.InlineKeyboardButton("name", callback_data='sport1')
button41 = types.InlineKeyboardButton("name", callback_data='fat1')
button51 = types.InlineKeyboardButton("name", callback_data='poh1')
button61 = types.InlineKeyboardButton("name", callback_data='pzdc1')
button71 = types.InlineKeyboardButton("name", callback_data='nothing1')
#Adding new buttons to the last keyboard
who1.add(button11, button21, button31, button41, button51, button61, button71)
#Creating list and counter
Whoisthere = []
counter = int(0)
#Another one keyboard
markup = types.InlineKeyboardMarkup(row_width=3)
item1 = types.InlineKeyboardButton("Choose random number!🎲", callback_data="random")
item2 = types.InlineKeyboardButton("At Ease!", callback_data='At_ease')
item3 = types.InlineKeyboardButton("Report", callback_data='kurs')
markup.add(item1, item2, item3)
#Creating a command handler
#Adding commands to handler
@bot.message_handler(commands=['help', 'smirno', 'chat_id'])
def comms(message):
    try:
        if '/help' in message.text:
            sti = open('sticker_directory.webp', 'rb')
            bot.send_sticker(message.chat.id, sti)
            bot.send_message(message.chat.id, '/help - command list\n/smirno - Attention command')
        elif '/smirno' in message.text:
            sti = open('some_sticker.tgs', 'rb')
            bot.send_sticker(message.chat.id, sti)
            bot.send_message(message.chat.id,
                             "Товарищ {0.first_name} {0.last_name}, Some report.\nAnother part of report.\nSome bot <b>{1.first_name}</b> \n Is reporting. At your service".format(
                                 message.from_user, bot.get_me()),
                             parse_mode='html', reply_markup=markup)
        elif '/chat_id' in message.text:
            bot.send_message(message.chat.id, message.chat.id)
    except Exception as e:
        print(repr(e))
@bot.message_handler(content_types=['text'])
def at_ease(message):
    try:
        if 'At ease' in message.text:
            bot.send_message(message.chat.id, "Chat, At Ease!!!")
        elif 'Call bot' in message.text.lower():
            bot.send_message(message.chat.id,
                             "I am {1.first_name}!".format(
                                 message.from_user, bot.get_me()),
                             parse_mode='html', reply_markup=markup)
    except Exception as e:
        print(repr(e))
#We used some new buttons in last actions and now we must use the call data of this buttons
@bot.callback_query_handler(func=lambda call: True)
def comrep(call):
    global Whoisthere
    global counter
    try:
        if call.message:
            # random number
            if call.data == 'random':
                bot.send_message(call.message.chat.id, str(random.randint(1, 15)))
                bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup='')
                bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                              reply_markup=markup)
                # At ease
            elif call.data == 'At_ease':
                bot.send_message(call.message.chat.id, "Chat, At ease!")
                bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                              reply_markup='')
                bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                              reply_markup=markup)
                # situation
            elif call.data == 'kurs':
                bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                              reply_markup='')
                reportkb = types.InlineKeyboardMarkup(row_width=1)
                whocame = types.InlineKeyboardButton("Somebody came", callback_data="came")
                wholeave = types.InlineKeyboardButton("Somebody arrived", callback_data="leave")
                ktoest = types.InlineKeyboardButton("What's up???", callback_data='kto')
                reportkb.add(whocame, wholeave, ktoest)
                bot.send_message(call.message.chat.id, 'Who is there?...', reply_markup=reportkb)
            elif call.data == 'came':
                bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                              reply_markup='')
                bot.send_message(call.message.chat.id, "Кто пришёл?", reply_markup=who)
            # The logic of choice
            elif call.data == 'kto':
                bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                              reply_markup='')
                if counter == 0:
                    bot.send_message(call.message.chat.id, f"Здесь сейчас никого")
                elif counter <= 4:
                    bot.send_message(call.message.chat.id, f"Здесь сейчас {counter} объекта:")
                    for i in range(counter):
                        bot.send_message(call.message.chat.id, f'{i+1}) {Whoisthere[i]} ;')
                elif counter >= 5:
                    bot.send_message(call.message.chat.id, f"Здесь сейчас {counter} объектов:")
                    for i in range(counter):
                        bot.send_message(call.message.chat.id, f'{i + 1}) {Whoisthere[i]} ;')

            elif call.data == 'leave':
                bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                              reply_markup='')
                bot.send_message(call.message.chat.id, "Кто ушёл?", reply_markup=who1)
            elif call.data == 'NK1':
                if "name" in Whoisthere:
                    Whoisthere.remove("name")
                    counter -= 1
                else:
                    print('XYU')
                    bot.send_message(call.message.chat.id, "Тут таких не было")
            elif call.data == 'tup1':
                if "name" in Whoisthere:
                    Whoisthere.remove("name")
                    counter -= 1
                else:
                    bot.send_message(call.message.chat.id, "Таких не видел")
            elif call.data == 'sport1':
                if "name" in Whoisthere:
                    Whoisthere.remove("name")
                    counter -= 1
                else:
                    bot.send_message(call.message.chat.id, "Его вроде и не было")
            elif call.data == 'fat1':
                if "name" in Whoisthere:
                    Whoisthere.remove("name")
                    counter -= 1
                else:
                    bot.send_message(call.message.chat.id, "Он куда-то ушёл")
            elif call.data == 'poh1':
                if "name" in Whoisthere:
                    Whoisthere.remove("name")
                    counter -= 1
                else:
                    bot.send_message(call.message.chat.id, "Та тут особо никто и не приходил")
            elif call.data == 'nothing1':
                return Whoisthere
            elif call.data == 'pzdc1':
                if "name" in Whoisthere:
                    Whoisthere.remove("name")
                    counter -= 1
                else:
                    bot.send_message(call.message.chat.id,
                                     "Короче, бля, что-то твоя разведка хуёво работает... Никаких важных хуёв тут и не бывало...")
            elif call.data == 'tup':
                if 'name' in Whoisthere:
                    bot.send_message(call.message.chat.id, 'Он и так тут был')
                else:
                    Whoisthere.append('name')
                    counter += 1
            elif call.data == 'sport':
                if "name" in Whoisthere:
                    bot.send_message(call.message.chat.id, "Он и так тут был")
                else:
                    Whoisthere.append("name")
                    counter += 1
            elif call.data == 'fat':
                if "name" in Whoisthere:
                    bot.send_message(call.message.chat.id, 'Он и так тут был')
                else:
                    Whoisthere.append("name")
                    counter += 1
            elif call.data == 'name':
                if "name" in Whoisthere:
                    bot.send_message(call.message.chat.id, 'Он и так тут был')
                else:
                    Whoisthere.append("name")
                    counter += 1
            elif call.data == 'poh':
                if "name" in Whoisthere:
                    bot.send_message(call.message.chat.id, 'Пока не уходил')
                else:
                    Whoisthere.append("name")
                    counter += 1
            elif call.data == "name":
                if "name" in Whoisthere:
                    bot.send_message(call.message.chat.id, 'Он(Они) всё ещё тут')
                else:
                    Whoisthere.append("name")
                    counter += 1
    except Exception as e:
        print(repr(e))
bot.polling(none_stop=True)
