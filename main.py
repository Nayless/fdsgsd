import telebot;

bot = telebot.TeleBot('1447603831:AAGbwnXcfhCRBzN6KCbjaBZVIE7nfSerz9A');
keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('/help')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    keyboard1.row('Купить', 'Схема', 'Канал')
    if message.text == "/help":
        bot.send_message(message.from_user.id, "Купить - информация о покупке        Схема - информация о схеме")
    elif message.text == "Купить":
        bot.send_message(message.from_user.id, "Чтобы приобрести схему напиши @cXema_seller")
    elif message.text == "Схема":
        bot.send_message(message.from_user.id, "Предпросмотр Схемы https://drive.google.com/drive/folders/1kawUB8kXfudxu1hOKmfVrYlnEJQwRodh")
    elif message.text == "Канал":
        bot.send_message(message.from_user.id, "Вот ссылка на наш канал - @cXema_money")
    else:
        bot.send_message(message.from_user.id, "Напиши /help если хочешь зарабатывать прямо сейчас", reply_markup=keyboard1)
bot.polling(none_stop=True, interval=0)
