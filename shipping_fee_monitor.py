import requests
import re
import json
import threading
import  time
import country_code as cc

def handle_cookie():
    cookie = {}
    file_path = r'C:\Users\PY-EX\bg_ds_cookies'
    with open(file_path, encoding='utf8') as fp:
        for c in fp:
            kv = c.replace('\n', '').split('\t')
            cookie[kv[-2]] = kv[-1]

    return cookie


def verify_sucess_login():
    url = 'https://www.banggood.com/index.php?com=account&t=setting'
    r = requests.get(url, cookies=handle_cookie())
    content = r.text
    m = re.findall('zx_cxj@aliyun.com', content)
    if m:
        print('login successfully...')
    else:
        print('fail to login...')


def check_cn_fee(country_code):
    # weight: 20g
    product_select = 'https://www.banggood.com/index.php?com=shopcart&t=changeSelected'\
                              '&warehouse=722&selected=1&cart_ids[]=1226354'

    product_add = 'https://www.banggood.com/index.php?com=shopcart&t=changeQty&warehouse=722'\
                  '&cart_id=1226354&quantity='
    ds_cookie = handle_cookie()
    code, country = country_code

    ds_cookie['default_ship_country'] = code
    for i in range(1, 101):
        add_product = product_add + str(i)
        requests.get(add_product, cookies=handle_cookie())
        rev = requests.get(product_select, cookies=handle_cookie())
        rev_content = json.loads(rev.text)
        flag_word = 'This warehouse can not ship to your location'
        flag = re.findall(flag_word, rev_content['shipments'])
        # print(rev_content['shipments'])
        if flag:
            print(flag_word, 'weight', i*20, 'country', country)
        #print(country)



def main_thread():
    for country_id, country_name in cc.COUNTRY_CODE_CONSTANT.items():
        country_id_name = (country_id,country_name)
        t = threading.Thread(group=None, target=check_cn_fee, args=(country_id_name, ))
        t.start()
    count = threading.activeCount()
    print('running threading count:', count)

if __name__ == '__main__':
    start_time = time.time()
    main_thread()
    end_time = time.time()
    print('time:', end_time - start_time)