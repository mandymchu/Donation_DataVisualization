## Donation_DataVisualization
Developed a dashboard that represents school donations broken down by five attributes, which are donation date, location, resource type, poverty level and total number of donations, using data from DonorsChoose.org. 

•	Perform data cleaning, transformation and dimension reduction using Principal component analysis (PCA), feature selection using MongoDB and Python.

•	Build a webserver using Python, Flask and use MongoDB as backend database.

•	Perform grouping, filtering, aggregating data using crossfilter.js, and develop interactive charts using d3.js and dc.js. 


Problem:

On the page http://localhost:5000/donorschoose/projects projects data could be printed out. However, on the page http://localhost:5000/, only could see a dashboard with empty charts. The problem should be in the amount of data being loaded. 

Solution:
1. In charts.js, using:
   var dateFormat = d3.time.format("%Y-%m-%d %H:%M:%S");
2. Press CTRL+Shift+R for reloading the page, ignoring cache. 



