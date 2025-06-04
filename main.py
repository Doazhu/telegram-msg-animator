import asyncio
import os
from dotenv import load_dotenv
from telethon import TelegramClient, errors
from telethon.tl.custom.message import Message

load_dotenv()
"""
создайте файл .env в корне проекта и в нем заполните следующие данные:

API_ID=1234
API_HASH=abs123
"""
api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")

async def animate_message():
    client = TelegramClient('animation_session', api_id, api_hash)

    async with client:
        frames = [
            "Начинаем анимацию...",
            "Первый кадр",
            "Второй кадр",
            "Третий кадр",
            "Анимация завершена!"
        ]
        # Варианты указания получателя:
        # 'me' - для себя (Избранное)
        # '@username' - по имени пользователя
        # phone_number - по номеру телефона
        # chat_id - по ID чата (для групп)

        message: Message = await client.send_message('@me', frames[0])

        for frame in frames[1:]:
            await asyncio.sleep(1.5)  # Задержка
            try:
                await message.edit(frame)
            except errors.FloodWaitError as e:
                print(f"Ожидание {e.seconds} секунд...")
                await asyncio.sleep(e.seconds)
                await message.edit(frame)


asyncio.run(animate_message())


"""
Эффект печатающей машинки
async def typewriter_effect():
client = TelegramClient('typewriter_session', api_id, api_hash)

async with client:
text = "Этот текст появляется по одной букве!"
message = await client.send_message('me', "")

for i in range(1, len(text) + 1):
try:
await message.edit(text[:i])
await asyncio.sleep(0.1)  # Быстрая печать
except errors.FloodWaitError as e:
await asyncio.sleep(e.seconds)
await message.edit(text[:i])

asyncio.run(typewriter_effect())

"""

"""
Анимация с эмодзи
async def emoji_animation():
client = TelegramClient('emoji_session', api_id, api_hash)

async with client:
loading_frames = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
message = await client.send_message('me', f"{loading_frames[0]} Загрузка...")

for _ in range(20):  # 20 циклов анимации
for frame in loading_frames:
try:
await message.edit(f"{frame} Загрузка...")
await asyncio.sleep(0.3)
except errors.FloodWaitError as e:
await asyncio.sleep(e.seconds)

await message.edit("✅ Загрузка завершена!")

asyncio.run(emoji_animation())

"""
