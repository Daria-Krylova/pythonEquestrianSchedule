from telegram import Update
from telegram.ext import CallbackContext
import datetime
from apscheduler.schedulers.asyncio import AsyncIOScheduler

# Функция для отправки поздравления с Новым Годом
async def send_new_year_greeting(context: CallbackContext):
    # Определяем текущую дату
    today = datetime.date.today()

    # Проверяем, если сегодня 31 декабря 2023 года, то отправляем поздравление
    if today == datetime.date(2023, 12, 31):
        greeting_message = "С наступающим Новым Годом! 🎉🎄 Пусть новый год принесет вам много счастья, радости и удачи!Конникам желаю больших побед, теплых взаимоотношений с конем и всегда радовать тренера!"

        # Отправляем поздравление всем пользователям
        for user_id in context.bot_data.get("user_ids", []):
            try:
                await context.bot.send_message(chat_id=user_id, text=greeting_message)
            except Exception as e:
                print(f"Ошибка при отправке поздравления пользователю {user_id}: {str(e)}")


# Функция для добавления пользователей, которым нужно отправить поздравление
def add_user_for_new_year_greeting(user_id: int, context: CallbackContext):
    user_ids = context.bot_data.get("user_ids", [])
    if user_id not in user_ids:
        user_ids.append(user_id)
        context.bot_data["user_ids"] = user_ids

# Создаем планировщик
scheduler = AsyncIOScheduler()

# Настройка выполнения функции в полночь каждый день
scheduler.add_job(send_new_year_greeting, "cron", day="31", month="12", year="2023", hour="0", minute="0", second="0")

# Запускаем планировщик
scheduler.start()