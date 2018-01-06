import  glob

cookie_file = glob.iglob(r'.\*cookies')
cookie = {}
with open([f for f in cookie_file][0], encoding='utf8') as fp:
    for c in fp:
        kv = c.replace('\n', '').split('\t')
        cookie[kv[-2]] = kv[-1]
    fp.close()

with open('.\cookies_dictionary.txt', 'w') as fw:
    fw.write(str(cookie))
    fw.close()