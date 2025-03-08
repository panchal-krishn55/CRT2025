import socket

# Create a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define IP address and port (Change IP to your system's local IP)
server_ip = "192.168.96.254"  # Replace with your local IP
port = 1234

# Bind the socket to the address and port
server_socket.bind((server_ip, port))

# Listen for incoming connections (Allow 1 connection at a time)
server_socket.listen(1)
print(f"Server is listening on {server_ip}:{port}...")

# Accept a connection from a client
conn, addr = server_socket.accept()
print(f"Connected to {addr}")

while True:
    # Receive data from the client
    msg = conn.recv(1024).decode('ascii')  # ✅ Fixed recv method
    if not msg:
        break
    print(f"Client: {msg}")
    # Send a response back to the client
    reply = input("You: ")
    conn.send(reply.encode('ascii'))

# Close the connection
conn.close()
server_socket.close()












# set1={1,2,3}
# set2={2,5,6}
# print(set1.intersection(set2))a=5
# b=10
# a=8
# sum=a+b
# print(sum)
# return sum

# def calc_sum(a,b):
#     sum=a+b
#     print(sum)

# calc_sum(6,44)
    
# calc_sum(3,55)

# calc_sum(5,55)




# def calcu_mult(a,b,c):
#     mult=(a*b*c)
#     print(mult)
    
    
# calcu_mult(4,5,6)

# calcu_mult(2,3,4)

# calcu_mult(10,20,30)
# def habibi(a,b):
#     return a/b
# multiply=habibi(45,2)
# print(multiply)

# def calc_avg(a,b,c):
#     return a*b*c/3
# avaeage=calc_avg(7,6,4)
# print(avaeage)


# def cakc_multi(a,b=8):
#     print(a*b)
#     return (a*b)
# cakc_multi(5)

# cities=["dehli",
#         "mumbai"," jaipur"]
# def print_len(list):
#     print(len(list))
# print_len(cities)
    
    
# def print_list(list):
#     for item in list:
#         print(item,end=" ")
        
# print_list(cities)

# def calc_fact(n):
#     fact=1
#     for i in range(1,n+1):
#           fact*=i
#     print(fact)
# # calc_fact()
# def USD_to_INR(N):
#    XX=N*83
#    print(N,"usd=",XX,"INR")
# USD_to_INR(7)

# def show(n):
#    if(n==-1):
#       return
#    print(n)
#    show(n-1)
   
#    show(6)

