import urllib.request
import os


def url_open(page_url):
    req = urllib.request.Request(page_url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36')
    req.add_header('Referer', " ")
    response = urllib.request.urlopen(req)
    html = response.read()
    return html


'''def get_page_num(page_url):
    html = url_open(page_url)
    html = html.decode('utf-8')
    page_num_begin = html.find('current-comment-page') + 23
    page_num_end = html.find(']', page_num_begin)
    page_num = int(html[page_num_begin: page_num_end])
    return page_num

'''


def page_find_picture(page_url):
    html = url_open(page_url).decode('utf-8')
    picture_address = []
    page_find_picture_begin = 0
    page_find_picture_end = 0
    while True:
        if html.find('img src', page_find_picture_end) == -1:
            break
        else:
            page_find_picture_begin = html.find('img src', page_find_picture_end) + 9
            page_find_picture_end = html.find('.jpg', page_find_picture_begin, page_find_picture_begin + 255) + 4
            picture_address.append(html[page_find_picture_begin:page_find_picture_end])
    return picture_address


def page_save_picture(page_address):
    for each_address in page_address:
        file_name = each_address.split('/')[-1]
        with open(file_name, 'wb') as picture_file:
            image = url_open(each_address)
            picture_file.write(image)


def download_mm(floder='ooxx', pages=10):
    os.chdir(os.getcwd())
    if floder not in os.listdir():
        os.mkdir(floder)
    os.chdir(floder)
    url = 'http://www.umei.cc/meinvtupian/'
#   page_num = get_page_num(url)
    page_address = page_find_picture(url)
    page_save_picture(page_address)


'''    for i in range(pages):
        page_num -= 1
        page_url = url + '/page-' + str(page_num) + '#comments'
        page_address = page_find_picture(page_url)
        page_save_picture(floder, page_address)
'''


if __name__ == '__main__':
    download_mm()
