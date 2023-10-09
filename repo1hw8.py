from datetime import date, timedelta

def get_bd(users: list) -> list:
    start_date = date.today()
    end_date = start_date + timedelta(days=7) 
    birthday_dict = {}

    for user in users:
        bd = user["birthday"]
        current_year = start_date.year
        if start_date > bd.replace(year=current_year):
            bd = bd.replace(year=current_year+1)
        day_of_week = bd.strftime("%A")
       
        if start_date <= bd < end_date:
            if day_of_week not in ["Saturday", "Sunday"]:
                if day_of_week not in birthday_dict:
                    birthday_dict[day_of_week] = []
                birthday_dict[day_of_week].append(user["name"])
            else:
                next_monday = start_date + timedelta(days=(7 - start_date.weekday()))
                day_of_week = next_monday.strftime("%A")
                if day_of_week not in birthday_dict:
                    birthday_dict[day_of_week] = []
                birthday_dict[day_of_week].append(user["name"])

    return birthday_dict