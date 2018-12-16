from socket import *
import pymysql
import json

class DataBase:
    def __init__(self):
        self.connection = pymysql.connect()

    def runSQLquery(self, query):
        with self.connection.cursor() as cur:
            #cur.execute("""select league_id from test_leagues where name = '%s' """ % (name))
            cur.execute(query)
            result = cur.fetchall()
            cur.close()
        
        return result


serverPort = 5004

# Define a socket and bind it
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("", serverPort))

serverSocket.listen(1) # listen...
db = DataBase() # create database object to run queries
print ("Server Started!") 

while True:
    connectionSocket, addr = serverSocket.accept() # accept connection
    print("[INFO] Connection from ", str(addr), ", ", str(connectionSocket))
    mssg = connectionSocket.recv(1024) # receive SQL query from client
    print("Query: " + mssg)
    
    # run query
    operation = mssg.split(' ')[0]
    response = '-response-'
    if operation.upper() != 'SELECT' :
        response = 'Yok oyle yagma!'
    else:
        try:
            jsn = {}
            response = db.runSQLquery(mssg)
            for i, row in enumerate(response):
                jsn[str(i)] = row
            response = json.dumps(jsn, ensure_ascii=False, encoding='utf8', indent=4)
        except Exception as e:
            response = 'Error'
    # send result to client
    connectionSocket.send(response)
    connectionSocket.close()

serverSocket.close()