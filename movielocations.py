from flask import Flask, request, Response, render_template, jsonify

app = Flask(__name__)

import os
import re
import json
from pymongo import MongoClient
from sets import Set

# Connecting to MongoDB
client = MongoClient('mongodb://karang19:Karang19@ds029187.mongolab.com:29187/heroku_app28139663')

# Selecting the database
db = client.heroku_app28139663

#Getting the required collection
locations = db.movielocations

# The following function is used for predictive search
@app.route('/n_autocomplete',methods=['GET'])
def autocomplete():
	if request.method == 'GET':
		search = request.args.get('term')
		
		#Invoking the regex engine
		regr = ".*" + search + ".*"
		regx = re.compile(regr, re.IGNORECASE)

		#Querying the collection
		movie_collection = locations.find({'Title': regx})
		
		# The dict object that needs to be returned
		movie_json = {}
		movie_list = []
		
		# Using Set for getting distinct values
		movie_set = Set([])
		
		# Adding movie titles to the set
		for doc in movie_collection:
			movie_set.add(str(doc['Title']))
		
		# Adding the distinct movie titles to a list
		for temp in movie_set:
			movie_list.append(temp)
		
		movie_json['Title'] = movie_list
		
		return jsonify(movie_json)



# Returning the shooting locations for the movie titles
@app.route('/plot_locations', methods=['POST'])
def plot_locations():
	# Retrieving the movie title selected by the user
	title = request.form['topic_title']
	
	#Getting the locations for a particular movie title
	location_collection = locations.find({'Title': title})
	
    # The list that needs to be returned for maps marker
	location_list = []

	for doc in location_collection:
		location_list.append(str(doc['Locations'].encode('ascii', 'ignore') + ' San Francisco, CA')) 
	
	#Checking if the movie exists in the database
	if not location_list:
		return "Sorry! This movie wasn't shot in San Francisco"

	return render_template("index.html", data=location_list)



# Homepage
@app.route('/')
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
