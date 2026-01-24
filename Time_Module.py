import time

# converts a time expressed in seconds since epoch to a string representing local time
print(time.ctime(0))
# epoch = when your computer thinks time began (Wed Dec 31 16:00:00 1969 for my computer)

# returns the current time in seconds since epoch as a floating point number
print(time.time())
# converts the current time in seconds since epoch to a string representing local time
print(time.ctime(time.time()))

# converts seconds since epoch to a struct_time in local time
time_object = time.localtime()
print(time_object)
# formats a struct_time as a string
local_time = time.strftime("%Y-%m-%d %H:%M:%S", time_object)
# docs.python.org/3/library/time.html for more formatting options
print(local_time)

# year, month, day, hour, minute, second, weekday, yearday, DST
time_tuple = (2024, 6, 1, 12, 0, 0, 0, 0, 0)
# converts a struct_time or tuple representing time to a string
time.asctime(time_tuple)
print(time.asctime(time_tuple))

# year, month, day, hour, minute, second, weekday, yearday, DST
time_tuple = (2024, 6, 1, 12, 0, 0, 0, 0, 0)
# converts a struct_time or tuple representing local time to seconds since epoch
time.mktime(time_tuple)
print(time.asctime(time_tuple))
