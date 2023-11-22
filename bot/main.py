from telegram.ext import CommandHandler, MessageHandler, Application, CallbackContext, CallbackQueryHandler
from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
import logging
import config
import handlers


def main():
    # Включаем логирование
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.DEBUG)
    logger = logging.getLogger(__name__)

    # Создаем Application и передаем ему токен вашего бота
    application = Application.builder().token(config.TOKEN).build()

    # Регистрируем команды
    application.add_handler(CommandHandler("start", handlers.start))
    application.add_handler(CommandHandler("help", handlers.help))
    application.add_handler(CommandHandler("schedule", handlers.schedule))
    application.add_handler(
        CallbackQueryHandler(handlers.handle_schedule_choice, pattern='^(create_schedule|show_schedule)$'))

    # Регистрируем обработчик для текстовых сообщений (без команд)
    application.add_handler(MessageHandler(None, handle_text_message))

    # Запускаем бота
    application.run_polling()


def handle_text_message(update: Update, context: CallbackContext):
    # Создайте кнопку "Меню"
    menu_button = KeyboardButton("Меню")

    # Создайте клавиатуру с кнопкой "Меню"
    menu_keyboard = ReplyKeyboardMarkup([[menu_button]], resize_keyboard=True, one_time_keyboard=True)

    # Отправьте клавиатуру с кнопкой "Меню" пользователю
    update.message.reply_text("Выберите опцию:", reply_markup=menu_keyboard)


if __name__ == '__main__':
    main()
