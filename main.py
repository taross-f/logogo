import requests, sys, time

def main():
    argv = sys.argv
    argc = len(argv)
    count = 1 if argc < 2 else int(argv[1])
    for _ in range(count):
        kick()
        time.sleep(1)
    kick()

def kick():
    headers = {'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}
    entry_payload = 'left=S&right=S&date=2020.12.16'
    entry_url = "http://zexy-logomakemagic.net/api/entry"
    
    entry_res = requests.post(entry_url, headers=headers, data=entry_payload)
    print(entry_res)
    print(entry_res.json())

    register_url = 'http://zexy-logomakemagic.net/api/regist'
    register_payload = 'uuid=' + entry_res.json()['uuid']

    register_res = requests.post(register_url, headers=headers, data=register_payload)
    print(register_res.json())

    image_url = 'http://zexy-logomakemagic.net/api/img/jpg?cpid=' + register_res.json()['cpid']
    image_res = requests.get(image_url)
    print(image_res)

    with open('images/' + register_res.json()['cpid'] + '.jpg', 'wb') as f:
        f.write(image_res.content)

if __name__ == "__main__":
    main()