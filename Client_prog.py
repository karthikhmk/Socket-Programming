#client prog
#
# @karthik

from socket import *                   # Import socket module

s = socket(AF_INET,SOCK_STREAM)            # Create a socket object
host = raw_input('Input server IP address:')   # Get local machine name
port = 23456                   # Reserve a port for your service.

def main():
    connect()

def connect():
    print 'connecting to',host
    s.connect((host, port))                 #connect to host ex.127.0.0.1
    print 'connected'
    s.send("Hello server!")
    send_file()
    
def send_file():
    #while True:
        filename='test.txt'
        print 'sending file',filename
        f = open(filename,'rb')
        l = f.read(2024)
        while (l):
           s.send(l)
           print'Sent',filename
           l = f.read(2024)
        f.close()
        print'Done sending'
        print 'closing connection to',host
        print 'exiting program'
        s.close()

if __name__ == "__main__":
    main()
