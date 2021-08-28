import sys
from jinja2 import Template


def getdata():
    if len(sys.argv)==1: # if no file given, read from stdin
        data = sys.stdin.read()
    else:
        f = open(sys.argv[1], "r")
        data = f.read()
        f.close()
    return data.strip()


def readcsv(content):
    """
    Read CSV with header from data string and return a header list
    containing a list of names and also return the list of lists
    containing the data.
    """
    lines = content.splitlines()
    headers = [header.strip() for header in lines[0].split(',')]
    data = [lines[i].split(',') for i in range(1, len(lines))]

    return headers, data


def writehtml(headers, data, template_file):

    with open(template_file) as file:
        t = Template(file.read())

    return t.render(headers=headers, data=data)


def writecsv(headers, data):

    csv = ''
    for head in headers:
        csv += (head + ',')
    csv = csv[:-1] + '\n'

    temp = ''
    for line in data:
        for i in range(len(line)):
            temp += (line[i] + ',')
        csv += temp
        temp = ''
        csv = csv[:-1] + '\n'
    csv = csv[:-1]

    return csv
