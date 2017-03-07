import csv
input = open('Seattle_911.csv', 'rb')
output = open('carfire.csv', 'wb')
writer = csv.writer(output)
for row in csv.reader(input):
    if "car fire" in row[1].lower():
        writer.writerow(row)
input.close()
output.close()