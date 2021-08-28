from mycsv import getdata, readcsv, writehtml

def csv2xml():
    headers, data = readcsv(getdata())

    return writehtml(headers, data, 'csv2xml.template')

if __name__ == '__main__':

    print(csv2xml())