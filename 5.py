from urllib import request
import pickle

data = request.urlopen("http://www.pythonchallenge.com/pc/def/banner.p")
# print(type(data))
# str1 = ''.join(str(data))
# print(pickle.load(data))
for item in pickle.load(data):
    print(item)
    # for x in item:

