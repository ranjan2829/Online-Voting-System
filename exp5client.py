import socket

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()
port = 9999

# connection to hostname on the port
s.connect((host, port))

# Receive no more than 1024 bytes
tm = s.recv(1024)

# Close the socket after receiving
s.close()

# Print the time received from the server
print("The time got from the server is %s" % tm.decode('ascii'))
