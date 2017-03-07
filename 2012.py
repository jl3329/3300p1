import csv
input = open('Seattle_911.csv', 'rb')
output = open('edit.csv', 'wb')
writer = csv.writer(output)
for row in csv.reader(input):
    if "/2012" in row[2]:
        writer.writerow(row)
input.close()
output.close()