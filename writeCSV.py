import csv
import random

with open('testData.csv', mode='w') as csv_file:
    fieldnames = ['class', 'dept', 'birth_month']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'emp_name': 'John Smith', 'dept': 'Accounting', 'birth_month': 'November'})
    writer.writerow({'emp_name': 'Erica Meyers', 'dept': 'IT', 'birth_month': 'March'})

#CS array
cs_classes = []
int x = len(cs_classes)
all_classes = []
int y = len(all_classes)

#CS only:
for i in range(50):
	writer.writerow({cs_classes[random.randint(0, x)]},{cs_classes[random.randint(0, x)]},{cs_classes[random.randint(0, x)]},{cs_classes[random.randint(0, x)]})

for j in range (950):
	writer.writerow({all_classes[random.randint(0, y)]},{all_classes[random.randint(0, y)]},{all_classes[random.randint(0, y)]},{all_classes[random.randint(0, y)]})


