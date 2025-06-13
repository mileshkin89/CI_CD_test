
import asyncio
from logging_config import get_logger
from bot_init import bot, dp
import start

logger = get_logger(__name__)


async def main():
    # Register command routers
    dp.include_router(start.router)

    # Start polling the Telegram API
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)



if __name__ == "__main__":
    logger.info("Bot started successfully.")
    asyncio.run(main())

