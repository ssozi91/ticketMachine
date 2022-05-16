# This is a ticketing system for theme park
import calendar
import datetime
import pytz


month = datetime.date.today().month
year = datetime.date.today().year

print('**************************************************')
print('**************************************************')

print('........WELCOME TO ADVENTURE THEME PARK ......')

print('**************************************************')

print('....When do you want to visit the theme park....')

print (f'{calendar.month(year,month)}')

today = datetime.date.today()
d1 = today.strftime("%d/%m/%Y")

tz_London = pytz.timezone('Europe/London')
datetime_London = datetime.datetime.now(tz_London)
current_time = datetime_London.strftime("%H:%M:%S")

print(f"Today's date: {d1} and time : {current_time}")

print('**************************************************')

while True:
    day_of_ticket = input("When would you want to attend the park? (in DD/MM/YYYY)\n: ")
    
    try:
        dayOfTicket = datetime.datetime.strptime(day_of_ticket,"%d/%m/%Y").date()
        days = dayOfTicket - today
    except ValueError:
        print(f"date entered {day_of_ticket} does not match format DD/MM/YYYY) please try again")
    else:
        if days.days < 0:
            print(f"the date entered {day_of_ticket} is in past please enter today's or future date")
        else:
            break
 
 
 
 

# if days.days < 0:
#     print(f"the date entered {day_of_ticket} is in past please enter today's or future date")
# print(dayOfTicket)

print(days.days)