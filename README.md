# yelp_datapull

There are two stages to this project. The first stage found in the root directory was an exercise in pulling the data from the Yelp pages and exporting them to an Excel spreadsheet for simple, manual analysis.

The second stage to this project was utilizing Google Cloud API to automate the sentiment analysis, and then outputting that result to Excel for even more detailed analysis. This is found in the 'sentiment analysis' folder, and is where the main functional Python file, datapullSentiment.py is found.

# Instructions for use
1. Open datapullSentiment.py with a text editor
2. Assign the mainUrl variable with the Yelp link
3. Adjust the number of pages to scan
4. Assign the output directory and filename
5. Open the Terminal and locate the directory the file is stored in
6. Run `python3 datapullSentiment.py` and wait for the program to complete
7. Locate output file in chosen directory
