import urllib.request
import urllib.parse
import json

content = input("请输入翻译内容:")
data = {}
data['i'] = content
data['from'] = 'AUTO'
data['to'] = 'AUTO'
data['smartresult'] = 'dict'
data['client'] = 'fanyideskweb'
data['salt'] = '1517063365833'
data['sign'] = '84bfe1e9c28eecb7a179ae1da3084aea'
data['doctype'] = 'json'
data['version'] = '2.1'
data['keyfrom'] = 'fanyi.web'
data['action'] = 'FY_BY_CLICKBUTTION'
data['typoResult'] = 'false'
data = urllib.parse.urlencode(data).encode('utf-8')
url = "http://fanyi.youdao.com/translate"

headers = {}
'''headers['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; WOW64) \
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"'''
req = urllib.request.Request(url, data, headers)
req.add_header('User-Agent', "Mozilla/5.0 (Windows NT 10.0; WOW64) \
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36")
response = urllib.request.urlopen(req)
html = response.read().decode('utf-8')
target = json.loads(html)
result = target['translateResult'][0][0]['tgt']
print("翻译结果为:%s" % result)
