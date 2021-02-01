import requests
import telebot
from settings import key

bot = telebot.TeleBot(key)
weather_parameters = {
    'format': 4,
    'M': ''
    # добавьте параметр запроса `T`, чтобы вернулся чёрно-белый текст
}


@bot.message_handler(commands=['start', 'help'])    
def handle_start_help(message):
    bot.send_message(
        message.chat.id,
        'Привет! Узнай погоду в любой точке планеты.\n\n'
        'Поддерживаемые типы местоположений:\n'
        '• Kazan, Казань - город на любом языке\n'
        '• Eiffel Tower - любое местоположение\n'
        '• SVO - код аэропорта по ICAO (3 буквы)\n'
        '• @stackoverflow.com - доменное имя\n'
        '• 94107 - почтовый индекс (только для США)\n'
        '• 53.638801, 55.964665 - GPS-координаты\n'
    )


@bot.message_handler(content_types=['text'])
def get_messages(message):
    city = message.text
    bot.send_message(message.chat.id, city_weather(city))


def city_weather(city):
    url = f'https://wttr.in/{city}'
    response = requests.get(url, params=weather_parameters)
    return response.text


bot.polling(none_stop=True, timeout=20)
