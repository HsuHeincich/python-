import csv

csvfile = open('E:/xhy_python/data-wrangling-master/data/chp3/data-text.csv', 'rb')
reader = csv.reader(csvfile)

for row in reader:
    print row


# cycle
dogs=['a','b','c','d',]
for dog in dogs:
    print dog