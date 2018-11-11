import re
import requests
from bs4 import BeautifulSoup
import bs4


def getHTMLText(url):
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        response.encoding = response.apparent_encoding
        return response.text
    except:
        print("There was a error!" , str(response.status_code))

