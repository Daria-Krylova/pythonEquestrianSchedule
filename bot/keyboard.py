from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def get_main_keyboard():
    # Создаем основную клавиатуру для команды /start
    keyboard = [
        [InlineKeyboardButton("Составить расписание", callback_data='create_schedule')],
        [InlineKeyboardButton("Показать расписание", callback_data='show_schedule')],
    ]
    return InlineKeyboardMarkup(keyboard)

def get_schedule_type_keyboard():
    # Клавиатура для выбора "Тренер" или "Ученик" при нажатии на /schedule
    keyboard = [
        [InlineKeyboardButton("Тренер", callback_data='trainer_schedule')],
        [InlineKeyboardButton("Ученик", callback_data='student_schedule')],
    ]
    return InlineKeyboardMarkup(keyboard)

def get_weekday_keyboard():
    # Создаем клавиатуру для выбора дня недели
    weekdays = ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"]
    keyboard = [
        [InlineKeyboardButton(weekday, callback_data=f'select_weekday_{weekday}')]
        for weekday in weekdays
    ]
    return InlineKeyboardMarkup(keyboard)

def get_time_slots_keyboard():
    # Создаем клавиатуру для выбора времени
    time_slots = ["12:00", "14:00", "16:00", "18:00", "20:00"]
    keyboard = [
        [InlineKeyboardButton(time_slot, callback_data=f'select_time_{time_slot}')]
        for time_slot in time_slots
    ]
    return InlineKeyboardMarkup(keyboard)
