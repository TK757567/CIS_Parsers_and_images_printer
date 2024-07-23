import json,csv



def getInfo(filename, description):
    f = open(filename, "r")
    jsonload = json.load(f)
    for i in jsonload['checks'][0]['contents'][1]['contents']:
        print(i['contents'])
        if i['contents']['type'] == 'CONFIG_CHECK' and i['contents']['description'] == description:
            info = i['info']
            print(info)
            
        #    solution = i['contents']['solution'][0]
        #    f.close()
        #    return info,solution
    
        return "None","None"


#info, solution = getInfo('CIS_Cisco_IOS_15_v4.1.1_Level_1.json', "4.2 Configure a Remote Backup Schedule")

# input
cis = open("tt", "r").readlines()

# output file
#file = open('output.csv', 'w', newline='')
#writer = csv.writer(file)


for i in cis:
    i = i.strip()
    
    info, solution = getInfo('CIS_Microsoft_Windows_Server_2022_Benchmark_v1.0.0_L1_MS.json',i)

#    writer.writerow([i,info, solution])

    

