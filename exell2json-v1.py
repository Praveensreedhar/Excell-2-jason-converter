import csv, json
csvFilePath = "amc.csv"
jasonFilePath = "amc1.json"

data ={}
with open(csvFilePath) as csvFile:
    csvReader = csv.DictReader(csvFile)
    for csvRow in csvReader:
        Device =csvRow["IPaddress"]
        data[Device] =csvRow


with open('amc11.json', 'w') as jsonFile:
    jsonFile.write(json.dumps(data, indent=1))
