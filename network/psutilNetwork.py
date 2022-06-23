import psutil


def print_io_counter():
    """
     :return: io counter
    """
    return ["io counter",psutil.net_io_counters()]

def print_io_connection():
    """
    :return: io connection
    """
    return ["io connection",psutil.net_connections()]


def print_net_adress():
    """
    :return: net adress
    """
    return ["net adress",psutil.net_if_addrs()]

def print_net_stat():
    """
    :return: net stats
    """
    return ["net stats",psutil.net_if_stats()]


def print_all_info():
    """
    :return: all network info
    """
    all_info = []

    all_info.append(print_io_counter())
    #all_info.append(print_io_connection())
    all_info.append(print_net_adress())
    all_info.append(print_net_stat())

    return all_info
