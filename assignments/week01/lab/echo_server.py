import socket
import sys

# Create a function to sum the numbers from the users 
def num_sum(msg):
    """ This function resturns the sum of a list of integers """
    num_sum = 0
    for i in range(len(msg)):
        num_sum += int(msg[i])
    return num_sum

# Create a TCP/IP socket
echo_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 50000)
print >>sys.stderr, 'starting up on %s port %s' % server_address
echo_server.bind(server_address)

# Listen for incoming connections
echo_server.listen(1)

while True:
    # Wait for a connection
    print >>sys.stderr, 'waiting for a connection'
    connection, client_address = echo_server.accept()
    try:
        print >>sys.stderr, 'connection from', client_address

        # Receive the data
        message = connection.recv(1024)
        data = message.split(',')
        print >>sys.stderr, 'received "%s"' % data
        
        # Compute the sum
        return_data = str(num_sum(data))

        # Send the data back to the client
        print >>sys.stderr, 'sending return_data back to the client', return_data
        connection.sendall(return_data)
        

    finally:
        # Clean up the connection
        connection.close()
