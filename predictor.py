from datetime import datetime

#Custom modules
from rules import rules
from utilities import utilities

class predict_pico_y_placa:

    @staticmethod
    def is_restricted_time_interval(time_str):

        restricted_interval = False

        time = utilities.validate_time_format(time_str)
        time = datetime.strptime(time_str, '%H:%M').time()
        AM_start, AM_end = rules.get_time_interval("AM")
        PM_start, PM_end = rules.get_time_interval("PM")
        if AM_start <= time <= AM_end:
            restricted_interval = True
        
        if PM_start <= time <= PM_end:
            restricted_interval = True
        
        return restricted_interval

    @staticmethod
    def day_cant_circulate(date_str, plate_number_str):

        allowed = True

        date_str = utilities.validate_date_format(date_str)
        day = utilities.get_iso_weekday(date_str)

        if day == 6 or day == 7:
            allowed = True

        plate_number_str = utilities.validate_plate_format(plate_number_str)
        last_num = plate_number_str[-1]
        last_num_plate = int(last_num)
        restricted_day = rules.cant_circulate_days()
        restricted_plate = restricted_day[day]

        if last_num_plate == restricted_plate[0] or last_num_plate == restricted_plate[1]:
            allowed = False
        else:
            allowed = True
        
        return allowed

    def __init__(self, plate_num_str):
        self.plate_num_str = plate_num_str

    def check_if_restricted(self, date_str, time_str):
        
        allowed = False

        if predict_pico_y_placa.day_cant_circulate(date_str, self.plate_num_str) == False and predict_pico_y_placa.is_restricted_time_interval(time_str) == True:
            allowed = True
            # print("\nVehicle with plate number: " + self.plate_num_str + " is RESTRICTED on " + date_str + " at " + time_str + " from circulation because of 'PICO Y PLACA'.\n")
        else:
            allowed = False
            # print("\nVehicle with plate number: " + self.plate_num_str + " is ALLOWED to circulate on " + date_str + " at " + time_str + " according to 'PICO Y PLACA'.\nDrive Safely!\n")

        return allowed



            
            


        