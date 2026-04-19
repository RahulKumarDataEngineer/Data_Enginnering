from loguru import logger

labour_name = ["Mahesh","Mithilesh","Sumesh"]

logger.info(f"first element in the list is {labour_name[0]}")
logger.info(f"last element in the list is {labour_name[-1]}")

# append , extend , insert

# append add one item at the end of the list
labour_name.append('Ram')
logger.info(labour_name)

new_labours = ["Raj","kumar"]
labour_name.extend(new_labours)

logger.info(f"labours after adding new labours {labour_name}")