import json

with open("./area_codes.json", mode='r', encoding='utf-8') as jfile:
    jdata = json.load(jfile)

with open("./area_codes.json", mode='w', encoding='utf-8') as wfile:
    json.dump(jdata, wfile, ensure_ascii=False, indent=2)

newDict = {}

for i in jdata.keys():
    if i != "其他":
        newDict.update({
            f"{i}": []
        })
        for o in jdata[i].keys():
            newDict[i].append({
                "region": jdata[i][o],
                "zip": o
            })

with open("./area_codes2.json", mode='w', encoding='utf-8') as wfile:
    json.dump(newDict, wfile, ensure_ascii=False, indent=3)

