CSV Scraper
Version 0.5.20151014
Tim Vannerson
tim@vannerson.com


This python script takes a volume of comma-separated-value (CSV) files and returns the maximum value of any requested headers for each file in a separate CSV file.

I created this after running an experiment that resulted in hundreds of CSV log files where each file was a record of various hardware monitors over a period of time. I was only concerned with the maximum value of each hardware monitor over the time scale and rather than manually calculate the maximum values in excel for each file, I decided to write a script that would find the values for me and output the results in a separate CSV file.

In practice, a user places this script within the folder containing the CSV files they want to scrape data from. They then provide the script with the headers of the data points they are interested in (if viewing in excel, this equates to column titles) and the resulting CSV file lists the maximum value for each data point on a row with the filename of the accompanying CSV log.


Planned Features:
- make sure 'filename' column is always first
- add 'minimum' feature
- add 'average' feature
- make path browseable (script doesn't have to be in containing folder)
- create GUI
- make .exe
