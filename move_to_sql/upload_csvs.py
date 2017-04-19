from methods import Methods
import pandas as pd

# Constants
ORIGIN_FOLDER = '../origin/'

# Load methods
methods = Methods('../_mysql_config.json')

# Load topics
topics = pd.read_csv(ORIGIN_FOLDER + 'topicDictionary.csv',header=None)
topics.columns = ['topic']
topics.to_sql('topics', methods.mysql_engine, if_exists='replace',index=False)

# Load sampleSubmission
sampleSubmission = pd.read_csv(ORIGIN_FOLDER + 'sampleSubmission.csv')
sampleSubmission.to_sql('sample_submission', methods.mysql_engine, if_exists='replace',index=False)
