import csv #Import csv to allow working with csv files
import datetime #Import datetime to enable working with dates

iDate = datetime.datetime.now()
date = iDate.strftime("%x") #Create date variable and store it in MM/DD/YYYY format

gross = int(input("Please enter todays gross sales:")) #Create gross sales variable from user input

tax = 1.2 #Define the tax rate, set as variable so it can be changed accordingly

net = gross / tax #Work out the net sales by dividing by the tax rate

with open('sales.csv', mode='a') as sales: #Create sales.csv and open it
    sales_writer = csv.writer(sales, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL) #Define the writing algorithm

    sales_writer.writerow(['00/00/0000', '0', '0']) #Zero values to initialize the calculations
    sales_writer.writerow([date, gross, ]) #Write data from program into file
