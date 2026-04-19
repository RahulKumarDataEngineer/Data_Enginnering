import math
from loguru import logger

length_of_land = 100
breadth_of_land = 100
bricks_cost_per_piece =10.5
labour_mistri_1 = "Jagmohan"
labour_mistri_2 = "Rampyare"
is_home = True

# length_of_land = int(input("enter the length of your land:"))

# if length_of_land < 100:
#     logger.info(f"your length is not sufficient to build 4BHK")
#     if length_of_land >80:
#         logger.info("You can build 3 BHK House")
#     else:
#         logger.info("Your land is not having enough space")    
# elif length_of_land > 500:
#     logger.info(f"You can build two buildings")    
# else:
#     logger.info("Share more details with us")

# How will u find out given no is even or odd

number_1 = input("Enter one number to check if it is odd or even:" )  #here data type ofinput is str
data_type_of_number1 = type(number_1)
print(data_type_of_number1)
number_2 = input()                                #here also input data type is str
data_type_of_number2 = type(number_2)
print(data_type_of_number2)

# so we need to convert str into int
number_2 = int(number_2)
data_type_of_number2=type(number_2)

sample_int = 1
sample_data_type = type(sample_int)
if (data_type_of_number2 == sample_data_type):
    result = int(number_2) % 2
    if result == 0:
        logger.info(f"{number_2} is even number")
    else:
        logger.info(f"{number_2} is odd number")    
else:
    logger.info(f"{number_1} is not a valid data type for checking even odd")