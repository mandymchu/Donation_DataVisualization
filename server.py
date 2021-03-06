from flask import Flask
from flask import render_template
from pymongo import MongoClient
import json
from bson import json_util
from bson.json_util import dumps

# connect to mongoDB
MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017
DBS_NAME = 'donorschoose'
COLLECTION_NAME = 'projects'
FIELDS = {'school_state': True, 'resource_type': True, \
          'poverty_level': True, 'date_posted': True,  \
          'total_donations': True, '_id': False}

# use flask to build a server
app = Flask(__name__)

@app.route("/")
def test():
	return render_template("test.html")

@app.route("/donorschoose/projects")
def donorschoose_projects():
    connection = MongoClient(MONGODB_HOST, MONGODB_PORT)
    collection = connection[DBS_NAME][COLLECTION_NAME]
    # projects = collection.find(projection=FIELDS)
    projects = collection.find(projection=FIELDS, limit=500000)
    #projects = collection.find({}, FIELDS, limit=1)
    json_projects = []
    for project in projects:
        json_projects.append(project)
    json_projects = json.dumps(json_projects, default=json_util.default)
    connection.close()
    return json_projects

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5000, debug=True)

# start mongoDB and run server.py. 
# If on the page http://localhost:5000/ only could see a dashboard with empty charts, 
# press CTRL+Shift+R for reloading the page, ignoring cache.
