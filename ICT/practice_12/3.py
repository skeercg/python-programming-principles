from datetime import datetime

current_time = datetime.now()
print(f'Hello, today is the {current_time.date()} and it\'s {current_time.time()}')