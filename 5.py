from urllib import request
import pickle

data = request.urlopen("http://www.pythonchallenge.com/pc/def/banner.p")
for item in pickle.load(data):
    line = ""
    for x in item:
        line += x[0] * x[1]
    print(line)
