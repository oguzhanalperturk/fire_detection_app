import fire_detection_app

def readFile(filename):
    try:
        file = open(filename, "r")
        records = file.readline()
        file.close()
        print(records)
        return records
    except:
        print("Error happened in opening the file")
        exit(1)

def test_saveFile():
    random_decimals_variation_1 = [
        "fire_images", ["fire_notification"],
        10, 1, "Girne", 20.5, 15.25, "85%",
        2, 1, "Kalkanli", 5.43, 14.32, "",
        1, 2, "Kutahya", 18.90, 4.56, "",
        2, 2, "Kutahya", 7.65, 22.11, "92%",
        1, 3, "Kyrenia", 24.56, 10.98, "",
        2, 3, "Kyrenia", 5.43, 19.87, ""
    ]

    fire_detection_app.saveFile(random_decimals_variation_1, 1, 1,5,6,7)
    fire_detection_app.saveFile(random_decimals_variation_1, 1, 4, 11, 12, 7)
    fire_detection_app.saveFile(random_decimals_variation_1, 2, 3, 17, 18,7)
    fire_detection_app.saveFile(random_decimals_variation_1, 2, 5, 23, 24, 25)
    fire_detection_app.saveFile(random_decimals_variation_1, 3, 6, 29, 30, 25)
    fire_detection_app.saveFile(random_decimals_variation_1, 3, 7, 35, 36, 25)


    assert readFile("raspberrypi_1_sensor_1.txt") == "20.5;15.25;85%\n"
    assert readFile("raspberrypi_1_sensor_4.txt") == "5.43;14.32;85%\n"
    assert readFile("raspberrypi_2_sensor_3.txt") == "18.9;4.56;85%\n"
    assert readFile("raspberrypi_2_sensor_5.txt") == "7.65;22.11;92%\n"
    assert readFile("raspberrypi_3_sensor_6.txt") == "24.56;10.98;92%\n"
    assert readFile("raspberrypi_3_sensor_7.txt") == "5.43;19.87;92%\n"











