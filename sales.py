import csv
import datetime

iDate = datetime.datetime.now()
date = iDate.strftime("%x")

with open('sales.csv', mode='w') as sales:
    sales_writer = csv.writer(sales, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    sales_writer.writerow(['Date', 'Gross', 'Net'])
    sales_writer.writerow([date, date, date])
    