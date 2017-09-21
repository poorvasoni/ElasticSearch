import pymssql
import csv
import base64
import requests
from datetime import datetime
from elasticsearch import Elasticsearch
import json
from elasticsearch import Elasticsearch
from elasticsearch.client import IndicesClient
from elasticsearch.client import IngestClient



conn = pymssql.connect(
	server = "40.71.86.193",
		port= 1433,
		user="sa",
		password="mssql@123",
		database="testCaseFinal")

cursor = conn.cursor()

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
es_index = IndicesClient(es)
ex_indices = IngestClient(es)


table_name = 'Attachment_sfdc'
query = "SELECT  Body FROM Attachment_sfdc " 
var = cursor.execute(query)
data_tup_list = cursor.fetchall()
#print(data_tup_list)

r = requests.get('http://localhost:9200') 
i = 1
if r.status_code == 200 :
	'''
	doc1 = {

			"description" : "Extract attachment information from arrays",
			  "processors" : [
			    {
			      "foreach": {
			        "field": "attachments",
			        "processor": {
			          "attachment": {
			            "target_field": "_ingest._value.attachment",
			            "field": "_ingest._value.data"
			          }
			        }
			      }
			    }
			  ]

	}

	val=ex_indices.put_pipeline(id="attach",body=doc1)
	print(val)


	
	i=0
	while i<17:
		strvalue = str(data_tup_list[i])
		doc = {
				"attachments" : [
	    
	  
	  
	    {
	      "filename" : "test.pdf",
	      "data":''.join(data_tup_list[0])
	    }
	    ]
	    }
		res = es.index(index="test-index0", doc_type='tweet', id=i, body=doc , pipeline = 'attach')
		print(res['created'])
		print(res)
		i=i+1
		'''
	doc3 = {
			"size":5,
			"query": {
			"query_string": {
			"query": "Dangal"
			}
			}
			}


	res = es.search(index="test-index0", doc_type = 'tweet', body= doc3)
	j=0
	resultlist=res['hits']['hits']
	if(resultlist!=[]):
		while j<5:
		
			resultdict=resultlist[j]['_source']

			reslist = resultdict['attachments']

			resdict=reslist[0]['attachment']

			finalval=resdict['content']

			j=j+1


			new_path = '/home/poorva/Desktop/myfirstapi/file{}.txt'.format(j)
			new_days = open(new_path,'w')
			new_days.write(finalval)
	else:
		print("No match Found")

	








