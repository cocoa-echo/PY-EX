import re

fp = r'C:\Users\Administrator\Desktop\push.txt'
with open(fp, encoding='utf8') as f:
    fc = f.read()
    code_contry_re = r'sel="(\d+)".*?png">([^\d]{1,})</li>'
    ff = re.findall(code_contry_re, fc)
    d = {}
    for i in range(len(ff)):
        d[ff[i][0]] = ff[i][1]

    print(d)



if __name__ == '__main__':
    import doctest
    doctest.testmod()