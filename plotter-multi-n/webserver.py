#Copyright Jon Berg , turtlemeat.com
#modified by Chris Takahashi

import string,cgi,time
from os import curdir, sep
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer


class MyHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        try:
            if self.path.endswith(".html"):
                f = open(curdir + sep + self.path) #self.path has /test.html
#note that this potentially makes every file on your computer readable by the internet

                self.send_response(200)
                self.send_header('Content-type',	'text/html')
                self.end_headers()
                self.wfile.write(f.read())
                f.close()
                return
            if self.path.endswith(".gif"):
                f = open(curdir + sep + self.path,'rb') #self.path has /test.html
#note that this potentially makes every file on your computer readable by the internet

                self.send_response(200)
                self.send_header('Content-type',	'image/gif')
                self.end_headers()
                self.wfile.write(f.read())
                f.close()
            if self.path.endswith(".png"):
                f = open(curdir + sep + self.path,'rb') #self.path has /test.html
#note that this potentially makes every file on your computer readable by the internet

                self.send_response(200)
                self.send_header('Content-type',	'image/png')
                self.end_headers()
                self.wfile.write(f.read())
                f.close()
            if self.path.endswith(".dat"):
                f = open(curdir + sep +".." + sep + self.path,'rb') #self.path has /test.html
#note that this potentially makes every file on your computer readable by the internet

                self.send_response(200)
                self.send_header('Content-type',	'application/octet-stream')
                self.end_headers()
                self.wfile.write(f.read())
                f.close()
#            if self.path.endswith(".esp"):   #our dynamic content
#                self.send_response(200)
#                self.send_header('Content-type',	'text/html')
#                self.end_headers()
#                self.wfile.write("hey, today is the" + str(time.localtime()[7]))
#                self.wfile.write(" day in the year " + str(time.localtime()[0]))
#                return
                
            return
                
        except IOError:
            self.send_error(404,'File Not Found: %s' % self.path)
     

    def do_POST(self):
        global rootnode
        try:
            ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
            if ctype == 'multipart/form-data':
                query=cgi.parse_multipart(self.rfile, pdict)
            self.send_response(301)
            
            self.end_headers()
            upfilecontent = query.get('upfile')
            print "filecontent", upfilecontent[0]
            self.wfile.write("<HTML>POST OK.<BR><BR>");
            self.wfile.write(upfilecontent[0]);
            
        except :
            pass

def main():
    try:
        server = HTTPServer(('', 8484), MyHandler)
        print 'started httpserver...'
        server.serve_forever()
    except KeyboardInterrupt:
        print '^C received, shutting down server'
        server.socket.close()
        raise

if __name__ == '__main__':
    main()

