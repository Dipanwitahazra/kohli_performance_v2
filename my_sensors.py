acc= accelerometer(
    name="accelerometer",
    location="haldia",
    record_date="2023-01-19"
)

acc.add_data(
    data=acc_data,
    time=acc_time
)
print('Accelerometer data: ',acc.data)

class gyro(accelerometer):
    def show_sensor_type(self):
        print(f"This is {self.name} and the location is {self.location}")

        class GPS(Sensor):
    def __init__(self, name, location, record_date,brand):
        super().__init__( 
                name, location, record_date
                )
        self.brand = brand

gps = GPS(
    name="GPS",
    location="Haldia",
    record_date="2023-01-10",
    brand="espressif"
)
print(gps.name)
print(gps.location)
print(gps.record_date)
print(gps.brand)


    

