import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')
csvpath_out = os.path.join('Resources', 'budget_data.txt')

with open(csvpath, newline= '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')
    csv_header = next(csvreader, None)

    change = 0
    total_months = 0
    total_pnl= 0
    avg_chg = 0
    heighest_ip = 0
    heighest_dp = 0

    for row in csvreader:
        total_months += 1
        total_pnl += int(row[1])

        if int(row[1]) - avg_chg > heighest_ip:
            heighest_ip = int(row[1]) - avg_chg
            hip_month = row[0]
        elif int(row[1]) - avg_chg < heighest_dp:
            heighest_dp = int(row[1]) - avg_chg
            hdp_month = row[0]
            change += int(row[1])

        avg_chg = int(row[1])

with open(csvpath_out, 'w', newline= '') as txtfile:

    txtfile.write('Financial Analysis\n')
    txtfile.write('----------------------------\n')
    txtfile.write('Total Months: '+str(total_months) + '\n')
    txtfile.write('Total: $'+str(total_pnl) + '\n')
    txtfile.write("Average Change: "+str(round((change/(total_months-1)),2)) + '\n')
    txtfile.write('Greatest Increase in Profit: '+hip_month+' ($'+str(heighest_ip) + ')\n')
    txtfile.write('Greatest Decrease in Profits:'+hdp_month+' ($'+str(heighest_dp) + ')\n')

with open(csvpath_out, newline= '') as f:
    for line in f:
        print(line, end = '')


