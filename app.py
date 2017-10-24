import os.path
import tornado.web
from handler import *

# join the template and static folder path
settings = dict (
	template_path = os.path.join(os.path.dirname(__file__), "templates"),
	static_path = os.path.join(os.path.dirname(__file__), "static"),
	debug = True
)

# r"/" for root website
app = tornado.web.Application([
	(r"/", MainHandler),
	(r"/templates/(.*)", tornado.web.StaticFileHandler, {"path": "templates"}),
    (r"/static/(.*)", tornado.web.StaticFileHandler, {"path": "static"}),
    (r"/upload/(.*)", tornado.web.StaticFileHandler, {"path": "upload"}),

], **settings)

# start main function
if __name__ == "__main__":
    # Define the port
    port = 8888
    
    # Simple startup tornado server
    print 'Server Running...'
    print 'Port: ' + str(port)
    app.listen(port)
    tornado.ioloop.IOLoop.instance().start()



