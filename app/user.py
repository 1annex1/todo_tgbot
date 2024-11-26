from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command

from app.database.requests import set_user,del_tasks,set_tasks
import app.keyboards as kb 
# from middlewares import BaseMiddleware

user = Router()

# user.message.middleware(BaseMiddleware())

@user.message(CommandStart())
async def cmd_start(message: Message):
    await set_user(message.from_user.id)
    await message.answer('Нажмите на выполненную задачу чтобы удалить или напишите в чат новую.',reply_markup=await kb.tasks(message.from_user.id))


@user.callback_query(F.data.startswith('task_'))
async def delete_task(callback:CallbackQuery):
    await callback.answer('Задача выполнена!')
    await del_tasks(callback.data.split('_')[1])
    await callback.message.delete()
    await callback.message.answer('Нажмите на выполненную задачу чтобы удалить или напишите в чат новую.',reply_markup=await kb.tasks(callback.from_user.id))
   
    
    
@user.message()
async def add_task(message:Message):
    if len(message.text) > 100:
        await message.answer('Задача слишком длинная!')
        return
    await set_tasks(message.from_user.id,message.text)
    await message.answer('Задача добавленна\nНажмите на выполненную задачу чтобы удалить или напишите в чат новую.',reply_markup=await kb.tasks(message.from_user.id))