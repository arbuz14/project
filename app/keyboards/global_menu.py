from aiogram.utils.keyboard import ReplyKeyboardBuilder


def global_menu_keyboard_builder():
    builder = ReplyKeyboardBuilder()
    builder.button(text="Показати всіх пацієнтів")
    builder.button(text="Виберіть пацієнта")
    builder.button(text="Додати новий товар")
    builder.button(text="Показати всі відгуки")
    builder.button(text="Додати новий відгук")
    builder.adjust(1)
    return builder.as_markup()