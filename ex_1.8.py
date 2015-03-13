'''
Exercise 1.8 if you run a 10km race in 43 minutes and 30 seconds, what is your
average time per mile. what is your average speed in mile per hour.
There are 1.61 km in a mile. 
'''

distance_in_km = 10
time_in_min = 43+(30.0/60)
distance_in_miles = distance_in_km/1.61
time_in_hrs=time_in_min/60

avg_time_per_mile=time_in_hrs/distance_in_miles
avg_speed = distance_in_miles/time_in_hrs

print("avg time per mile " + str(avg_time_per_mile))
print("avg speed " + str(avg_speed) )
print("distance in miles " + str(distance_in_miles))
