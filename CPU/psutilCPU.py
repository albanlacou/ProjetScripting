import psutil
import logging


#def print_cpu_time():

  #  return ["CPU time:",psutil.cpu_times()]


def print_cpu_percent():

    """
    print the cpu percent
    :return: cpu percent
    """
    return ["CPU percent:",psutil.cpu_percent(interval=1)]

def print_cpu_count():
    """
    print the cpu percent
    :return: cpu percent
    """
    return ["CPU count",psutil.cpu_count()]

#def print_cpu_stat():
    """
    print the cpu stats
    :return: cpu stats
    """
 #   return ["CPU stats",psutil.cpu_stats()]

#def print_cpu_freq():
    """
    return cpu freq
    :return: cpu freq
    """
 #   return ["cpu freq",psutil.cpu_freq()]

#def print_cpu_avg():
    """
    return cpu avg
    :return: cpu avg
    """
 #   return ["cpu avg",psutil.getloadavg()]


def get_all_info_cpu():
    allinfo = []

   # allinfo.append(print_cpu_time())
    allinfo.append(print_cpu_percent())
    allinfo.append(print_cpu_count())
   # allinfo.append(print_cpu_stat())
   # allinfo.append(print_cpu_freq())
   # allinfo.append(print_cpu_avg())

    return allinfo



