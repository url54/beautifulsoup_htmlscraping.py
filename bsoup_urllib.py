# This program was built for an assignment.  The objective of the assignment was to
# scrape a specific website for specific data and then provide the sum of that data (in this case integers)
# The assignemnt instructions are follow these comments.

# Scraping Numbers from HTML using BeautifulSoup In this assignment you will write a Python program that uses
# urllib and BeautifulSoup to read the HTML from the data files below, and parse the data, extracting numbers and compute the sum 
# of the numbers in the file. Actual data: http://py4e-data.dr-chuck.net/comments_1139132.html (Sum ends with 30)
# You do not need to save these files to your folder since your program will read the data directly from the URL.
# Note: Each student will have a distinct data url for the assignment - so only use your own data url for analysis.

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

nlst = list()
tags = soup('span')
for tag in tags:
    nmb = int(tag.contents[0])
    nlst.append(nmb)
print(sum(nlst))
