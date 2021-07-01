import csv
dataset_1=[]
dataset_2_sorted=[]

with open("dataset_1.csv","r")as f:
    csvreader=csv.reader(f)
    for row in csvreader:
        dataset_1.append(row)

with open("dataset_2_sorted.csv","r")as f:
    csvreader=csv.reader(f)
    for row in csvreader:
        dataset_2_sorted.append(row)

headers_1=dataset_1[0]
planets_data_1=dataset_1[1:]

headers_2=dataset_2_sorted[0]
planets_data_2=dataset_2_sorted[1:]

headers=headers_1+headers_2
planet_data=[]

for index,data_row in enumerate (planets_data_1):
    planet_data.append(planets_data_1[index]+planets_data_2[index])

with open("final1.csv","a+")as f:
    csvwriter=csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planet_data)