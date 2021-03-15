import requests
from datetime import datetime
import pymongo
from area_data import area_data

client = pymongo.MongoClient()
coll = client.mask.pharmacy
log = open('/root/code/mask_backend/log.txt', 'a')

try:
	r = requests.get('https://data.nhi.gov.tw/Datasets/Download.ashx?rid=A21030000I-D50001-001&l=https://data.nhi.gov.tw/resource/mask/maskdata.csv', timeout = 5)
except:
	log.write('requests fail at ' + datetime.now().isoformat() + '\n')
	log.close()

pharmacies = []
lines = r.text.split('\r\n')
lines = lines[1:-1]
for line in lines:
	row = line.split(',')
	coll.update_one({'code': row[0]}, {'$set': {'name': row[1], 'address': row[2], 'phone': row[3], 'adult': int(row[4]), 'child': int(row[5]), 'source_time': row[6]}}, upsert = True)

log.write('db update complete at ' + datetime.now().isoformat() + '\n')
log.close()
