from datetime import datetime

class Time:
    def c_hour():
        c_time = datetime.now()
        c_hour = c_time.hour
        return c_hour
    
    def c_time():
        c_time = datetime.now()
        c_hour = c_time.hour
        c_min = c_time.minute
        return f"{c_hour}:{c_min}"
    
    def bday_dist():
        c_year = datetime.now().year
        birthday = datetime(c_year, 6, 7, 22, 10, 45) # Should be in UTC
        cur_date = datetime.now() # Time in UTC
        if cur_date.date() > birthday.date():
            birthday = datetime(c_year+1, 6, 7, 22, 10, 45) 
        elapsed_time = birthday - cur_date
        return elapsed_time.days
    
print(Time.bday_dist())
    