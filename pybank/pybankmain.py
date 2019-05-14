import csv
import os
file_to_load = os.path.join("pybank", "Resources", "budget_data.csv")

# Set Variables

total_months = 0
month_of_change = []
net_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 0]
total_net = 0
prev_net = 0

# Open CSV

with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

# Iterate over headers

    header = next(reader)

# Track total months

    for row in reader: 
        
        total_months = total_months + 1
        total_net = total_net + float(row[1])

        if total_months > 1:

            # Track the net change
     
            net_change = float(row[1]) - prev_net
        
            net_change_list = net_change_list + [net_change]
            month_of_change = month_of_change + [row[0]]

        # Calculate the greatest increase
    
            if net_change > greatest_increase[1]:
                greatest_increase[0] = row[0]
                greatest_increase[1] = net_change

        # Calculate the greatest decrease
            if net_change < greatest_decrease[1]:
                greatest_decrease[0] = row[0]
                greatest_decrease[1] = net_change

        prev_net = float(row[1])

# Track net monthly averages
         
net_monthly_avg = sum(net_change_list)/(len(net_change_list))

#Output a summary of the analysis:
print()
print(f'Financial Analysis')
print(f'__________________')
print(f'Total Months: {total_months}')
print(f'Total:{total_net}')
print(f'Average Change: ${(round(net_monthly_avg, 2))}')
print(f'Greatest Increase in Profits: {greatest_increase[0:]}')
print(f'Greatest Decrease in Profits: {greatest_decrease[0:]}')


import sys
sys.stdout = open('PyBank_Output.txt', 'w')

print(f'Financial Analysis')
print(f'__________________')
print(f'Total Months:{total_months}')
print(f'Total:{total_net}')
print(f'Average Change: ${(round(net_monthly_avg, 2))}')
print(f'Greatest Increase in Profits: {greatest_increase[0:]}')
print(f'Greatest Decrease in Profits: {greatest_decrease[0:]}')






     


