from datetime import datetime, timedelta

def generate_reminder_date(expiration_date: datetime, days_before_reminder: int):  

    if days_before_reminder <= 0:
        return [expiration_date]

    difference = days_before_reminder
    dates = []

    while difference > 0:
        if difference >= 60:
            step = 30
        elif difference >= 30:
            step = 14
        else:
            step = difference

        reminder_date = expiration_date - timedelta(days=difference)
        if reminder_date >= datetime.now().date():
            dates.append(reminder_date)

        difference -= step

    dates.append(expiration_date)
    return dates