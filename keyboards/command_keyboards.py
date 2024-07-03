from aiogram.utils.keyboard import ReplyKeyboardBuilder

class ButtonText:

    JOKE='🤣 Расскажи анекдот'
    FACT='📜 Поведай интересный факт'
    PHRASE='💭 Поделись мудростью'
    WOMAN='👩 Сделай комплимент женщине'
    MAN='👨 Сделай комплимент мужчине'
    MEM='🖼️ Покажи какой-нибудь мем'

def ActionKeyboards():
    builder=ReplyKeyboardBuilder()
    builder.button(text=ButtonText.JOKE,)
    builder.button(text=ButtonText.FACT,)
    builder.button(text=ButtonText.PHRASE,)
    builder.button(text=ButtonText.WOMAN,)
    builder.button(text=ButtonText.MAN,)
    builder.button(text=ButtonText.MEM,)
    builder.adjust(1)
    return builder.as_markup()