import os
import asyncio
import requests
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.filters.command import Command
from aiogram.fsm.storage.memory import MemoryStorage

load_dotenv()
API_TOKEN = os.getenv('API_TOKEN')
OPENWEATHER_API_KEY = os.getenv('OPENWEATHER_API_KEY')

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot=bot, storage=MemoryStorage())


class GetWeather(StatesGroup):
    city = State()


@dp.message(Command("start"))
async def start_command(message: types.Message, state: FSMContext):
    await message.answer("Hi! 👋 Enter city name to get current weather:")
    await state.set_state(GetWeather.city)


@dp.message(GetWeather.city)
async def fetch_weather(message: types.Message, state: FSMContext):
    city = message.text

    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}&units=metric'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        description = data['weather'][0]['description']
        icon_code = data['weather'][0]['icon']
        icon_url = f"http://openweathermap.org/img/wn/{icon_code}@4x.png?appid={OPENWEATHER_API_KEY}"
        await message.answer_photo(icon_url, caption=f"It's {temp}°C in {city} right now, {description}.")
    else:
        await message.answer("Unfortunately, I couldn't get the weather data. Please, check the city name you entered.")
    await state.set_state(GetWeather.city)


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
