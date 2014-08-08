'''
Script for inserting the records in the DB
'''
import os
import csv

from pymongo import MongoClient

client = MongoClient('mongodb://karang19:Karang19@ds029187.mongolab.com:29187/heroku_app28139663')

db = client.heroku_app28139663
movielocations = db.movielocations
 
def readMyFiles(filename):
    with open(filename, 'r') as csvfile:
        csvfile.seek(0)
        #read the CSV file into a dictionary
        dictReader = csv.DictReader(csvfile)
        for row in dictReader:
            #do your processing here
            movielocations.insert(row)                     
    return
 
 
if __name__ == '__main__':
    readMyFiles('Film_Locations_in_San_Francisco.csv')