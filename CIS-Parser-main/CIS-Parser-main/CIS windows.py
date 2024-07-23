import json,csv



def getInfo(filename, description):
    f = open(filename, "r")
    jsonload = json.load(f)
    for i in jsonload['checks'][0]['contents'][1]['contents']:
        if i['item_type'] == 'custom' and i['contents']['description'][0] == description:
            info = i['contents']['info'][0]
            solution = i['contents']['solution'][0]
            f.close()
            return info,solution
    
    return "None","None"


# info, solution = getInfo('CIS_MS_Windows_10_Enterprise_Level_1_v1.12.0.json', "19.7.4.1 Ensure 'Do not preserve zone information in file attachments' is set to 'Disabled'")

# input
cis = open("tt", "r").readlines()

# output file
file = open('output.csv', 'w', newline='')
writer = csv.writer(file)


for i in cis:
    i = i.strip()
    info, solution = getInfo('CIS_MS_Windows_11_Enterprise_Level_1_v1.0.0.json',i)

    writer.writerow([i,info, solution])
