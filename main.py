import io
import requests
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text

TOKEN = "6014463386:AAEO-UIB7SFcQHDKlbrKfrGa5wb5V2sKFLQ"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_motivation(message: types.Message):
    await message.reply("Привет! Ты зашел в бот по генерации мотивации!")
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["мотивируй меня!", "давай поговорим"]
    keyboard.add(*buttons)
    await message.answer("Чем я могу тебе помочь?", reply_markup=keyboard)

@dp.message_handler(Text(equals="мотивируй меня!"))
async def send_motivation_photo(message: types.Message):
    await message.reply("Лови заряд мотивации!")

    response = requests.get('https://source.unsplash.com/featured/?motivation')
    photo = response.content

    await bot.send_photo(message.chat.id, photo)


@dp.message_handler(lambda message: message.text == "давай поговорим")
async def without_Up_your_motivation_now_bot2(message: types.Message):
    await message.reply("Хорошо! Расскажу немного о себе:)\n Я был создан студенткой Полиной специально для того, чтобы заряжать людей мотивацией. ")
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Я пользователь", "Я преподаватель", "Вернуться"]
    keyboard.add(*buttons)
    await message.answer("А ты кто такой?", reply_markup=keyboard)

@dp.message_handler(Text(equals="Я пользователь"))
async def with_Up_your_motivation_now_bot3(message: types.Message):
    await message.reply("Очень приятно познакомиться!)")
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Я вымотан", "Замечательно)", "Немного поговорив с тобой, стало легче)", "Вернуться"]
    keyboard.add(*buttons)
    await message.answer("Как у тебя дела? Наверняка хочешь отдохнуть, да?", reply_markup=keyboard)

@dp.message_handler(Text(equals="Я вымотан"))
async def with_Up_your_motivation_now_bot4(message: types.Message):
    await message.reply("Это печально(. Хочешь дам совет? :)\n Ложись сегодня спать по-раньше:)\n Я слышал, что это обычно помогает людям")

@dp.message_handler(Text(equals="Замечательно)"))
async def with_Up_your_motivation_now_bot5(message: types.Message):
    await message.reply("Отлично!)")

@dp.message_handler(Text(equals="Немного поговорив с тобой, стало легче)"))
async def with_Up_your_motivation_now_bot6(message: types.Message):
    await message.reply("Ура, рад что был полезен!)")

@dp.message_handler(Text(equals="Я преподаватель"))
async def with_Up_your_motivation_now_bot7(message: types.Message):
    await message.reply("извините, технические неполадки со временем сдачи...:)\n Надо чутка подправить...")

@dp.message_handler(lambda message: message.text == "Вернуться")
async def without_Up_your_motivation_now_bot8(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["мотивируй меня!", "давай поговорим"]
    keyboard.add(*buttons)
    await message.answer("Чем я могу тебе помочь?", reply_markup=keyboard)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
