import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

API_TOKEN = '5410029850:AAE7Fy04R3Z9DyzRBha5lciD4m9D-0zlXfY'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

class Balance(StatesGroup):
    waiting_for_sum = State()
    mak_payment = State()

@dp.callback_query_handler(text="deposit")
async def create_expense(call: types.CallbackQuery):
    await call.message.answer("Введите сумму, на которую вы хотите пополнить баланс")
    await call.answer()

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Пополнить баланс", callback_data="deposit"))
    await message.answer(f"Привет {message.from_user.full_name}")
    await message.answer("Я - бот для пополнения баланса.\nНажмите на кнопку, чтобы пополнить баланс.", reply_markup=keyboard)
    await Balance.waiting_for_sum.set()
    await Balance.next()

# @dp.message_handler()
# async def echo(message: types.Message):
#     # old style:
#     # await bot.send_message(message.chat.id, message.text)
#
#     await message.answer(message.text)

@dp.message_handler(commands="admin")
async def cmd_test1(message: types.Message):
    await message.answer("admin")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)