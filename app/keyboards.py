from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

from app.database.requests import get_tasks

async def tasks(tg_id):
   tasks = await get_tasks(tg_id)
   keyboard = InlineKeyboardBuilder()
   for task in tasks:
       keyboard.add(InlineKeyboardButton(text=task.task,callback_data=f'task_{task.id}'))
   return keyboard.adjust(1).as_markup()
       
       