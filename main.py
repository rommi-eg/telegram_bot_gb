import asyncio
import logging
import config.config as config

from aiogram import Bot, Dispatcher, html, types, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from protection.token_reader import token
from aiogram.filters import CommandStart, Command
from aiogram.types import FSInputFile, URLInputFile
from plugins.plugin import ContentGeneration
from keyboards.command_keyboards import ButtonText, ActionKeyboards

dp = Dispatcher()

@dp.message(CommandStart())
async def handle_start(message: types.Message):
    bot_name = await message.bot.get_me()
    text=config.hello.format(
        
        html.bold(message.from_user.full_name),
        html.bold(bot_name.first_name),
        config.description

        )
    
    await message.answer_photo(

        caption=text,
        photo=FSInputFile(config.image),
        reply_markup=ActionKeyboards()

        )
    
@dp.message(Command('help'))
async def handle_help(message: types.Message):
    await message.answer(

        text=config.help

        )

@dp.message(F.text==ButtonText.JOKE)
@dp.message(Command('joke'))
async def joke_generation(message: types.Message):
    await message.answer(

        text=ContentGeneration(config.joke)

    )

@dp.message(F.text==ButtonText.FACT)
@dp.message(Command('fact'))
async def joke_generation(message: types.Message):
    await message.answer(

        text=ContentGeneration(config.fact)

    )

@dp.message(F.text==ButtonText.PHRASE)
@dp.message(Command('phrase'))
async def joke_generation(message: types.Message):
    await message.answer(

        text=ContentGeneration(config.phrase)

    )

@dp.message(F.text==ButtonText.WOMAN)
@dp.message(Command('woman'))
async def joke_generation(message: types.Message):
    await message.answer(

        text=ContentGeneration(config.woman)

    )

@dp.message(F.text==ButtonText.MAN)
@dp.message(Command('man'))
async def joke_generation(message: types.Message):
    await message.answer(

        text=ContentGeneration(config.man)

    )

@dp.message(F.text==ButtonText.MEM)
@dp.message(Command('mem'))
async def joke_generation(message: types.Message):
    await message.answer_photo(

        photo=URLInputFile(ContentGeneration())

    )

@dp.message(F.text.lower())
async def echo_message(message: types.Message):
    try:
        if 'анекдот' in message.text:
            await message.reply(

                ContentGeneration(config.joke)

                )
        elif 'факт' in message.text:
            await message.reply(

                ContentGeneration(config.fact)

                )
        elif 'мудрость' in message.text:
            await message.reply(

                ContentGeneration(config.phrase)

                )
        elif 'женщине' in message.text:
            await message.reply(

                ContentGeneration(config.woman)

                )
        elif 'мужчине' in message.text:
            await message.reply(

                ContentGeneration(config.man)

                )
        elif 'мем' in message.text:
            await message.answer_photo(

                photo = URLInputFile(ContentGeneration())
                
                )
        else:
            await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply(text='ERROR')

async def main():
    logging.basicConfig(level=logging.INFO)

    bot=Bot(

        token=token.bot_token.get_secret_value(),
        default=DefaultBotProperties(

            parse_mode=ParseMode.HTML
            
            )

        )
    
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())