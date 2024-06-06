import asyncio

from aiogram import Bot, Dispatcher, enums

from keys import get_bot_key
from main_router import MainRouter

# https://t.me/hse_ml_sp2024_bot
bot = Bot(get_bot_key())
dp = Dispatcher()

main_router = MainRouter(bot)

async def main() -> None:
    dp.include_routers(
        main_router
    )

    await bot.delete_webhook()

    poll = asyncio.create_task(dp.start_polling(bot))

    print('Bot started')

    await poll

if __name__ == "__main__":
    print('Initializing...')
    asyncio.run(main())
