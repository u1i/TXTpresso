import socket
import logging
from dnslib import DNSRecord, RR, QTYPE, TXT

logging.basicConfig(level=logging.INFO)

class BaseHandler:
    def handle(self):
        raise NotImplementedError("This method should be overridden")

class TXTpressoServer:
    def __init__(self, port=53):
        self.port = port
        self.handlers = {}

    def register_handler(self, action, handler):
        if issubclass(handler, BaseHandler):
            self.handlers[action] = handler()
        else:
            raise TypeError("Handler must be a subclass of BaseHandler")

    def handle_request(self, dns_request):
        qname = str(dns_request.q.qname)
        qtype = QTYPE[dns_request.q.qtype]

        reply = dns_request.reply()
        if qtype != 'TXT':
            logging.info("Non-TXT query received, returning default reply.")
            return reply

        parts = qname.split('.')
        # Extract the action and ignore the random part
        action = parts[0].split('.')[0] if parts else ''
        handler = self.handlers.get(action)

        if handler:
            response_data = handler.handle()
        else:
            response_data = "Error: Unrecognized request."

        reply.add_answer(RR(qname, QTYPE.TXT, rdata=TXT(response_data)))
        return reply

    def start(self):
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.bind(('', self.port))
            logging.info(f"TXTpresso Server listening on port {self.port}")

            try:
                while True:
                    data, addr = s.recvfrom(512)
                    try:
                        dns_req = DNSRecord.parse(data)
                        response = self.handle_request(dns_req)
                        s.sendto(response.pack(), addr)
                    except Exception as e:
                        logging.error(f"Error processing request: {e}")
            except KeyboardInterrupt:
                logging.info("TXTpresso Server shutting down")

if __name__ == '__main__':
    server = TXTpressoServer()
    # Example handler registration
    # server.register_handler('time', TimeHandler)
    server.start()