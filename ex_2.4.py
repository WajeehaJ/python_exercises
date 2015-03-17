
# -*- coding: utf-8 -*-
"""
Exercise 2.4:1. The volume of a sphere with radius r is 4/3 π r3.
What is the volume of a sphere with radius 5? Hint: 392.7 is wrong!
2. Suppose the cover price of a book is $24.95, but bookstores get
a 40% discount. Shipping costs $3 for the first copy and 75 cents for
each additional copy. What is the total wholesale cost for 60 copies?
3. If I leave my house at 6:52 am and run 1 mile at an easy pace
(8:15 per mile), then 3 miles at tempo (7:12 per mile)
and 1 mile at easy pace again, what time do I get home for breakfast?
"""

from  math import pi

#Calculation for the volume of the sphere
print "4.0/3 * pi *r3 = " + str((4.0/3)*pi*(5**3))

#Cover price including the discount for the 60 books
cover_price_discnt_incl = (24.95-(24.95*40)/100) *60

#Shipping price of the first book
first_copy_price = 3

#Shiping price of the remaining 59 books
rst_copies_price = (75.0/100)*59

#Summing up the shipping price and the cover price
total_book_price = cover_price_discnt_incl + first_copy_price + rst_copies_price

print "Total book price = " + str(total_book_price)


#Seconds, Minutes and Hours Conversion
SECS = 1
MINS = 60
HRS = 60*MINS

#start time from the house
start_time = (6*HRS+52*MINS)

easy_pace_time = (8*MINS+15*SECS)*2

fast_pace_time = (7*MINS+12*SECS)*3

total_time_in_sec = start_time + easy_pace_time + fast_pace_time

# use // for floor division
#Extracting hours, minutes and seconds.
hours = total_time_in_sec // HRS
remaining_time = total_time_in_sec % HRS
minutes = remaining_time// MINS
secs = remaining_time%MINS

print "Total time in hours:min:sec " + str(hours) + ":" + str(minutes) + ":" +str(secs)
