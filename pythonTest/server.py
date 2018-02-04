import SimpleHTTPServer
import SocketServer


PORT = 8000

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
Handler.cgi_directories = ['/cgi-bin']

httpd = SocketServer.TCPServer(("",PORT),Handler)

print "serving at port", PORT
httpd.serve_forever()
