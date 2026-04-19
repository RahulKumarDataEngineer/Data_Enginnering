from loguru import logger

length_of_land = 100
breadth_of_land = 200

# if length_of_land == 100:
#     length_of_land = 400
# else:
#     length_of_land = 300
# print(length_of_land) 

# for new line use \n
print("my home is of 4 bhk \nlength of land is 100")

# for multiline string use triple quote '''
print('''my home is of "4 bhk"
length of land is 100''')

# backslash  "\" use to escape next character ahead of backslash
print("my home is of \"4 bhk\" length of land is 100")

# about f string 
print(f'''length of land is {length_of_land}
breadth of land is {breadth_of_land}''')
# logging
logger.info(f'''length of land is {length_of_land}
breadth of land is {breadth_of_land}''')
