class Time:
    """Represents time of a day.
    
    Attributes: hour, minute, second.
    """


def print_time(time):
    print("%.2d : %.2d : %.2d" % (time.hour, time.minute, time.second))


def is_after(time1, time2):
    total_second1 = time1.hour * 3600 + time1.minute * 60 + time1.second
    total_second2 = time2.hour * 3600 + time2.minute * 60 + time2.second

    return total_second1 > total_second2


def add_time(time1, time2):
    res = Time()
    res.hour = time1.hour + time2.hour
    res.minute = time1.minute + time2.minute
    res.second = time1.second + time2.second

    res.minute += (res.second // 60)
    res.second %= 60

    res.hour += int(res.minute // 60)
    res.minute %= 60
    

    return res

def is_same_time(time1, time2):
    return (time1.hour == time2.hour and time1.minute == time2.minute and time1.second == time2.second)




movie_start = Time()
movie_start.hour = 9
movie_start.minute = 45
movie_start.second = 0

print_time(movie_start)


movie_end = Time()
movie_end.hour = 11
movie_end.minute = 20
movie_end.second = 0

print_time(movie_end)

print(is_after(movie_end, movie_start))

movie_duration = Time()
movie_duration.hour = 1
movie_duration.minute = 35
movie_duration.second = 0


calculated_movie_end = add_time(movie_start, movie_duration)
print_time(calculated_movie_end)

print(is_same_time(calculated_movie_end, movie_end))