from mycsv import getdata, writecsv
import json
import re

def json2csv():
    jdata = getdata()
    jdata = jdata.replace('\n', '') #this is a single backslash literal
    first_bracket = jdata.find('{')
    last_bracket = jdata.rfind('}')
    jdata = jdata[first_bracket+1:last_bracket]
    jdata = jdata.split('"data":')

    headers = jdata[0].split('headers')[1]#[2:-2].split(',')
    first_square = headers.find('[')
    last_square = headers.find(']')
    headers = headers[first_square+1:last_square]
    headers = headers.replace('"', '').split(',')

    jvalues = jdata[1].replace(' ', '')#.replace(':', '').replace('"', '')
    first_bracket = jvalues.find('{')
    last_bracket = jvalues.rfind('}')
    jvalues = jvalues[first_bracket+1:last_bracket]
    jvalues = jvalues.split('},{')

    data = []
    for line in jvalues:
        temp = []
        for cell in line.split(','):
            value = cell.split(':')[1].replace('"', '')
            temp.append(value)
        data.append(temp)
    #sorted_headers = sorted(headers, key=len, reverse=True)
    #for header in sorted_headers:
    #    jvalues = jvalues.replace(header, '')
    #jvalues = jvalues[2:-3]
    #jvalues = jvalues.split('},{')
    #jvalues = [jvalue.split(',') for jvalue in jvalues]

    #data = []
    #temp = []
    #for line in jvalues:
    #   for header in headers:
    #        temp.append(line[header])
    #    data.append(temp)
    #    temp = []

    return writecsv(headers, data)

if __name__ == '__main__':
    print(json2csv())