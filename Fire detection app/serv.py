from socket import *
from threading import *
import time
import random


class ClientThread(Thread):
    def __init__(self, cSocket, cAddress):
        Thread.__init__(self)
        self.cSocket = cSocket
        self.cAddress = cAddress
        print("Connection successful from ", self.cAddress)

    def run(self):
        clientMsg = ""

        images = ["image1.jpg", "image2.jpg", "image3.jpg", "image4.jpg", "image5.jpg", "image6.jpg", "image7.jpg",
                  "image8.jpg", "image9.jpg",
                  "image10.jpg", "image11.jpg", "image12.jpg", "image13.jpg", "image14.jpg", "image15.jpg",
                  "image16.jpg", "image17.jpg", "image18.jpg"]


        while "!DISCONNECT" not in clientMsg:

            temp0 = str(random.randint(0, 39))
            humidity0 = str(random.randint(0, 39))
            sensorid0 = str(5.0)

            temp1 = str(random.randint(0, 39))
            humidity1 = str(random.randint(0, 39))
            sensorid1 = str(2.0)

            temp2 = str(random.randint(0, 39))
            humidity2 = str(random.randint(0, 39))
            sensorid2 = str(66.145)


            accuracy = str(random.randint(0, 99)) + "%"
            image_number = random.randint(0, 17)
            image_name = images[image_number]

            fire_notification = "1"

            send_list = [[[accuracy,image_name,fire_notification],[sensorid0,temp0,humidity0],[sensorid1,temp1,humidity1],[sensorid2,temp2,humidity2]]]

            send_str = ''.join(str(item) for item in send_list)
            self.cSocket.send(send_str.encode())

            clientMsg = self.cSocket.recv(1024).decode()

            print(clientMsg)

            time.sleep(2) # The time will be arranged


        print("Disconnected from ", self.cAddress)
        self.cSocket.close()


if __name__ == "__main__":
    HOST = "127.0.0.1"
    PORT = 4000

    socket = socket(AF_INET, SOCK_STREAM)
    socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    socket.bind((HOST, PORT))
    while True:
        socket.listen()
        cSocket, cAddress = socket.accept()
        newClient = ClientThread(cSocket, cAddress)
        newClient.start()
