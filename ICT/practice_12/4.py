from datetime import datetime

year = int(input('Which year: '))
month = int(input('Which month: '))
day = int(input('Which day: '))

date = datetime(year, month, day)
print(f'It was {date.strftime("%A")}')