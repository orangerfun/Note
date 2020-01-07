import tornado.ioloop
import tornado.web
import requests
import logging
import json
from tornado.httpserver import HTTPServer
from tornado.web import Application
from biz import Sync_io


# 加载输入数据，确定其类型
def understand_data(data):
    if isinstance(type(data), bytes):
        try:
            data = pickle.loads(data)
        except:
            raise ValueError("Can not pickle bytes!")
    else:
        try:
            data = json.loads(data)
        except:
            pass
    return data


class MainHandler(tornado.web.RequestHandler):
	def get(self):
		self.write("hellow,word")

class WriteDownHandler(tornado.web.RequestHandler):
    # def decode_argument(self, value, name=None):
    #     try:
    #         return _unicode(value)
    #     except UnicodeDecodeError:
    #         return bytes(value)
    #     except:
    #         raise HTTPError(400, "[WriteDownHandler]: Invalid unicode or bytes in %s: %r" %
                            # (name or "url", value[:40]))
    # 以post方式发起请求
    def post(self):
        # logger.info("[WriteDownHandler]: get data from memory")
        write_data = self.get_argument("data")
        write_data = understand_data(write_data)
        path = self.get_argument("file_name")
        if not isinstance(path, str):
            # logger.warn("[WriteDownHandler]: TypeError: not a file name")
            return
        write_flag = self.get_argument("write_mode")
        if not isinstance(write_flag, str):
            # logger.warn("[WriteDownHandler]: TypeError: write_flag is not string")
            return
        # logger.info("[WriteDownHandler]: write data into %s" % path)
        with open(path, write_flag, encoding="utf-8") as f:
            f.write(write_data)
        # sync_io.write(path, {"flag": write_flag, "data": write_data})
        # logger.info("[SendOutHandler]: write done")


# sync_io = Sync_io()
handlers = [(r"/wt",WriteDownHandler)]
application = Application(handlers)
if __name__ == '__main__':
	server = HTTPServer(application)
	server.listen(6000)
	tornado.ioloop.IOLoop.current().start()
	