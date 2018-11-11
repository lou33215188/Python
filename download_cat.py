import urllib.request as u

response = u.urlopen(r"http://www.yaochanglai.com/d/file/img/rw/20170505/loloqsjk3mwybtm.jpg")
image = response.read()

with open("D://new_picture_1.jpg", "wb") as file_:
    file_.write(image)
