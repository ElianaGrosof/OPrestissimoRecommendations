import csv
import random

with open('testData.csv', mode='w') as csv_file:
    fieldnames = ['class', 'dept', 'birth_month']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'emp_name': 'John Smith', 'dept': 'Accounting', 'birth_month': 'November'})
    writer.writerow({'emp_name': 'Erica Meyers', 'dept': 'IT', 'birth_month': 'March'})

#CS array
cs_classes = [1442, 1445, 1448, 4234, 4235, 4236, 4681, 4685, 6729, 6865, 6866, 7267, 8313, 8315, 8316, 8559, 8560, 8561]
int x = len(cs_classes)
all_classes = [11709, 11917, 12276, 13818, 14094, 14096, 14098, 14099, 14101, 14260, 14261, 17790, 18089, 19336, 19540, 19543, 19545, 19546, 19547, 19687, 1442, 1445, 1448, 4234, 4235, 4236, 4681, 4685, 6729, 6865, 6866, 7267, 8313, 8315, 8316, 8559, 8560, 8561, 1547, 2231, 2627, 4187, 5274, 5293, 5947, 5948, 6022, 6909, 7839, 7991, 8317, 8320, 8553, 1067, 8370, 11946, 12221, 12348, 12387, 13427, 13530, 13531, 13647, 13647, 13648, 14086, 14088, 14089, 14344, 14545, 14546, 14557, 16066, 17302, 17303, 18485, 18579, 18597, 19133, 19281, 19536, 19538, 19539, 1048, 12142, 14093, 1049, 1045, 1046, 8325, 1047, 7727, 19812, 7157, 7158, 7159, 14273, 19811, 20052, 7160,17993, 10527, 1339, 1340, 1341, 1343, 1344, 1351, 1352, 1353, 1354, 1355, 1356, 1360, 2683, 2684, 6926, 7337, 8074, 8422, 8423, 8424, 8607, 9552, 9556, 9555, 9556, 9555, 9555, 9555, 15054, 15085, 16082, 16120, 16122, 18449, 18450, 18451, 17945, 18984, 18984, 18983, 16121, 19152, 18984, 12532, 14034, 14035, 14036, 11902, 12966, 13613, 13614, 10657, 10651, 8425, 1538, 1539, 13466, 14037, 14579, 19495, 19830, 19498, 14443, 7396, 17277, 19058, 19059, 19782, 19783, 19496, 19497, 12464, 18542, 19553, 19554, 15918, 19639, 19555, 19556, 19557, 19537, 19795, 19829, 19561, 19562, 19638, 19158, 19156, 18684, 15932, 19558, 19559, 19560, 19640, 18682, 19563, 17386]
int y = len(all_classes)

#CS only:
for i in range(50):
	writer.writerow({cs_classes[random.randint(0, x)]},{cs_classes[random.randint(0, x)]},{cs_classes[random.randint(0, x)]},{cs_classes[random.randint(0, x)]})

for j in range (950):
	writer.writerow({all_classes[random.randint(0, y)]},{all_classes[random.randint(0, y)]},{all_classes[random.randint(0, y)]},{all_classes[random.randint(0, y)]})


