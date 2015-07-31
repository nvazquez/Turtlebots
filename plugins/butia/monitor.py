# MONITOR BUTIA
# FING
# GRUPO 9
# 2015

# (MONITOR_BUTIA) Distinguimos segun el tipo de error
ERROR_BOARD_DISCONECTED = -100
ERROR_MODULE_NOT_PRESENT = -101
ERROR_EXCEPTION = -102
ERROR = -1

class MonitorButia():

    def __init__(self):
        self.count_board_disconected = 0
        self.count_module_not_present = 0
        self.count_error_exception = 0
        self.count_error_butia = 0

    def evaluate_result(self, result):
        if result == ERROR_BOARD_DISCONECTED:
            self.count_board_disconected += 1
        else:
            if result == ERROR_MODULE_NOT_PRESENT:
                self.count_module_not_present += 1
            else:
                if result == ERROR_EXCEPTION:
                    self.count_error_exception += 1
                else:
                    if result == ERROR:
                        self.count_error_butia += 1
                    #else, valor normal, ver si lo contamos tambien

    def get_count_board_disconected(self):
        return self.count_board_disconected