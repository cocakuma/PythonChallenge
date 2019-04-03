import zipfile
import re

z = zipfile.ZipFile("channel.zip")
num = "90052"
comments = []

while True:
    name = num + ".txt"
    comments.append(z.getinfo(name).comment.decode('utf-8'))
    data = z.read(name).decode('utf-8')
    print(data)
    try:
        num = re.search(r"nothing is (\d+)", data).group(1)
    except AttributeError:
        break

print(''.join(comments))
