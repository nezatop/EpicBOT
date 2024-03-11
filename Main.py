import telebot
import requests
from io import BytesIO
from PIL import Image
import os
from epicstore_api import EpicGamesStoreAPI
import json


TOKEN = 'TOKEN'

def games_extractor():
    api = EpicGamesStoreAPI()
    return api.get_free_games()['data']['Catalog']['searchStore']['elements']


def save_game_list_to_json(gamelist, filename):
    games_data = []
    for game in gamelist:
        games_data.append(game)
    with open(filename, "w") as json_file:
        json.dump(games_data, json_file, indent=4)
    print("Game list saved as", filename)


def main():
    bot = telebot.TeleBot(TOKEN)
    games = games_extractor()
    save_game_list_to_json(games, "games.json")

    @bot.message_handler(content_types=['text'])
    def get_text_messages(message):
        if message.text == "Игры":
            for game in games:
                title = game['title']
                description = game['description']
                photos = game['keyImages']
                response = f"{title}\n{description}\n"
                photo_files = []
                for photo in photos:
                    if photo['type'] == 'OfferImageWide':
                        photo_url = photo['url']
                        photo_file = download_photo(photo_url)
                        if photo_file:
                            photo_files.append(photo_file)
                if not photo_files:
                    bot.send_message(message.chat.id, response)
                for photo_file in photo_files:
                    with open(photo_file, "rb") as photo:
                        bot.send_photo(message.chat.id, photo, caption=response)
                for photo_file in photo_files:
                    os.remove(photo_file)
        elif message.text == "/help":
            bot.send_message(message.chat.id, "Если хочешь получить список белплатных игр. \n Напиши Игры")
        else:
            bot.send_message(message.chat.id, "Я тебя не понимаю. Напиши /help.")

    bot.polling(none_stop=True, interval=0)


def download_photo(photo_url):
    try:
        response = requests.get(photo_url)
        response.raise_for_status()
        image_data = response.content
        image = Image.open(BytesIO(image_data))
        image_filename = "temp_image.jpg"
        image.save(image_filename)
        return image_filename
    except Exception as e:
        print("Error downloading photo:", e)
        return None


if __name__ == '__main__':
    main()
