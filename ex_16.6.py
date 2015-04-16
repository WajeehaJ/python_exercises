"""

Exercise 16.6:

Write a function called mul_time that takes a Time object and a number and
returns a new Time object that contains the product of the original Time
and the number.
"""

class Time(object):
    """Represents the time of day.

    attributes: hour, minute, second
    """

def print_time(t):
    """
    function that display time %H:%M:%S
    """
    print '%.2d:%.2d:%.2d' % (t.hour, t.minute, t.second)


def time_to_int(time):
    """
    Function that converts the time to seconds.
    """
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds


def int_to_time(number):
    """
    function that converts the seconds to
    (hour : minute : second) time format
    """
    time = Time()
    minutes, time.second = divmod(number, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time


def valid_time(time):
    """
    Function that validates the time object
    """
    if time.hour < 0 or time.minute < 0 or time.second < 0:
        return False
    if time.minute >= 60 or time.second >= 60:
        return False
    return True

def mul_time(t, number):
    """
    Function that multiply the time object t
    with number and return the time object
    containing the product.
    """
    if not valid_time(t):
        raise ValueError('invalid Time object in mul_time')
    pace  =  time_to_int(t)  * number
    return int_to_time(pace)


if __name__ == '__main__':

    time = Time()
    time.hour = 10
    time.minute = 12
    time.second = 30
    print "Before multiplying: ",
    print_time(time)
    print "After multiplying: ",
    print_time( mul_time(time, 2 ))
