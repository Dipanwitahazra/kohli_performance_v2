from sensorModule import Accelerometer,Gyro,GPS
import numpy as np


acc=Accelerometer(
    name="Accelerometer",
    location="Haldia",
    record_date="2023-01--10"
)
gyro=Gyro(
    name="gyroscope",
    location="chennai",
    record_date="6878-89798-987",
    brand="hghbhj"

)


gps=GPS(
    name="GPS",
    location="Chennai",
    record_date="2023-01-10",
    brand="espressif"
)

time=np.arange(10)
acc_data=np.random.randint(-10,10,10)
gyro_data=np.random.randint(-15,15,10)
gps_data=np.random.randint(-12,12,10)

print(acc.name)
print(acc.location)
print(acc.record_date)
acc.add_data(
    data=acc_data,
    time=time
)


print(gyro.name)
print(gyro.location)
print(gyro.record_date)
gyro.add_data(
    data=gyro_data,
    time=time
)

print(gps.name)
print(gps.location)
print(gps.record_date)
print(gps.brand)
gps.add_data(
    data=gps_data,
    time=time
)