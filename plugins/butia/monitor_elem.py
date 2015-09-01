# MONITOR BUTIA
# FING
# GRUPO 9
# 2015

from monitor import ERROR_BOARD_DISCONECTED
from monitor import ERROR_MODULE_NOT_PRESENT
from monitor import ERROR_EXCEPTION
from monitor import ERROR
from monitor import MONITOR_RETURN_TYPE_NO_OP
from monitor import MONITOR_RETURN_TYPE_LOW
from monitor import MONITOR_RETURN_TYPE_MEDIUM
from monitor import MONITOR_RETURN_TYPE_HIGH

class MonitorElem():

    def __init__(self):
        self.count_board_disconected = 0
        self.count_module_not_present = 0
        self.count_error_exception = 0
        self.count_error_butia = 0
        self.count_total = 0
        self.inuse = 0

    def evaluate_result(self, result):
        self.count_total += 1
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

    def get_monitor_evaluation(self):
        list = [self.count_board_disconected, self.count_module_not_present, self.count_error_exception, self.count_error_butia]
        max_error = max(list)
        if self.count_total != 0:
            avg_error = max_error / self.count_total
            if avg_error < 0.25:
                return MONITOR_RETURN_TYPE_LOW
            else:
                if avg_error < 0.5:
                    return MONITOR_RETURN_TYPE_MEDIUM
                else:
                    return MONITOR_RETURN_TYPE_HIGH
        return MONITOR_RETURN_TYPE_NO_OP

    def activate(self):
        self.count_board_disconected = 0
        self.count_module_not_present = 0
        self.count_error_exception = 0
        self.count_error_butia = 0
        self.count_total = 0
        self.inuse = 1

    def unactivate(self):
        self.inuse = 0

    def reset(self):
        if self.inuse == 1:
            self.count_board_disconected = 0
            self.count_module_not_present = 0
            self.count_error_exception = 0
            self.count_error_butia = 0
            self.count_total = 0

