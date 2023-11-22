from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext, CommandHandler, CallbackQueryHandler
from telegram_bot_calendar import DetailedTelegramCalendar, LSTEP
from keyboard import get_main_keyboard

async def start(update: Update, context: CallbackContext):
    welcome_message = "Привет!＼ʕ •ᴥ•ʔ／ \nЯ бот, который упростит тренеру жизнь.\nЯ могу помочь тебе с составлением расписания 🗓️ занятий на неделю. Кроме того, иногда я буду высылать интерсные оповещения! 🚀"
    await update.message.reply_text(welcome_message)

async def help(update: Update, context: CallbackContext):
    help_message = "Доступные команды:\n/start - начать диалог с ботом\n/schedule - получить расписание занятий\n/calendar - выбрать дату\n/help - получить информацию о командах"
    await update.message.reply_text(help_message)



async def schedule(update: Update, context: CallbackContext):
    keyboard = get_main_keyboard()
    await update.message.reply_text('Выберите опцию:', reply_markup=keyboard)

async def handle_schedule_choice(update: Update, context: CallbackContext):
    query = update.callback_query
    await query.answer()

    if query.data == 'create_schedule':
        calendar, step = DetailedTelegramCalendar().build()
        await query.message.reply_text(f"Выберите дату:", reply_markup=calendar)
    elif query.data == 'show_schedule':
        await query.message.reply_text("Здесь будет отображаться текущее расписание.")

