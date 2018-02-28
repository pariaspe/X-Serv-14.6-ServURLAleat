#!/usr/bin/python3

"""
Pedro Arias Perez
ITT+IAA
 pariaspe @ alumnos.urjc.es
 SAT (Universidad Rey Juan Carlos)
"""

import webapp
import random


class aleat(webapp.webApp):
    def process(self, parsedRequest):
        num = random.randrange(999999999)
        html_answer = "<html><body><h1>Hola. <a href='" + str(num)
        html_answer += "'>Dame otra<a/></h1></body></html>"
        return ("200 OK", html_answer)

if __name__ == '__main__':
    miapp = aleat('0.0.0.0', 1234)
