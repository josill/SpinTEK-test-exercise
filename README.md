# SpinTEK payday finder

The purpose of this Command Line Interface (CLI) application is to prompt the user for a specific year, and then compute all the paydays in accorande with the Estonian law. In Estonia paydays are always scheduled for the 10th day of the upcoming month, and if the 10th falls on a weekend, the payday is rescheduled to the previous weekday.

## Starting the script

1. Open the terminal and change directory to the root folder:
2. Create a virtual environment
```
$ python -m venv /path/to/new/virtual/environment
```
3. Activate the virutal environment

On Mac:
```
$ source venv/bin/activat
```
On Windows:
```
$ .\venv\Scripts\activate
```
4. Install the requirements from the requirements.txt file
```
$ pip install -r requirements.txt
```
5. Run the script from your code editor or from the terminal via the command
```
$ python payday_finder.py
```

## payday_finder class

This class maintains a record of the actual paydays and sends notifications to the accountant about upcoming paydays. Notifications are sent to the accountant three days prior to the payday.

### get_paydays function

Generates a dictionary of payday notifications and a dictionary of accountant notifications for the given year.

To begin with, we set the start date of the year as January 1st and the end date as December 31st. Additionally, we initialize a decrementor that will decrease the day count in each iteration, along with the current date and a flag that identifies special cases where the 10th day falls on a weekend. Here we are using the datetime library to handle all the date logic.

We proceed to iterate through every day of the year and add the notification if the special case flag has not been raised and the payday (which is always on the 10th day of each month) is not on a weekend. If the payday falls on a weekend, we raise the special case flag to identify the closest Friday in the subsequent iterations. It is worth noting that we are iterating the days of the year in reverse to identify the nearest Friday to the payday, in case it is a special case.

### get_paydays function

Writes the accountant notifications and payday notifications for the given year to a CSV file.

In this block of code, we either create a new csv file or open an existing one with the given year name. The file is created in the same folder, where the application is ran from. Then, we use the csv library to initialize the csv writer, and set the header row with the cells "Kuu", "Raamatupidaja meeldetuletuse kuupäev" and "Palgapäeva kuupäev".

Next we iterate through the accountant notifications dictionary in reverse (to maintain the correct order of months) and write a row for each key-value pair that corresponds to the headers.
