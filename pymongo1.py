from pymongo import MongoClient

# Create the client
client = MongoClient('localhost', 27017)

# Connect to our database
db = client['SeriesDB']

# Fetch our series collection
series_collection = db['series']
new_show = {
    "name": "FRIENDS",
    "year": 1994
}

shows = [{
    "name": "HOUSE",
    "year": 1995
}, {
    "name": "CLINIC",
    "year": 1996
}]
#from pprint import pprint
#series_collection.insert_one(new_show)
#series_collection.insert_many(shows)
print(list(series_collection.find({'year' : {'$lte': 1995}})))