# hello_world.py
from txtpresso.server import TXTpressoServer, BaseHandler

class HelloHandler(BaseHandler):
    def handle(self):
        return "Hello, world!"

def main():
    server = TXTpressoServer()
    server.register_handler('hello', HelloHandler)
    print("TXTpresso Hello World server is running. Query with 'dig @localhost -p 53 +short txt hello.txtpresso'")
    server.start()

if __name__ == "__main__":
    main()