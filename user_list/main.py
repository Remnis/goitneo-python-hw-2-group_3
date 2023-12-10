from datetime import datetime

WEEK_DAYS_BY_NUMBERS = {
    0: 'Monday',
    1: 'Tuesday',
    2: 'Wednesday',
    3: 'Thursday',
    4: 'Friday',
    5: 'Saturday',
    6: 'Sunday'
}


def show_birthdays_per_week(birthdays):
    for key, value in birthdays.items():
        print(f"{key}: {', '.join(value)}")


def get_birthdays_per_week(users):
    today = datetime.today().date()

    next_week_birthdays_by_weekday = {
        'Monday': [],
        'Tuesday': [],
        'Wednesday': [],
        'Thursday': [],
        'Friday': [],
        'Saturday': [],
        'Sunday': [],
    }

    for user in users:
        name = user['name']
        birthday = user['birthday'].date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        delta_days = (birthday_this_year - today).days

        if delta_days < 7:
            birthday_week_day = birthday_this_year.weekday()

            if birthday_week_day in [5, 6]:
                next_week_birthdays_by_weekday['Monday'].append(name)
            elif birthday_week_day < 5:
                weekday_name = WEEK_DAYS_BY_NUMBERS[birthday_week_day]
                next_week_birthdays_by_weekday[weekday_name].append(name)

    show_birthdays_per_week(next_week_birthdays_by_weekday)


# Dummy data
users = [
    {'name': 'Bill Gates', 'birthday': datetime(1955, 10, 28)},
    {'name': 'Jon Doe', 'birthday': datetime(1978, 12, 8)},
    {'name': 'Jane Doe', 'birthday': datetime(1988, 12, 8)}
]

get_birthdays_per_week(users)
