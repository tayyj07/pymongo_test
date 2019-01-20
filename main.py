import pymongo
from pprint import pprint

user = 'tayyjadmin'
password = '123qweASD'
database = 'tayyj_test'
connection_end = 'tayyjtest-shard-00-00-tlyzm.mongodb.net:27017,tayyjtest-shard-00-01-tlyzm.mongodb.net:27017,tayyjtest-shard-00-02-tlyzm.mongodb.net:27017/test?ssl=true&replicaSet=tayyjtest-shard-0&authSource=admin&retryWrites=true'

client = pymongo.MongoClient("mongodb://{0}:{1}@{2}".format(user, password, connection_end))
db = client[database]
db_collection = db.testing

pprint(client.list_database_names())