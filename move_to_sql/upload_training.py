from methods import Methods
import pandas as pd
from os import listdir


# Constants
ORIGIN_FOLDER = '../origin/'
TRAINING_DATA_FOLDER = ORIGIN_FOLDER + 'TrainingData/'
LOW_LIMIT = 0

# Read File List
fileList = listdir(TRAINING_DATA_FOLDER)
UP_LIMIT = len(fileList)

# loop on list
print("Staring to loop on " + str(UP_LIMIT - LOW_LIMIT))
for fileIndex in range(LOW_LIMIT,UP_LIMIT):
	fileName = fileList[fileIndex]
	print('Started uploading  ' + fileName)
	methods = Methods('../_mysql_config.json')
	methods.loadDataJsonFormatIntoDB(TRAINING_DATA_FOLDER + fileName, "TrainingData", "training_data", "append")
	print('Done uploading ' + fileName)
