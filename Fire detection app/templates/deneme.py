import ast
import random

string = "[[[1,'selam',3],[1,2,3],[2,3,4],[5,6,7]]]"
nested_array = ast.literal_eval(string)

print(nested_array)

temp0 = str(random.randint(0, 9))
humidity0 = str(random.randint(0, 9))
sensorid0 = str(5.0)

temp1 = str(random.randint(0, 9))
humidity1 = str(random.randint(0, 9))
sensorid1 = str(5.0)

temp2 = str(random.randint(0, 9))
humidity2 = str(random.randint(0, 9))
sensorid2 = str(5.0)


accuracy = str(random.randint(0, 99)) + "%"
image_number = random.randint(0, 17)
image_name = "image.txt"

fire_notification = "1"

send_list = [[[accuracy,image_name,fire_notification],[sensorid0,temp0,humidity0],[sensorid1,temp1,humidity1],[sensorid2,temp2,humidity2]]]

send_str = ''.join(str(item) for item in send_list)

print(send_str)