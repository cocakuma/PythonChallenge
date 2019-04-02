from urllib import request
import re

url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
num = "12345"

for i in range(0, 400):
    data = str(request.urlopen(url + num).read())
    print(data)
    num = re.search(r"nothing is (\d+)", data).group(1)
    # print(i, num)
