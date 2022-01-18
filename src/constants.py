from types import SimpleNamespace
from telebot import types

from src.utils.keyboard import create_keyboard

markup = types.ReplyKeyboardMarkup(row_width=2)
itembtn1 = types.KeyboardButton('a')
itembtn2 = types.KeyboardButton('v')
itembtn3 = types.KeyboardButton('d')
markup.add(itembtn1, itembtn2, itembtn3)

keys = SimpleNamespace(
    random_connect = ':bust_in_silhouette: Random Connect',
    settings=':gear: Settings',

)

keyboards = SimpleNamespace(
    main=create_keyboard(keys.random_connect, keys.settings)

)
