#!/usr/bin/python

class plus():
	
	def parse(self, request, rest):
		try:
			operation = rest.split("/")
			first= int(operation[1])
			second= int(operation[2])
		except ValueError:
			return "Introduzca 2 numeros"
		return (first, second)

	def process(self, parsedRequest):
		if parsedRequest:
			result = int(parsedRequest[0]) + int(parsedRequest[1])
			return("200 OK", "<html><body><h1>" + str(result) + "</h1></body></html>")
		else:
			return ("400 Error", "<html><body><h1> Sum Error</h1></body></html>")

class subtract():

	def parse(self, request, rest):
	        try:
	        	operation = rest.split("/")
			first= int(operation[1])
			second= int(operation[2])
        	except ValueError:
            		return "Introduzca 2 numeros"
        	return (first, second)

	def process(self, parsedRequest):
        	if parsedRequest:
        		result = int(parsedRequest[0]) - int(parsedRequest[1])
            		return ("200 OK", "<html><body><h1>" + str(result) + "</h1></body></html>")
        	else:
            		return ("400 Error", "<html><body><h1> Subtraction Error</h1></body></html>")

class mult():

	def parse(self, request, rest):
	        try:
			operation = rest.split("/")
			first= int(operation[1])
			second= int(operation[2])
        	except ValueError:
            		return "Introduzca 2 numeros"
        	return (first, second)

    	def process(self, parsedRequest):
        	if parsedRequest:
            		result = int(parsedRequest[0]) * int(parsedRequest[1])
            		return ("200 OK", "<html><body><h1>" + str(result) + "</h1></body></html>")
        	else:
            		return ("400 Error", "<html><body><h1>Multiplication Error</h1></body></html>")

class div():

	def parse(self, request, rest):
	        try:
            		operation = rest.split("/")
		 	print operation
			first= int(operation[1])
			second= int(operation[2])
        	except ValueError:
            		return "Introduzca 2 numeros"
        	return (first, second)

    	def process(self, parsedRequest):
        	if parsedRequest:
            		result = int(parsedRequest[0]) / int(parsedRequest[1])
            		return ("200 OK", "<html><body><h1>" + str(result) + "</h1></body></html>")
        	else:
            		return ("400 Error", "<html><body><h1>Division Error</h1></body></html>")

