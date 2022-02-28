import datetime

print(f'Yesterday: {datetime.datetime.now() - datetime.timedelta(1)}')
print(f'Today: {datetime.datetime.now()}')
print(f'Tomorrow: {datetime.datetime.now() + datetime.timedelta(5)}')