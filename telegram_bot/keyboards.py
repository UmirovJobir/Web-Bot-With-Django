from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

# web_app = WebAppInfo(url="https://UmirovJobir.github.io/")
web_app = WebAppInfo(url="https://2525-91-188-129-195.in.ngrok.io/catalogue/")

keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Каталог", web_app=web_app)]
    ],
    resize_keyboard=True
)

cb = CallbackData('btn', 'action')
key = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton('Pay', callback_data='btn:buy')]]
)
