This app runs Telegram bot, that give you current weather by city name.
To run this bot you need to add .env file with 2 tokens:
* API_TOKEN 
* OPENWEATHER_API_KEY

1. First token you can get from BotFather in Telegram. There you need to register your bot, give it a username and get the token in return.
2. Second token you can get from https://openweathermap.org/api. Here you need to register and Subscribe to One Call API 3.0.<br>
P.s. Make sure you set max calls to free 1000 (the default value is 2000, when there are only 1000 of them being free). After the registration you will be able
to get the token in your profile at https://home.openweathermap.org/api_keys.
3. Also, you need to install dependencies using 'pip install -r requirements.txt'.
   
After setting both tokens and installing requirements you just need to run bot.py and find this bot in Telegram by username you gave it in step 1.
