class Time(object):
    """Represents the time of day.

    attributes: hour, minute, second
    """

def increment(t, seconds):
    """Pure function that increments the time in seconds"""
    time = Time()
    time.hour, time.minute,time.second = (0,0,0)

    time.second = t.second + seconds


    minutes, time.second = divmod(time.second, 60)
    minutes += t.minute
    time.hour, time.minute = divmod(minutes, 60)
    time.hour += t.hour

    return time

def print_time(t):
    print '%.2d:%.2d:%.2d' % (t.hour, t.minute, t.second)


if __name__ == '__main__':
    time = Time()
    time.hour = 10
    time.minute = 12
    time.second = 30
    print_time(time)
    time = increment(time,50)
    print_time(time)


