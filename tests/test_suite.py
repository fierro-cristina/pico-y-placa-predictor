from unittest import TestCase, main

# Custom modules
from predictor import predict_pico_y_placa
from utilities import utilities

class test_pico_placa_predictor(TestCase):

    def setUp(self):
        self.plate_1 = predict_pico_y_placa("PPD-0228")

    def test_predictor(self):
        self.assertTrue(self.plate_1.check_if_restricted("28/01/2021", "16:35"))
        self.assertTrue(self.plate_1.check_if_restricted("08-04-2021", "09:15"))
        self.assertFalse(self.plate_1.check_if_restricted("27/01/2021", "07:15"))
        self.assertFalse(self.plate_1.check_if_restricted("05-12-2021", "17:22"))
    
    def test_pico_y_placa_monday(self):
        self.assertIs(predict_pico_y_placa.day_cant_circulate("01/02/2021", "PDF-1221"), False)
        self.assertIs(predict_pico_y_placa.day_cant_circulate("25-10-2021", "GYD-402"), False)
        self.assertIs(predict_pico_y_placa.day_cant_circulate("15/02/2021", "PBD-1203"), True)
        self.assertIs(predict_pico_y_placa.day_cant_circulate("14-06-2021", "PPD-874"), True)

    def test_pico_y_placa_tuesday(self):
        self.assertIs(predict_pico_y_placa.day_cant_circulate("09/02/2021", "IBY-0433"), False)
        self.assertIs(predict_pico_y_placa.day_cant_circulate("20-07-2021", "PCD-884"), False)
        self.assertIs(predict_pico_y_placa.day_cant_circulate("20/04/2021", "CHG-0522"), True)
        self.assertIs(predict_pico_y_placa.day_cant_circulate("25-05-2021", "IBY-171"), True)

    def test_pico_y_placa_wednesday(self):
        self.assertIs(predict_pico_y_placa.day_cant_circulate("17/02/2021", "PPD-9745"), False)
        self.assertIs(predict_pico_y_placa.day_cant_circulate("01-09-2021", "PXW-306"), False)
        self.assertIs(predict_pico_y_placa.day_cant_circulate("10/03/2021", "CYX-2077"), True)
        self.assertIs(predict_pico_y_placa.day_cant_circulate("07-07-2021", "TGF-929"), True)

    def test_pico_y_placa_thursday(self):
        self.assertIs(predict_pico_y_placa.day_cant_circulate("11/02/2021", "PPD-7898"), False)
        self.assertIs(predict_pico_y_placa.day_cant_circulate("13-05-2021", "CXY-217"), False)
        self.assertIs(predict_pico_y_placa.day_cant_circulate("10/06/2021", "INP-3100"), True)
        self.assertIs(predict_pico_y_placa.day_cant_circulate("27-08-2021", "GHI-564"), True)

    def test_pico_y_placa_friday(self):
        self.assertIs(predict_pico_y_placa.day_cant_circulate("29/01/2021", "EMI-1990"), False)
        self.assertIs(predict_pico_y_placa.day_cant_circulate("21-05-2021", "CML-259"), False)
        self.assertIs(predict_pico_y_placa.day_cant_circulate("23/07/2021", "PPM-1577"), True)
        self.assertIs(predict_pico_y_placa.day_cant_circulate("15-10-2021", "CTI-254"), True)

    def test_pico_y_placa_weekends(self):
        self.assertIs(predict_pico_y_placa.day_cant_circulate("13/03/2021", "CML-219"), True)
        self.assertIs(predict_pico_y_placa.day_cant_circulate("02-10-2021", "PPI-9780"), True)
        self.assertIs(predict_pico_y_placa.day_cant_circulate("28/11/2021", "ETR-578"), True)
        self.assertIs(predict_pico_y_placa.day_cant_circulate("05-12-2021", "PDS-0142"), True)

class test_pico_placa_predictor_time(TestCase):

    def test_pico_y_placa_time_morning(self):
        self.assertTrue(predict_pico_y_placa.is_restricted_time_interval("09:05"))
        self.assertTrue(predict_pico_y_placa.is_restricted_time_interval("07:18"))
        self.assertFalse(predict_pico_y_placa.is_restricted_time_interval("10:45"))
        self.assertFalse(predict_pico_y_placa.is_restricted_time_interval("11:22"))

    def test_pico_y_placa_time_evening(self):
        self.assertTrue(predict_pico_y_placa.is_restricted_time_interval("16:35"))
        self.assertTrue(predict_pico_y_placa.is_restricted_time_interval("18:05"))
        self.assertFalse(predict_pico_y_placa.is_restricted_time_interval("14:20"))
        self.assertFalse(predict_pico_y_placa.is_restricted_time_interval("19:35"))

class test_input_validators(TestCase):

    def test_date_plate_format_validator(self):
        self.assertRaises(ValueError, utilities.validate_plate_format, "XYZW-1234")
        self.assertRaises(ValueError, utilities.validate_plate_format, "A-123")
        self.assertRaises(ValueError, utilities.validate_plate_format, "PPD-18630")
        self.assertRaises(ValueError, utilities.validate_plate_format, "")

    def test_date_format_validator(self):
        self.assertRaises(ValueError, utilities.validate_date_format, "12.03.2021")
        self.assertRaises(ValueError, utilities.validate_date_format, "2021/03/12")
        self.assertRaises(ValueError, utilities.validate_date_format, "12032021")
        self.assertRaises(ValueError, utilities.validate_date_format, "")

    def test_time_format_validator(self):
        self.assertRaises(ValueError, utilities.validate_time_format, "07:30:00")
        self.assertRaises(ValueError, utilities.validate_time_format, "1600")
        self.assertRaises(ValueError, utilities.validate_time_format, "11-30")
        self.assertRaises(ValueError, utilities.validate_time_format, "")

if __name__ == "__main__":
    main()