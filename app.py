import os.path
import tornado.web
import wsgiref.simple_server
import tornado.wsgi
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
    '''
    print 'Server Running...'
    print 'Port: ' + str(port)
    app.listen(port)
    tornado.ioloop.IOLoop.instance().start()
    '''

    # Startup tornado server with wsgi (guinicorn)
    # Run guinicorn
    # Command: gunicorn -b 192.168.1.66 api_startup:application
    application = tornado.wsgi.WSGIAdapter(app)

    # Start the server forever without running command
    # Method: make_server(bind-ip-address, port , application)
    server = wsgiref.simple_server.make_server('', port, application)
    print "Started server with port:" + str(port) + "..."
    server.serve_forever()



