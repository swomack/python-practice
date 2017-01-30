class Time:
    """Represents time of a day.
    
    Attributes: hour, minute, second.
    """


def print_time(time):
    print("%.2d : %.2d : %.2d" % (time.hour, time.minute, time.minute))


def is_after(time1, time2):
    total_second1 = time1.hour * 3600 + time1.minute * 60 + time1.second
    total_second2 = time2.hour * 3600 + time2.minute * 60 + time2.second

    return total_second1 > total_second2



time1 = Time()
time1.hour = 12
time1.minute = 20
time1.second = 35

print_time(time1)


time2 = Time()
time2.hour = 13
time2.minute = 20
time2.second = 35

print_time(time2)



print(is_after(time1, time2))