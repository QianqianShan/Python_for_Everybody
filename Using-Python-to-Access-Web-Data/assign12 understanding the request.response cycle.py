# Exploring the HyperText Transport Protocol

# You are to retrieve the following document using the HTTP protocol
# in a way that you can examine the HTTP Response headers.

# http://data.pr4e.org/intro-short.txt
#There are three ways that you might retrieve this web page and look at the response headers:

# 1.Preferred: Modify the socket1.py program to retrieve the above URL and print out the headers and data.
# Make sure to change the code to retrieve the above URL - the values are different for each URL.
# 2.Open the URL in a web browser with a developer console or FireBug and manually examine the headers that are returned.
# 3.Use the telnet program as shown in lecture to retrieve the headers and content.

import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org',80))  # make a connection to port 80 on the server
mysock.send('GET http://data.pr4e.org/intro-short.txt HTTP/1.0\n\n') #we must send the GET command followed by a blank line.

while True:
    data=mysock.recv(512)
    if (len(data)<1):
        break
    print data

mysock.close()
