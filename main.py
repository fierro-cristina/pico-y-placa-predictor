#Custom modules
from predictor import predict_pico_y_placa

def main():
    plate_num = input("Enter plate number in the format ABC-123 or ABC-1234: ")
    date = input("Enter circulation date in the format DD-MM-YYYY or DD/MM/YY: ")
    time = input("Enter circulation time in the format HH:MM : ")

    vehicle = predict_pico_y_placa(plate_num)
    if vehicle.check_if_restricted(date, time) == True:
        print("\nVehicle with plate number: " + plate_num + " is RESTRICTED on " + date + " at " + time + " from circulation because of 'PICO Y PLACA'.\n")
    elif vehicle.check_if_restricted(date, time) == False:
        print("\nVehicle with plate number: " + plate_num + " is ALLOWED to circulate on " + date + " at " + time + " according to 'PICO Y PLACA'.\nDrive Safely!\n")


if __name__ == "__main__":
    main()