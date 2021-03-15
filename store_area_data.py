import pymongo
from area_data import area_data

client = pymongo.MongoClient()
coll = client.mask.area

for county in area_data:
	coll.insert_one({'county': county, 'areas': area_data[county]})
