import urllib.request
import re
import os


def url_open(page_url):
    req = urllib.request.Request(page_url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36')
    response = urllib.request.urlopen(req)
    html = response.read()
    return html


def find_picture(html):
    string = r'img class="BDE_Image" src="[^"]+\.jpg'
    picture_address = re.findall(string, html)
    return picture_address


def download_mm(floder='ooxx'):
    os.chdir(os.getcwd())
    if floder not in os.listdir():
        os.mkdir(floder)
    os.chdir(floder)
    page_url = 'https://tieba.baidu.com/p/3563409202?red_tag=2364272361'
    html = url_open(page_url).decode('utf-8')
    picture_address = find_picture(html)
    for each_address in picture_address:
        each_file_name = each_address.split('/')[-1]
        with open(each_file_name, 'wb') as f:
            print(each_address)
            picture = url_open(each_address[each_address.find('https'):])
            f.write(picture)


if __name__ == '__main__':
    download_mm()
