from socket import *

server = ("192.168.2.2", 5004) # --server info-- 

# client socket
clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.connect(server) # connet TCP ye ozel 

# get SQL query
print ("Please enter your SQL query. \n like :")
## select Company, Url from Google_Analytics.Categories_Hourly as GA where GA.Rate = 1;      
print ("SELECT Company, Hour_of_Day, Rate, Article_id, Url FROM Google_Analytics.Categories_Hourly LIMIT 10;")
mssg = raw_input('>>>')

# send SQL message
clientSocket.send(mssg) 

# get response from server
data = clientSocket.recv(1024)
print ("[INFO] From server:\n" + str(data)) 

# close socket
clientSocket.close()