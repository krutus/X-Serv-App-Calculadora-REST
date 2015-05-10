#!/usr/bin/python

"""	
	Luis Haro
	programa principal practica calculadora rest

"""

import socket
import calc


class app:
    
    def parse(self, request):
        return None

    def process(self, parsedRequest):
        
        return ("200 OK", "<html><body><h1>It works!</h1>" + "</h1><p> App : " + str(self) + "</p></body></html>")


class webApp:

    def select(self, request):

        resource = request.split(' ', 2)[1]
        for prefix in self.apps.keys():
            if resource.startswith(prefix):
                print "Running app for prefix: " + prefix + \
                    ", rest of resource: " + resource[len(prefix):] + "."
                return (self.apps[prefix], resource[len(prefix):])
        print "Running default"
        return (self.myApp, resource)

    def __init__(self, hostname, port, apps):

	self.apps = apps
	self.myApp = app()

        mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        mySocket.bind((hostname, port))

        mySocket.listen(5)

        while True:
            print 'Waiting for connections'
            (recvSocket, address) = mySocket.accept()
            print 'HTTP request received (going to process):'
            request = recvSocket.recv(2048)
            print request
            (App, rest) = self.select(request)
            parsedRequest = App.parse(request, rest)
            (returnCode, Answer) = App.process(parsedRequest)
            print 'Answering...'
            recvSocket.send("HTTP/1.1 " + returnCode + " \r\n\r\n"
                            + Answer + "\r\n")
            recvSocket.close()

if __name__ == "__main__":
    anApp = app()
    otherApp = app()
    suma = calc.plus()
    resta = calc.subtract()
    multi = calc.mult()
    div = calc.div()
    testWebApp = webApp("localhost", 1234, {'/app': anApp,
					    '/other': otherApp,
					    '/suma': suma,
					    '/+' :suma,
                                            '/resta': resta,
					    '/-' : resta,
					    '/mult' : multi,
                                            '/x': multi,
                                            '/div': div,
					    '/:' : div})

