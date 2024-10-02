from aiogram.utils.keyboard import InlineKeyboardBuilder 


def services_keyboard_builder(products: list):
    builder = InlineKeyboardBuilder()

    for product in products:
        builder.button(text=product, callback_data=f"patient_{product}")

    builder.adjust(3)
    return builder.as_markup()


def service_actions_keyboards(product: str):
    builder = InlineKeyboardBuilder()
    builder.button(text="Вилікувати тваринку", callback_data=f"cured_animal_{product}")
    builder.button(text="Видалити тваринку", callback_data=f"delete_animal_{product}")
    return builder.as_markup()