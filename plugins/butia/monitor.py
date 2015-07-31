# MONITOR BUTIA
# FING
# GRUPO 9
# 2015

# (MONITOR_BUTIA) Distinguimos segun el tipo de error
ERROR_BOARD_DISCONECTED = -100
ERROR_MODULE_NOT_PRESENT = -101
ERROR_EXCEPTION = -102
ERROR = -1

from monitor_elem import MonitorElem

class MonitorButia():

    def __init__(self):
        self.sensors = {
            'grey' : MonitorElem(),
            'light' : MonitorElem(),
            'distance' : MonitorElem(),
            'button' : MonitorElem(),
            'motors' : MonitorElem()
        }

    def evaluate_result(self, sensor_name, sensor_result):
        self.sensors[sensor_name].evaluate_result(sensor_result)