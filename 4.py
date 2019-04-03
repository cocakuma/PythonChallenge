from urllib import request
import re

url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
num = "12345"

for i in range(0, 400):
    data = request.urlopen(url + num).read().decode('utf-8')
    print(data)
    num = re.search(r"nothing is (\d+)", data).group(1)
    # print(i, num)
