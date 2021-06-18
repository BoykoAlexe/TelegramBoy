import telebot
import datetime
from time import sleep
from telebot import types
from bs4 import BeautifulSoup
import requests

bot = telebot.TeleBot("1806174595:AAH787kHTcaPuiNqQwiuKI1I64mDsIDIiko")
day = ""
hours = ""
minute = ""
list0 = ["Что делает команда import?",
         "Какая функция отвечает за вывод на экран?",
         "Какая функция отвечает за открытие файла?",
         "Выберите вариант правильного удаления переменной а",
         "Какое значение 1//2 вернет выражение в среде IDLE?",
         "Как называется встроенный в языке Python тип данных неупорядоченной коллекции из нуля или более пар ключ-значение?",
         "Выберите правильную запись оператора присваивания:",
         "Сложный был тест?"]
list1 = [
    ["удаляет файл", "импортирует файл модуля", "создает функцию", "ничего"],
    ["cout<<a", "out(a)", "print(a)", "Ни одна из перечисленных"],
    ["file()", "open()", "open_file()", "Ни одна из перечисленных"],
    ["del(a)", "delete(a)", "delete=a", "Ни одно из перечисленных"],
    ["0", "0.5", "0.50", "Ни одно из перечисленных"],
    ["dict", "set", "list", "frozenset"],
    ["10 = х", "у = 7,8", "а = 5", "а == b + x"],
    ["Не сложный", "Средний", "Тяжелый", "Слишком тяжелый"]]
call_back = ["answer1", "answer2", "answer3", "answer4", "answer5", "answer6",
             "answer7", "answer8", "answer9",
             "answer10", "answer11", "answer12", "answer13", "answer14",
             "answer15", "answer16", "answer17", "answer18",
             "answer19", "answer20", "answer21", "answer22", "answer23",
             "answer24", "answer25", "answer26", "answer27",
             "answer28", "answer29", "answer30", "answer31", "answer32",
             "answer33", "answer34", "answer35", "answer36",
             "answer37", "answer38", "answer39", "answer40"]

K = 0
POINT = 0
P = 0
URL = "https://student.mirea.ru/"
URLK = "https://student.mirea.ru"
NAP = ""


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет, меня зовут Python_boy\n"
                          "Я могу поставить напоминание - /zav_bud\n"
                          "Могу дать порешать тест  - /test\n"
                          "Могу прислать полезные файлы - /get_files\n"
                          "Могу рассказать последние новости МИРЭА - /news")


@bot.message_handler(commands=['del_bud'])
def del_bud(message):
    global hours
    global minute
    global day
    hours = ""
    minute = ""
    day = ""


@bot.message_handler(commands=['us_bud'])
def us_bud(message):
    global NAP
    global hours
    global minute
    global day
    while True:
        if hours == "" and day == "" and minute == "":
            break
        time_now = datetime.datetime.now()
        if str(time_now.hour) == str(hours) and str(time_now.minute) == str(
                minute) and str(time_now.day) == str(day):
            for i in range(5):
                sleep(2)
                bot.reply_to(message, NAP)
            hours = ""
            minute = ""
            day = ""
            NAP = ""
            break


@bot.message_handler(commands=['zav_bud'])
def zav_bud(message):
    global hours
    global minute
    global day
    bot.send_message(message.from_user.id, "На какой деннь поставить напоминание?")
    bot.register_next_step_handler(message, day_s)


def day_s(message):
    global day
    day = message.text
    bot.send_message(message.from_user.id, "На сколько часов?")
    bot.register_next_step_handler(message, hours_s)


def hours_s(message):
    global hours
    hours = message.text
    bot.send_message(message.from_user.id, "На сколько минут?")
    bot.register_next_step_handler(message, minute_s)


def minute_s(message):
    global minute
    global day
    global hours
    minute = message.text
    bot.send_message(message.from_user.id, "Напиши текст для напоминания")
    bot.register_next_step_handler(message, zav_bud1)


def zav_bud1(message):
    global NAP
    global minute
    global day
    global hours
    strl = "В " + hours + " часов " + minute + " минут придет оповещение!"
    NAP = message.text
    bot.send_message(message.chat.id, strl + "\nДля того чтобы установить будильник напишите - /us_bud")


