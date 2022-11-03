import csv

with open('sales.csv', mode='w') as sales:
    sales_writer = csv.writer(sales, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    sales_writer.writerow(['Date', 'Gross', 'Net'])

    
    