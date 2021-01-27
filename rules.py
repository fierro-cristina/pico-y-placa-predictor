from datetime import datetime

class rules:

    @staticmethod
    def cant_circulate_days():

        '''
        Days are number coded in the following manner:
        1 - Monday, 2 - Tuesday ... 7 - Sunday 
        '''

        days = {1:[1,2], 2:[3,4], 3:[5,6], 4:[7,8], 5:[9,0], 6:[None, None], 7:[None, None]}
        return days

    @staticmethod
    def cant_circulate_time():
        time_intervals = {"AM" : ["7:00", "9:30"], "PM":["16:00", "19:30"]}
        return time_intervals

    @staticmethod
    def get_time_interval(AM_or_PM):

        restricted_time = rules.cant_circulate_time()
        start = restricted_time[AM_or_PM][0]
        end = restricted_time[AM_or_PM][1]
        fmt = '%H:%M'
        start = datetime.strptime(start, fmt).time()
        end = datetime.strptime(end, fmt).time()
        
        return start, end

    

