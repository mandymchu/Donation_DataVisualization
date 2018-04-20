## Donation_DataVisualization
In this project, a dataset from DonorsChoose.org is used to build an interactive data visualization that represents school donations broken down by different attributes.

MongoDB, Python, JavaScript, Flask, D3.js, DC.js will be used.

Problem:

On the page http://localhost:5000/donorschoose/projects projects data could be printed out. However, on the page http://localhost:5000/, only could see a dashboard with empty charts. The problem should be in the amount of data being loaded. 

Solution:
1. In charts.js, using:
   var dateFormat = d3.time.format("%Y-%m-%d %H:%M:%S");
2. Press CTRL+Shift+R for reloading the page, ignoring cache. 



