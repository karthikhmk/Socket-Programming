#server prog
#
# @Karthik

import socket                   # Import socket module
port = 23456                    # Reserve a port for your service.
s = socket.socket()   # Create a socket object
host =''
s.bind((host, port))            # Bind to the port
s.listen(5)                     # Now wait for client connection.

def main():
    print 'listening on TCP port',port
    print 'listening for new connection'

if __name__ == "__main__":
    main()

conn, addr = s.accept()     # Establish connection with client.
print 'connecting from',addr

#receive file
with open('received_file', 'wb') as f:
    print 'file opened'
    while True:
        print 'recieving file',
        data = conn.recv(1024)
        print'data=', data
        print 'received successfully'
        if not data:
            break
        # write data to a file
        f.write(data)

print 'closing connection from',addr
f.close()
s.close()
print('connection closed')
