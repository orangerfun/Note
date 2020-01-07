import requests
import json

class RemoteIO(object):
    def __init__(self, host):
        self.host = host

    def save(self, data: list, file_name: str, write_mode: str):
        payload = {
            "data": json.dumps(data),
            "file_name": file_name,
            "write_mode": write_mode
        }
        requests.post(url="http://%s:6000/wt" % self.host, data=payload)

if __name__ == '__main__':
	remoteio = RemoteIO("localhost")
	write_flag = "a"
	data = "\ni love jiangsu"
	remoteio.save(data, "./123.txt",write_flag)