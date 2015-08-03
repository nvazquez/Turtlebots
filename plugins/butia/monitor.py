# MONITOR BUTIA
# FING
# GRUPO 9
# 2015

# (MONITOR_BUTIA) Distinguimos segun el tipo de error
ERROR_BOARD_DISCONECTED = -100
ERROR_MODULE_NOT_PRESENT = -101
ERROR_EXCEPTION = -102
ERROR = -1

MONITOR_RETURN_TYPE_NO_OP = 0
MONITOR_RETURN_TYPE_LOW = 1
MONITOR_RETURN_TYPE_MEDIUM = 2
MONITOR_RETURN_TYPE_HIGH = 3

MONITOR_COLOR_NO_OP = ["#FE9A2E","#DF7401"]
MONITOR_COLOR_LOW = ["#00FFFF","#01DFD7"]
MONITOR_COLOR_MEDIUM = ["#0080FF","#0174DF"]
MONITOR_COLOR_HIGH = ["#0404B4", "#08088A"]

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

    def get_monitor_evaluation(self):
        elem_grey = self.sensors['grey'].get_monitor_evaluation()
        elem_light = self.sensors['light'].get_monitor_evaluation()
        elem_distance = self.sensors['distance'].get_monitor_evaluation()
        elem_button = self.sensors['button'].get_monitor_evaluation()
        elem_motors = self.sensors['motors'].get_monitor_evaluation()
        sensors_hash = {
            'grey' : elem_grey,
            'light' : elem_distance,
            'distance' : elem_distance,
            'button' : elem_button,
            'motors' : elem_motors
        }
        return sensors_hash