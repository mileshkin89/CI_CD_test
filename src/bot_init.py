from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.enums.parse_mode import ParseMode
from src.config import config

# Dispatcher responsible for handling updates and storing FSM state in memory.
dp = Dispatcher(storage=MemoryStorage())

# Bot instance configured with token and default parse mode (HTML formatting for messages).
bot = Bot(
    token=config.TG_BOT_API_KEY,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)