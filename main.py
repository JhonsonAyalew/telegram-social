from aiogram import Bot, Dispatcher, types
from aiogram.types import WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder
import asyncio
from config import BOT_TOKEN, WEBAPP_URL

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message()
async def start_command(message: types.Message):
    if message.text == "/start":
        # Store user info (we’ll connect to backend later)
        user = message.from_user

        # Create web app button
        kb = InlineKeyboardBuilder()
        kb.button(text="🛍 Open Marketplace", web_app=WebAppInfo(url=WEBAPP_URL))
        kb.adjust(1)

        await message.answer(
            f"👋 Hello {user.first_name}!\nWelcome to *Ethio Marketplace* — your gateway to all local Telegram shops.",
            parse_mode="Markdown",
            reply_markup=kb.as_markup()
        )

async def main():
    print("🚀 Bot is running...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
