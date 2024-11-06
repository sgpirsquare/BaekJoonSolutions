from datetime import datetime

utc_now = datetime.utcnow()
seoul_time = utc_now.replace(hour=(utc_now.hour + 9) % 24)

print(seoul_time.year)
print(seoul_time.month)
print(seoul_time.day)