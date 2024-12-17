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
        birthday = datetime(2024, 11, 12, 6, 1, 0) # Should be in UTC
        cur_date = datetime.now() # Time in UTC
        elapsed_time = cur_date - birthday
        return elapsed_time.days
    