import json
from mycsv import getdata, readcsv

def csv2json():
    headers, data = readcsv(getdata())

    jdata = {}
    jdata["headers"] = headers
    data_values = []
    temp_dict = {}
    for line in data:
        for i in range(len(headers)):
            temp_dict[headers[i]] = line[i]
        data_values.append(temp_dict)
        temp_dict = {}
    jdata["data"] = data_values

    jdata = str(jdata)
    double_quote = '"'
    backslash = jdata[1]
    jdata = jdata.replace(backslash, double_quote)

    return jdata

if __name__ == '__main__':

    print(csv2json())