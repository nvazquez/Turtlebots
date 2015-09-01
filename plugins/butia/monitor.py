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

MONITOR_COLOR_NO_OP = ["#FE9A2E","#808080"]
MONITOR_COLOR_LOW = ["#FF0000","#808080"]
MONITOR_COLOR_MEDIUM = ["#0080FF","#808080"]
MONITOR_COLOR_HIGH = ["#0404B4","#808080"]

from monitor_elem import MonitorElem

class MonitorButia():

    def __init__(self):
        self.sensors = {
            'grey': [MonitorElem() for i in range(6)],
            'light':[MonitorElem() for i in range(6)],
            'distanc': [MonitorElem() for i in range(6)],
            'button': [MonitorElem() for i in range(6)],
            'motors': [MonitorElem() for i in range(8)]
        }
        self.sensors_name = ['grey', 'light', 'button', 'distanc','motors']

    def evaluate_result(self, sensor_name,sensor_port, sensor_result):
        self.sensors[sensor_name][int(sensor_port) - 1].evaluate_result(sensor_result)

    def get_monitor_evaluation(self):
        res = []
        for s in self.sensors_name:
            for i in range(6):
                if self.sensors[s][i].inuse == 1:
                    res.append((s,i+1,self.sensors[s][i].get_monitor_evaluation()))
        return res

    def activate_monitor(self,set_new_devices):
        for device in set_new_devices:
            print(device)
            words = device.split(":")
            if any(words[0] in s for s in self.sensors_name):
                self.sensors[words[0]][int(words[1])-1].activate()


    def desactivate_monitor(self,set_old_devices):
         for device in set_old_devices:
            print(device)
            words = device.split(":")
            if any(words[0] in s for s in self.sensors_name):
                self.sensors[words[0]][int(words[1])-1].unactivate()

    def reset(self):
        for i in self.sensors_name:
            for elem in self.sensors[i]:
                elem.reset()


