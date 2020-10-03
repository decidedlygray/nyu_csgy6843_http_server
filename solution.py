#import socket module
from socket import *
import sys # In order to terminate the program

def webServer(port=13331):
    serverSocket = socket(AF_INET, SOCK_STREAM)

    #Prepare a sever socket
    #Fill in start
    # serverSocket.bind((gethostname(), port))
    serverSocket.bind(('127.0.0.1', port))
    #Fill in end

    while True:
        #Establish the connection
        print('Ready to serve...')
        # connectionSocket, addr = #Fill in start      #Fill in end
        connectionSocket, addr = serverSocket.accept()
        try:
            # message = #Fill in start    #Fill in end
            message = connectionSocket.recv(1024)
            # print('DBG:: {}'.format(message))

            filename = message.split()[1]
            f = open(filename[1:])
            # outputdata = #Fill in start     #Fill in end
            outputdata = f.read()

            #Send one HTTP header line into socket
            #Fill in start
            connectionSocket.send('HTTP/1.1 200 OK\r\n')
            #Fill in end

            #Send the content of the requested file to the client
            for i in range(0, len(outputdata)):
                connectionSocket.send(outputdata[i].encode())

            connectionSocket.send("\r\n".encode())
            connectionSocket.close()
        except IOError:
            #Send response message for file not found (404)
            #Fill in start
            connectionSocket.send('HTTP/1.1 404 Not Found\r\n')
            #Fill in end

            #Close client socket
            #Fill in start
            connectionSocket.close()
            #Fill in end

    serverSocket.close()
    sys.exit()  # Terminate the program after sending the corresponding data

if __name__ == "__main__":
    webServer(13331)
