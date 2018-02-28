import os, csv

class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.photo_file_name = photo_file_name
        self.brand = brand
        self.carrying = carrying

    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[1]


class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = "car"
        self.passenger_seats_count = int(passenger_seats_count)        
    

class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = "truck"
        if body_whl == '': body_whl = '0x0x0'
        self.body_width = float(body_whl.split('x')[0])
        self.body_height = float(body_whl.split('x')[1])
        self.body_length = float(body_whl.split('x')[2])
    
    def get_body_volume(self):
        return self.body_width * self.body_height * self.body_length


class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = "spec_machine"
        self.extra = extra
        


def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename, 'r') as csv_f:
        reader_s = csv.reader(csv_f, delimiter=';')
        for row in reader_s:
            if (row[0:1] == ['']) or (row[1:2] == ['']) or (row[3:4] == ['']) or (row[5:6] == ['']):
                continue
            else:
                if row[0:1] == ['car']:
                    if row[2:3] == ['']:
                        continue
                    else:
                        car_list.append(Car(''.join(row[1:2]), ''.join(row[3:4]), ''.join(row[5:6]), ''.join(row[2:3])))                       
                elif row[0:1] == ['truck']:
                    car_list.append(Truck(''.join(row[1:2]), ''.join(row[3:4]), ''.join(row[5:6]), ''.join(row[4:5])))
                elif row[0:1] == ['spec_machine']:
                    car_list.append(SpecMachine(''.join(row[1:2]), ''.join(row[3:4]), ''.join(row[5:6]), ''.join(row[6:7])))
    return car_list