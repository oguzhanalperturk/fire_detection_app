from flask import Flask, render_template, redirect, jsonify, url_for
import ast
import random
from socket import *
import time

# __name__ referring local python file that you are working on
app = Flask(__name__)

#HOST = "192.168.0.109"
#HOST = "169.254.252.160"
HOST = "127.0.0.1"

PORT = 4000


@app.route('/')
def initial():
    return redirect('/main')

@app.route('/main')
def home_page():
    return render_template('main.html')


@app.route('/start_sensing')
def makeCommunication():
    global s
    s = socket(AF_INET, SOCK_STREAM)
    s.connect((HOST, PORT))
    return redirect(url_for("information_page"))



# first data is image name. The image will be send here when fire is detected.
# image_name - fire notification
# Data Order: fire_notification - sensor_id - raspberrypi_id - location - temperature - humidity - accuracy
random_decimals = []

@app.route('/update_decimal', methods=['POST'])
def updatedecimal():

    start_time = time.time()

    # receive data
    serverMsg = s.recv(1024).decode()

    # send confirmation (necessary to send something)
    s.send("received".encode())

    random_decimal = 0
    random_decimal2 = 0
    random_decimal4 = 0
    random_decimal5 = 0
    random_decimal6 = 0
    random_decimal7 = 0

    nested_array = ast.literal_eval(serverMsg)

    fire_notification = nested_array[0][2]
    server_image = nested_array[0][1]
    accuracy = nested_array[0][0]

    for i in nested_array:
        sens_id = i[0]
        if(sens_id == "5.0"):
            random_decimal = i[1] # temp
            random_decimal2 = i[2].replace("\n","") # humidity
        elif(sens_id == "2.0"):
            random_decimal4 = i[1]  # temp
            random_decimal5 = i[2].replace("\n","") # humidity
        else:
            random_decimal6 = i[1]  # temp
            random_decimal7 = i[2].replace("\n","") # humidity


    images = ["image1.jpg", "image2.jpg", "image3.jpg", "image4.jpg", "image5.jpg", "image6.jpg", "image7.jpg", "image8.jpg", "image9.jpg",
              "image10.jpg", "image11.jpg", "image12.jpg", "image13.jpg", "image14.jpg", "image15.jpg", "image16.jpg", "image17.jpg", "image18.jpg"]

    image_number = random.randint(0, 17)

    fire_notification = [fire_notification, 0, 0]

    fire_notification_str = ""
    for i in fire_notification:
        fire_notification_str += str(i) + ";"
    fire_notification_str = fire_notification_str[:-1]

    received_image_data = [server_image,
                           images[image_number], images[image_number]]
    fire_images_str = ""
    for i in received_image_data:
        fire_images_str += str(i) + ";"
    fire_images_str = fire_images_str[:-1]

    # Blank strings should be added for accuracy
    random_decimals = [fire_images_str, [fire_notification_str],
                       5.0, 1, "Kalkanli", random_decimal, random_decimal2,accuracy,
                       2.0, 1, "Kalkanli", random_decimal4, random_decimal5,"",
                       66.145, 1, "Kalkanli", random_decimal6, random_decimal7,""]


    for i in range(2, len(random_decimals)):

        if ((i-2) % 6 == 0):
            sensor_id = random_decimals[i]
        elif ((i-2) % 6 == 1):
            rasp_id = random_decimals[i]
        elif ((i-2) % 6 == 3):
            index1 = i
        elif ((i-2) % 6 == 4):
            index2 = i
        elif((i-2) % 6 == 5):
            if(random_decimals[i] != ""):
                index3 = i

            saveFile(random_decimals, rasp_id,sensor_id, index1, index2, index3)

    end_time = time.time()
    print(end_time - start_time)

    return jsonify('', render_template('random_decimal_model.html', x=random_decimals))


@app.route('/information')
def information_page():
    return render_template('information.html', x=random_decimals)

@app.route('/stop_sensing')
def stop_sensing():
    s.send("!DISCONNECT".encode())
    return redirect(url_for("home_page"))

@app.route('/fire_image')
def display_image_page():
    return render_template('display_image.html', x=random_decimals)

def saveFile(random_decimals, rasp_id, sensor_id, index1, index2, index3):
    filename = "raspberrypi_" + \
        str(rasp_id) + "_sensor_" + str(sensor_id) + ".txt"

    file = open(filename, "a")

    line = str(random_decimals[index1]) + ";" + str(random_decimals[index2]) + ";" + str(random_decimals[index3]) + "\n"

    file.writelines(line)

    file.close()

app.run(debug=True)