@bot.message_handler(commands=['test'])
def test(message):
    global POINT
    global P
    global K
    bot.send_message(message.from_user.id,
                     "Через 5 секунд будет предоставлен тест на 8 вопросов.\nУдачи на тесте😉")
    sleep(5)
    while K <= 7:
        if K == 0 and P == 0:
            markup = types.InlineKeyboardMarkup(row_width=1)
            ans1 = types.InlineKeyboardButton(list1[0][0],
                                              callback_data="answer1")
            ans2 = types.InlineKeyboardButton(list1[0][1],
                                              callback_data="answer2")
            ans3 = types.InlineKeyboardButton(list1[0][2],
                                              callback_data="answer3")
            ans4 = types.InlineKeyboardButton(list1[0][3],
                                              callback_data="answer4")
            markup.add(ans1, ans2, ans3, ans4)
            bot.send_message(message.chat.id, list0[0], reply_markup=markup)
            P = 1
        elif K == 1 and P == 0:
            sleep(2)
            markup = types.InlineKeyboardMarkup(row_width=1)
            ans1 = types.InlineKeyboardButton(list1[1][0],
                                              callback_data=call_back[4])
            ans2 = types.InlineKeyboardButton(list1[1][1],
                                              callback_data=call_back[5])
            ans3 = types.InlineKeyboardButton(list1[1][2],
                                              callback_data=call_back[6])
            ans4 = types.InlineKeyboardButton(list1[1][3],
                                              callback_data=call_back[7])
            markup.add(ans1, ans2, ans3, ans4)
            bot.send_message(message.chat.id, list0[1], reply_markup=markup)
            P = 1
        elif K == 2 and P == 0:
            sleep(2)
            markup = types.InlineKeyboardMarkup(row_width=1)
            ans1 = types.InlineKeyboardButton(list1[2][0],
                                              callback_data=call_back[8])
            ans2 = types.InlineKeyboardButton(list1[2][1],
                                              callback_data=call_back[9])
            ans3 = types.InlineKeyboardButton(list1[2][2],
                                              callback_data=call_back[10])
            ans4 = types.InlineKeyboardButton(list1[2][3],
                                              callback_data=call_back[11])
            markup.add(ans1, ans2, ans3, ans4)
            bot.send_message(message.chat.id, list0[2], reply_markup=markup)
            P = 1
        elif K == 3 and P == 0:
            sleep(2)
            markup = types.InlineKeyboardMarkup(row_width=1)
            ans1 = types.InlineKeyboardButton(list1[3][0],
                                              callback_data=call_back[12])
            ans2 = types.InlineKeyboardButton(list1[3][1],
                                              callback_data=call_back[13])
            ans3 = types.InlineKeyboardButton(list1[3][2],
                                              callback_data=call_back[14])
            ans4 = types.InlineKeyboardButton(list1[3][3],
                                              callback_data=call_back[15])
            markup.add(ans1, ans2, ans3, ans4)
            bot.send_message(message.chat.id, list0[3], reply_markup=markup)
            P = 1
        elif K == 4 and P == 0:
            sleep(2)
            markup = types.InlineKeyboardMarkup(row_width=1)
            ans1 = types.InlineKeyboardButton(list1[4][0],
                                              callback_data=call_back[16])
            ans2 = types.InlineKeyboardButton(list1[4][1],
                                              callback_data=call_back[17])
            ans3 = types.InlineKeyboardButton(list1[4][2],
                                              callback_data=call_back[18])
            ans4 = types.InlineKeyboardButton(list1[4][3],
                                              callback_data=call_back[19])
            markup.add(ans1, ans2, ans3, ans4)
            bot.send_message(message.chat.id, list0[4], reply_markup=markup)
            P = 1
        elif K == 5 and P == 0:
            sleep(2)
            markup = types.InlineKeyboardMarkup(row_width=1)
            ans1 = types.InlineKeyboardButton(list1[5][0],
                                              callback_data=call_back[20])
            ans2 = types.InlineKeyboardButton(list1[5][1],
                                              callback_data=call_back[21])
            ans3 = types.InlineKeyboardButton(list1[5][2],
                                              callback_data=call_back[22])
            ans4 = types.InlineKeyboardButton(list1[5][3],
                                              callback_data=call_back[23])
            markup.add(ans1, ans2, ans3, ans4)
            bot.send_message(message.chat.id, list0[5], reply_markup=markup)
            P = 1
        elif K == 6 and P == 0:
            sleep(2)
            markup = types.InlineKeyboardMarkup(row_width=1)
            ans1 = types.InlineKeyboardButton(list1[6][0],
                                              callback_data=call_back[24])
            ans2 = types.InlineKeyboardButton(list1[6][1],
                                              callback_data=call_back[25])
            ans3 = types.InlineKeyboardButton(list1[6][2],
                                              callback_data=call_back[26])
            ans4 = types.InlineKeyboardButton(list1[6][3],
                                              callback_data=call_back[27])
            markup.add(ans1, ans2, ans3, ans4)
            bot.send_message(message.chat.id, list0[6], reply_markup=markup)
            P = 1
        elif K == 7 and P == 0:
            sleep(2)
            markup = types.InlineKeyboardMarkup(row_width=1)
            ans1 = types.InlineKeyboardButton(list1[7][0],
                                              callback_data=call_back[28])
            ans2 = types.InlineKeyboardButton(list1[7][1],
                                              callback_data=call_back[29])
            ans3 = types.InlineKeyboardButton(list1[7][2],
                                              callback_data=call_back[30])
            ans4 = types.InlineKeyboardButton(list1[7][3],
                                              callback_data=call_back[31])
            markup.add(ans1, ans2, ans3, ans4)
            bot.send_message(message.chat.id, list0[7], reply_markup=markup)
            bot.send_message(message.chat.id,
                             "Ты набрал " + str(POINT) + " балов из 7!!!")
            sleep(2)
            if 0 <= POINT < 3:
                bot.send_message(message.chat.id, "Это очень плохо")
            elif 3 <= POINT < 5:
                bot.send_message(message.chat.id, "Да уж, зананий не хватает")
            else:
                bot.send_message(message.chat.id,
                                 "Супер, но не расслабляйся!!!")
            P = 1


