from txtpresso.server import TXTpressoServer, BaseHandler
from datetime import datetime

class TimeHandler(BaseHandler):
    def handle(self):
        return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

if __name__ == '__main__':
    server = TXTpressoServer()
    server.register_handler('time', TimeHandler)
    server.start()

