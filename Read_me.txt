Project: SF Movies

Technical Track: Full stack since that's what I have been doing for the past 6 months. 

How to use the web application:
1.Go to the url: https://movielocations.herokuapp.com/.
2.Type a movie name in the search bar. Type atleast 2 characters to get movie suggestions.
3.Choose a movie from the list and hit Enter.
4.For the movie choosen, markers will be placed on the map indicating where the movie was filmed.
5.Click on the marker to get the address. 

E.g: Type 'Ex'
The autocomplete feature would give the option 'Experiment in Terror'
Select the option and hit Enter 

Things I would have done differently:
1. For the movies that are not in the database, the current app directs the user to the 
following message, "Sorry! This movie wasn't shot in San Francisco". 
What I really wanted to do: Show the message on the same page and along with the search bar so that the user
can search again
2. The geocoder times out when the locations are more than 15. Gives QUERY_OVER_LIMIT error. Would wanna fix that.
3. Would make the web page more appealing. 