@bot.callback_query_handler(func=lambda call: True)
def ansic(call):
    global K
    global P
    global POINT
    if call.message:
        if call.data == "answer2":
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.id,
                                  text="Вопрос 1 - Верно!")  # !!!
            K = 1
            POINT = POINT + 1
            P = 0
            sleep(1)
        elif call.data == "answer1" or call.data == "answer3" or call.data == "answer4":
            K = 1
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.id,
                                  text="Вопрос 1 - Неверно!")
            P = 0
            sleep(1)
        elif call.data == "answer5" or call.data == "answer6" or call.data == "answer8":
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.id,
                                  text="Вопрос 2 - Неверно!")
            K = 2
            P = 0
            sleep(1)
        elif call.data == "answer9" or call.data == "answer11" or call.data == "answer12":
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.id,
                                  text="Вопрос 3 - Неверно!")
            K = 3
            P = 0
            sleep(1)
        elif call.data == "answer13" or call.data == "answer15" or call.data == "answer16":
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.id,
                                  text="Вопрос 4 - Неверно!")
            K = 4
            P = 0
            sleep(1)
        elif call.data == "answer19" or call.data == "answer18" or call.data == "answer20":
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.id,
                                  text="Вопрос 5 - Неверно!")
            K = 5
            P = 0
            sleep(1)
        elif call.data == "answer22" or call.data == "answer23" or call.data == "answer24":
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.id,
                                  text="Вопрос 6 - Неверно!")
            K = 6
            P = 0
            sleep(1)
        elif call.data == "answer25" or call.data == "answer26" or call.data == "answer28":
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.id,
                                  text="Вопрос 7 - Неверно!")
            K = 7
            P = 0
            sleep(1)
        elif call.data == "answer7":
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.id,
                                  text="Вопрос 2 - Верно!")  # !!!
            K = 2
            POINT = POINT + 1
            P = 0
            sleep(1)
        elif call.data == "answer10":
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.id,
                                  text="Вопрос 3 - Верно!")
            K = 3
            POINT = POINT + 1
            P = 0
            sleep(1)
        elif call.data == "answer14":
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.id,
                                  text="Вопрос 4 - Верно!")
            K = 4
            POINT = POINT + 1
            P = 0
            sleep(1)
        elif call.data == "answer17":
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.id,
                                  text="Вопрос 5 - Верно!")
            K = 5
            POINT = POINT + 1
            P = 0
            sleep(1)
        elif call.data == "answer21":
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.id,
                                  text="Вопрос 6 - Верно!")
            K = 6
            POINT = POINT + 1
            P = 0
            sleep(1)
        elif call.data == "answer27":
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.id,
                                  text="Вопрос 7 - Верно!")
            K = 7
            POINT = POINT + 1
            P = 0
            sleep(1)
        elif call.data == "answer29":
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.id,
                                  text="Отлично, ты готов!!!")
            K = 8
            P = 0
            sleep(3)
        elif call.data == "answer30":
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.id,
                                  text="Стоит немного подтянуть знания!!!")
            K = 8
            P = 0
            sleep(3)
        elif call.data == "answer31":
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.id,
                                  text="Ужас, скоро экзамен!!!")
            K = 8
            P = 0
            sleep(3)
        elif call.data == "answer32":
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.id,
                                  text="Мне нечего сказать😔")
            K = 8
            P = 0
            sleep(3)


@bot.message_handler(commands=["get_files"])
def files(message):
    f = open("C:\oprosi.pdf", "rb")
    f1 = open("C:\metodichka.pdf", "rb")
    bot.send_document(message.chat.id, f)
    bot.send_document(message.chat.id, f1)


@bot.message_handler(commands=["news"])
def news(message):
    global URL
    global URLK
    request = requests.get(URL)
    soup = BeautifulSoup(request.text, "html.parser")
    fil = soup.find("div", class_="g-mb-35")
    fil1 = soup.find("a",
                     class_="btn u-shadow-v39 g-color-white g-color-white--hover g-bg-main g-bg-primary--hover g-font-size-default g-rounded-30 g-px-35 g-py-8")
    bot.send_message(message.chat.id, fil.text)
    href = str(fil1.get("href"))
    url2 = URLK + href
    bot.send_message(message.chat.id, url2)


bot.polling()
