import pandas as pd
import pymysql
from sqlalchemy import create_engine
import unidecode
import json

class Methods():
	def __init__(self, mysqlConfig='../_mysql_config.json'):
		MYSQL_CONFIG = json.load(open(mysqlConfig));
		self.mysql_engine = create_engine('mysql+pymysql://{user}:{password}@{host}:{port}/{dbname}'.format(
		    user=MYSQL_CONFIG['USER'],
		    password=MYSQL_CONFIG['PASSWORD'],
		    port=MYSQL_CONFIG['PORT'],
		    dbname=MYSQL_CONFIG['DATABASE'],
		    host=MYSQL_CONFIG['HOST']
		))

	def loadDataJsonFormatIntoDB(self, location, mainKey='TestData', tableName='test_data', if_exists='replace',chunksize=10):
	    with open(location) as data_file:
	        data = json.load(data_file)
	        return pd.DataFrame([
	            {
	                'id': dId,
	                'bodyText': unidecode.unidecode(data[mainKey][dId]['bodyText']),
	                'webPublicationDate': data[mainKey][dId]['webPublicationDate']
	            }
	            for dId in data[mainKey]
	        ]).to_sql(tableName, self.mysql_engine, if_exists=if_exists, index=False,chunksize=chunksize);
