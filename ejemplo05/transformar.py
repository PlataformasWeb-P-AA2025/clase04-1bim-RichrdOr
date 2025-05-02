import csv
import json

jsonArr = []

with open('shampoo_sales.csv',encoding='utf-8') as csvfile:
    csvReader = csv.DictReader(csvfile)
    for row in csvReader:
        jsonArr.append(row)

with open('shampoo_sañes.csv','w', encoding='utf-8') as jsonfile:
    jsonString = json.dumps(jsonArr, indent=4)
    jsonfile.write(jsonString)
