# Epic Games Free Games Telegram Bot

This is a Telegram bot that provides a list of free games available on the Epic Games Store. The bot retrieves the game data using the Epic Games Store API and sends the game information along with their promotional images to the user.

## Prerequisites

Before running the bot, make sure you have the following installed:

- Python 3.x
- `telebot` library
- `requests` library
- `Pillow` library
- `epicstore_api` library

You can install these dependencies using `pip`:

```
pip install telebot requests Pillow epicstore_api
```

## Configuration

1. Obtain a Telegram bot token: 

   - Create a new bot by talking to [BotFather](https://t.me/BotFather) on Telegram.
   - Follow the instructions to create a new bot and obtain the bot token.

2. Update the `TOKEN` variable:
   
   - Replace `'TOKEN'` with your Telegram bot token in the script.

## Usage

To use the bot, follow these steps:

1. Run the script:

   ```
   python bot.py
   ```

2. Start a conversation with your bot on Telegram.

3. Send the command `/help` to see the available commands.

4. To get the list of free games, send the command "Игры" to the bot.

5. The bot will retrieve the game information and send it to you. If there are promotional images available for a game, the bot will also send the images along with the information.

## Contributing

If you want to contribute to this project, feel free to fork the repository and submit pull requests with your changes. You can also open issues to report bugs or suggest improvements.

## License

This project is licensed under the [MIT License](LICENSE).
