from datetime import date, timedelta

start_date = date.today()
end_date = start_date + timedelta(7)

def get_period(start_date: date, days: int):
    result = {}
    for _ in range(days + 1):
        result[start_date.day, start_date.month] = start_date.year
        start_date += timedelta(1)
    return result

def get_bd(users: list) -> list:
    start_date = date(2023, 12, 29)
    period = get_period(start_date, 7)

    for user in users:
        bd: date = user["birthday"]
        date_bd = (bd.day, bd.month)
        if date_bd in list(period):
            print(user["name"])
            print(period[date_bd])
        
if __name__ == "__main__":
    users = [{"name": "Bill", "birthday": date(1990, 12, 30)},
             {"name": "Marry", "birthday": date(2000, 1, 2)},
             ]
    
    get_bd(users)

    #print(get_period(date(2023, 12, 29), 7))