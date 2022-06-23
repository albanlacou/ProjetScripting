import psutil


def print_sensor_temperature():
    """
    :return: sensor temperature
    """
    return ["sensor temperature",psutil.sensors_temperatures()]

def print_sensor_fans():
    """
    :return: sensor fans
    """
    return ["sensor fans",psutil.sensors_fans()]

def print_sensor_battery():
    """
    :return: sensor battery
    """
    return ["sensor battery",psutil.sensors_battery()]

def print_all_info():
    """
    :return: print all info
    """

    allinfos = []

    #allinfos.append(print_sensor_temperature())
    #allinfos.append(print_sensor_fans())
    allinfos.append(print_sensor_battery())

    return allinfos

