import socket
import sys

# Create a function for requesting numbers from the users 
def get_num():
    """ This function takes two numbers 'x' and 'y' and returns a string """
    list_num = raw_input(' Please enter two comma seperated numbers > ')
    return list_num

# Create a TCP/IP socket
echo_client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 50000)
echo_client.connect(server_address)

try:
    
    # Send data
    message = get_num()
    print >>sys.stderr, 'sending "%s"' % message
    echo_client.sendall(message)

    # receive the response from the server
    data = echo_client.recv(1024)

    # print the response
    print >>sys.stderr, 'Computed sum of %s is "%s"' % (message, data)

finally:
    # close the socket to clean up
    print >>sys.stderr, 'closing socket'
    echo_client.close()

