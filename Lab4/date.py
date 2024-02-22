#TASK 1
from datetime import datetime, timedelta
x = datetime.now() - timedelta(days=5)
print(x.strftime("%Y-%m-%d"))
#TASK 2
print("Today:", datetime.now.strftime("%Y-%m-%d"))
print("Tomorrow:", (datetime.now + timedelta(days=1)).strftime("%Y-%m-%d"))
print("Yesterday:", (datetime.now - timedelta(days=1)).strftime("%Y-%m-%d"))
#TASK 3
x = datetime.now().replace(microsecond=0)
print(x)
#TASK 4
firstdate = datetime(2011, 9, 11, 9, 4, 3)
seconddate = datetime(2024, 2, 23, 4, 5, 3)
print("Seconds:", abs((seconddate - firstdate).total_seconds()))