from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands(bot: Bot):
    commands = [
        BotCommand(
            command="start",
            description="Запуск Бота"
        ),
        BotCommand(
            command="help",
            description="Помощь"
        )
    ]

    await bot.set_my_commands(commands, BotCommandScopeDefault())
