import csv 
from collections import Counter

""" Finding mean """
with open("height-weight.csv", newline = "") as f:
    csv_reader = csv.reader(f)
    file_data = list(csv_reader)

    file_data.pop(0)
    

weight_list = []
for i in range(0, len(file_data)):
    weight = float(file_data[i][1])
    weight_list.append(weight)

n = len(file_data)


total_sum = 0
for i in range(0, len(weight_list)):
   total_sum += weight_list[i]

mean = total_sum/n
print("Average of the weights is - " + str(mean))

""" Finding median """
if(n%2 == 0):
    median1 = float(weight_list[n//2])
    median2 = float(weight_list[n//2+1])

    median = (median1 + median2)/2
else:
    median = weight_list[n//2]

print("Median for the weights is " + str(median))

    
""" floor division - using 2 slashes // to ignore the after decimal numbers, but not round off """

""" finding mode """

data = Counter(weight_list)


mode_data_for_range = {
    "50-60" : 0,
    "60-70" : 0,
    "70-80" : 0
}
for weight, occurence in data.items():
    if 50 < float(weight) < 60:
        mode_data_for_range["50-60"] += occurence
    if 60 < float(weight) < 70:
        mode_data_for_range["60-70"] += occurence
    if 70 < float(weight) < 80:
        mode_data_for_range["70-80"] += occurence
    
mode_range, mode_occurence = 0, 0

for range, occurence in mode_data_for_range.items():
    if occurence > mode_occurence:
        mode_range, mode_occurence = [int(range.split('-')[0]), int(range.split('-')[1])], occurence

mode = (mode_range[0] + mode_range[1])/2

print(mode)


