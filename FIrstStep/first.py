import datetime
import pymssql
import csv
import base64
import requests
import base64
import json

conn = pymssql.connect(
	server = "40.71.86.193",
		port= 1433,
		user="sa",
		password="mssql@123",
		database="testCaseFinal")

cursor = conn.cursor()

table_name = 'Attachment_sfdc'
query = "SELECT  Body,name FROM Attachment_sfdc " 
var = cursor.execute(query)
data_tup_list = cursor.fetchall()
#print(data_tup_list[0])
value = str(data_tup_list[0])
#print(type(value)) 
print(''.join(data_tup_list[0][1]))
import json



