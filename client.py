import requests
for i in range(100):
    requests.post("http://localhost:8001/pub?id=my_channel_1", data="hey, count %d\n" % i)
