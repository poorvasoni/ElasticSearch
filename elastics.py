from flask import Flask
from flask_restful import Resource, Api
from flask_restful import reqparse
from flask import request
from datetime import datetime
from elasticsearch import Elasticsearch

app = Flask(__name__)
api = Api(app)

class CreateUser(Resource):
	def post(self):
		try:
			arg = request.get_json(force =True)
			print(arg)
			es = Elasticsearch()

			doc = {
			    'author': 'kimchy',
			    'text': 'Elasticsearch: cool. bonsai cool.',
			    'timestamp': datetime.now(),
			}
			res = es.index(index="test-index", doc_type='tweet', id=1, body=doc)
			print(res['created'])

			res = es.get(index="test-index", doc_type='tweet', id=1)
			print(res['_source'])

			es.indices.refresh(index="test-index")

			res = es.search(index="test-index", body={"query": {"match_all": {}}})
			print("Got %d Hits:" % res['hits']['total'])
			for hit in res['hits']['hits']:
			    print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])       
            # Parse the arguments
            # parser = reqparse.RequestParser()
            # parser.add_argument('email', type=str, help='Email address to create user')
            # parser.add_argument('password', type=str, help='Password to create user')
            # args = parser.parse_args()
            
            

		except Exception as e:
			return {'error': str(e)}

api.add_resource(CreateUser)




if __name__ == '__main__':
	app.run(debug=True)


