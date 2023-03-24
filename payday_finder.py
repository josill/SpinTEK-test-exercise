import datetime
import csv
import holidays

class payday_finder:
    
    def __init__(self, year):
        self.year = year
        self.accountant_notifications = {} # Save the accountant notifications for every month
        self.payday_notifications = {} # Save the payday notifications for every month
        self.holidays = [] # Save the holidays for the given year

    def get_holidays(self):
        """
        Adds all the holiday dates in Estonia for the given year to a list.

        Returns:
        -None
        """
        for holiday in holidays.Estonia(years = self.year).items():
            self.holidays.append(holiday[0])  

    def get_paydays(self):
        """
        Generates a dictionary of payday notifications and a dictionary of accountant notifications for the given year.

        The function iterates through all the days of the year, starting from December 31st and ending on January 1st, to identify the 10th day of each month as the payday.        
        If the 10th day falls on a weekend, the payday is moved to the Friday before. If the 10th day is not a weekend 
        but the following Monday is, the accountant notification is sent on the preceding Thursday. If there are no issues 
        with the payday or accountant notification, the function adds the corresponding dates to the payday and accountant 
        notifications dictionaries. 

        Returns:
        - None
        """
        start_date = datetime.date(self.year, 1, 1)
        end_date = datetime.date(self.year, 12, 31)
        decrementor = datetime.timedelta(days=1)
        current_date = end_date
        flag = False # Create a flag for the paydays that are not on the 10th day

        while current_date >= start_date:
            if flag and current_date.isoweekday() not in (6, 7) and current_date not in self.holidays:
                self.accountant_notifications[current_date.strftime("%B")] = datetime.date(self.year, current_date.month, current_date.day - 3).strftime("%Y-%m-%d")
                self.payday_notifications[current_date.strftime("%B")] = datetime.date(self.year, current_date.month, current_date.day).strftime("%Y-%m-%d")
                flag = False # Deactivate special case scenario, where the payday is on a weekend

            if current_date.day == 10:
                if current_date.isoweekday() not in (6, 7) and current_date not in self.holidays:
                    self.accountant_notifications[current_date.strftime("%B")] = datetime.date(self.year, current_date.month, current_date.day - 3).strftime("%Y-%m-%d")
                    self.payday_notifications[current_date.strftime("%B")] = datetime.date(self.year, current_date.month, current_date.day).strftime("%Y-%m-%d")
                else:
                    flag = True # Activate special case scenario, where the payday is on a weekend

            current_date -= decrementor # Set the current date as the day before the current date

    def download_as_csv(self):
        """
        Writes the accountant notifications and payday notifications for the given year to a CSV file.

        The function creates a new CSV file with the name "{year given by user}.csv" and writes the accountant notifications and payday 
        notifications to it. The CSV file includes a header row with the column names "Kuu", "Raamatupidaja meeldetuletuse 
        kuupäev", and "Palgapäeva kuupäev". The function then iterates through the accountant notifications and payday 
        notifications dictionaries in reverse order and writes the corresponding values to the CSV file.

        Returns:
        - None
        """
        with open(f"{year}.csv", "w", newline="") as file:
            writer = csv.writer(file)

            writer.writerow(["Kuu", "Raamatupidaja meeldetuletuse kuupäev", "Palgapäeva kuupäev"])

            for month in reversed(self.accountant_notifications.keys()):
                writer.writerow([month, self.accountant_notifications[month], self.payday_notifications[month]])
                

print("Enter the year:")

year = int(input())

payday_finder_class = payday_finder(year)
payday_finder_class.get_holidays()
payday_finder_class.get_paydays()
payday_finder_class.download_as_csv()