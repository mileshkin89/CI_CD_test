from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
import datetime

router = Router()

@router.message(F.text)
async def cmd_start(message: Message):
    new_time = datetime.datetime.now()
    await message.answer(f"Time now = {new_time.hour}:{new_time.minute}:{new_time.second}\nupdate: avto deploy")