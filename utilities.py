from datetime import datetime
import re

class utilities:

    @staticmethod
    def validate_plate_format(plate_number):
        if re.match(r'^[A-Z]{3}[-/]\d{3,4}$', plate_number):
            return plate_number
        else:
            raise ValueError("Plate number does not match ECUADOR standard.")

    @staticmethod
    def validate_date_format(date_str):
        try:
            r = re.compile(r'(\d+)[-/](\d+)[-/](?:20)?(\d+)')
            date_ = r.sub(r"\1/\2/20\3", date_str)
            date_formatted = datetime.strftime(datetime.strptime(date_, '%d/%m/%Y'), '%d/%m/%Y')
            return date_formatted 
        except ValueError:
           pass

        raise ValueError("Unkown date format.")
        
    @staticmethod
    def validate_time_format(time_str):
        fmt = '%H:%M'
        try:
            valid_time = datetime.strptime(time_str, fmt)
            return time_str
        except ValueError:
            pass
        raise ValueError ("Invalid time format.")

    @staticmethod
    def get_iso_weekday(date_str):
        date = datetime.strptime(date_str, '%d/%m/%Y')
        day = date.isoweekday()
        return day