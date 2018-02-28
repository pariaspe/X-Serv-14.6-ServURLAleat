#!/usr/bin/python3

"""
Pedro Arias Perez
ITT+IAA
 pariaspe @ alumnos.urjc.es
 SAT (Universidad Rey Juan Carlos)
"""

import webapp

class aleat(webapp.webApp):
    def process(self, parsedRequest):
        return ("200 OK", "<html><body><h1>Hola</h1></body></html>")

if __name__ == '__main__':
    miapp = aleat('0.0.0.0', 1234)
