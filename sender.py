import socket

# Create a TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define server IP and port (must match the server's IP and port)
server_ip = "192.168.96.254"  # Use the server's local IP
port = 1234

# Connect to the server
client_socket.connect((server_ip, port))  # ✅ Must establish a connection first
print(f"Connected to {server_ip}:{port}")

while True:
    # Send message to the server
    message = input("You: ")
    client_socket.send(message.encode('ascii'))

    # Receive reply from the server
    reply = client_socket.recv(1024).decode('ascii')
    print(f"Server: {reply}")

# Close the connection
client_socket.close()
























# # # info = {
# # #     "key":"i_mkrishnpanchal",
# # #     "name" :"shradhaakhapra",
# # #     "learn":"DSA",
# # #     "subjects": ("A","b","c"),
# # #     "surename":"lodha"
# # # }
# # # print(info["key"])
# # # print(info["name"])
# # # print(info["learn"])
# # # print(info["subjects"])
# # # print(info["surname"])
# # # null_dict={}

# # # # info["name"]="Narendra"#over write
# # # # print("surename")
# # # # student={
# # # #     "name": "Ruhal kumar",
# # # #     "subjects":{
# # # #         "phy":56,
# # # #         "chem":89,
# # # #         "math" :78
# # # #     }
# # # # }
# # # # null_dict = {}
# # # # null_dict["name"]="apana college"
# # # # print(null_dict)

# # student={
# #     "name":"Krishn Kumar",
# #     "subject" : {
# #         "phy": 97,
# #         "chem": 98,
# #         "math": 95,
# #         "Bio": 99,
        
# #     }}
# # print(student["subject"]["chem"])
# # print(len(student))
# # pair1=list(student.items())
# # print(pair1[0])
# # print(student.get("name11"))
# # print(student["name11"])

# #UPDATE 
# # new_dict={"Sidhi bachchi":"komal soni","age": "19","mammi ji":"durgesh Devi"}
# # student.update(new_dict)
# # print(student)
# # first=int(input ("enter the first num"))

# # second =int(input ("enter the second num"))

# # print("the sumcis", first+second)
# # # # #sets
# collection={1,2,3,4555,"harish","harish","harish",83895,89465,"harish"}
# print(type(collection))
# print(type(collection))
# # # # # # print(len(collection))
# # # # # #cr3eate a empty set
# # # # # collection=set()
# # # # # collection.add("ramesh")
# # # collection.add(45)
# # # # # # collection.add("ramhari")
# # # # # # collection.add((1,2,3))
# # # print(collection)

# # # # # # collection.remove(1)
# # # # # print(len(collection))


# set1={1,2,3}
# set2={2,5,6}
# print(set1.intersection(set2))
# # # dict={
# # #     "cat":"small animal",
# # #     "table":["a piese of ferniture","34400 ka takhat"]
# # # }
# # # print(dict)

# # dictionary={
# #     "value":"d"
    
# # }
# # print(type(dictionary))
