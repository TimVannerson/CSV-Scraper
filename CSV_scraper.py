import sys
import os
import csv


def yesOrNo(string):
    if string == "yes" or string == "no":
        return True
    else:
        return False

def validAction(string):
    if string == "min" or string == "max" or string == "avg":
        return True
    else:
        return False

monitors = {}
moreScrapers = True        
while moreScrapers:
    monitors[raw_input("What monitor would you like to scrape? (please make sure your response exactly matches the header in the CSV file(s): ")] = 0
    while True:
        status = raw_input("Would you like to scrape another monitor? (yes/no): ").lower()
        if yesOrNo(status):
            break
    if status == "yes":
        moreScrapers = True
    else:
        moreScrapers = False
monitors['filename'] = None

while True:
    action = raw_input("What action would you like to take on the monitors? (min/max/avg): ").lower()
    if validAction(action):
        break


if action == "max":
    with open('max_values.csv', 'wb') as output:
        fieldnames = []
        for key in monitors:
            fieldnames.append(key)
        writer = csv.DictWriter(output, fieldnames=fieldnames)
        writer.writeheader()

        for file in os.listdir(os.getcwd()):
            if file.endswith(".csv") and not file.startswith("max_values"):
                with open(file) as csvfile:
                    reader = csv.DictReader(csvfile)
                    for row in reader:
                        for key in monitors:
                            if key == 'filename':
                                monitors['filename'] = file
                            else:
                                if row[key] > monitors[key]:
                                    monitors[key] = row[key]
                    writer.writerow(monitors)
                    for key in monitors:
                        monitors[key] = 0
        #merge rows in output csv
       
elif action == "min":
    print "Sorry, that command is currently in development."

elif action == "avg":
    print "Sorry, that command is currently in development."


