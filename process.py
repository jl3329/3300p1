import csv
input = open('edit.csv', 'rb')
output = open('processed911.csv', 'wb')
writer = csv.writer(output)
for row in csv.reader(input):
    if row[0] and row[1] and row[2] and row[3] and row[4] and row[5] and row[6]:
        writer.writerow(row)
input.close()
output.close()