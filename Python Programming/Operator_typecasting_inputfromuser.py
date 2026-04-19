import math
from loguru import logger

# Floor divission & cieling division 
# a=4
# b=17
# print(b/a)
# print(b//a)  #floor division //
# print(math.ceil(b/a))
# print(math.floor(b/a))

# take input from user 
# use input() function to take input from user

length_land = input("Please enter the length of your land:")
breadth_land = input("Please enter the breadth of land:")
total_area_of_your_land = float(length_land) * float(breadth_land)
logger.info(f"Total area of your land is {total_area_of_your_land} sq ft")
