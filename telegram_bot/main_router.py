from aiogram import Router, Bot
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.filters import CommandStart

from model_worker import predict_rating

class MainRouter(Router):
    def __init__(self, bot: Bot) -> None:
        super().__init__()

        self.bot = bot

        self.message.register(self.enter_handler, CommandStart())
        self.message.register(self.default_handler)

    async def default_handler(self, message: Message) -> None:
        tags = predict_rating(message.text)[0]
        await message.reply(f"Даю следующие теги этому тексту: {tags}")
    
    async def enter_handler(self, message: Message, state: FSMContext) -> None:
        await message.answer("Привет! Я бот который даёт оценку комментариям.\n\nНапиши мне что-нибудь, и я попробую оценить его.")
