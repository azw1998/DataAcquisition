import untangle
from mycsv import getdata, writecsv


def xml2csv():
    tree = untangle.parse(getdata())
    headers = tree.file.headers.cdata.split(',')
    data_values = tree.file.data.children
    data = []
    temp = []
    for i in range(len(data_values)):
        for j in range(len(data_values[i].children)):
            temp.append(data_values[i].children[j].cdata)
        data.append(temp)
        temp = []
    return writecsv(headers, data)

if __name__ == '__main__':
    print(xml2csv())