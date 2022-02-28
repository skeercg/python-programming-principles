import datetime
from random import randint

date_1 = datetime.datetime.now()
date_2 = datetime.datetime.now() - datetime.timedelta(randint(0, 10))
print((date_1 - date_2).total_seconds())