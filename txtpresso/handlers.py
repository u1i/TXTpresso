class BaseHandler:
    def handle(self):
        raise NotImplementedError("This method should be overridden")

class DefaultHandler(BaseHandler):
    def handle(self):
        return "no data for this request sorry"

