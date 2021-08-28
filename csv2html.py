from mycsv import getdata, readcsv, writehtml

def csv2html():
    headers, data = readcsv(getdata())

    return writehtml(headers, data, 'csv2html.template')

if __name__ == '__main__':

    print(csv2html())