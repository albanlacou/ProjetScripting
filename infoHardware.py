import argparse
import time
import logging

import CPU.psutilCPU as cpu
import Disks.psutilDisks as disks
import Memory.psutilMemory as mem
import network.psutilNetwork as net
import sensors.psutilSensor as sens

global frequence

frequence = 0
logging.basicConfig()

parser = argparse.ArgumentParser()

parser.add_argument("-f", "--frequence", help="the file update frequence", required=True)
parser.add_argument("-l","--loglevel",help="int for the logging level")
args = parser.parse_args()
frequence = args.frequence

if args.loglevel:
    logging.getLogger().setLevel(int(args.logging))





def get_all_info():
    """
    :return: all infos
    """
    allinfos = []
    allinfos.append(cpu.get_all_info_cpu())
    allinfos.append(disks.print_all_info_disks())
    allinfos.append(mem.print_all_info_memory())
    allinfos.append(net.print_all_info())
    allinfos.append(sens.print_all_info())

    return allinfos


def write_log_in_file(interval):
    """
    write all info in a file with interval
    :return:
    """

    while (True):
        print("oe")
        file = open("logs.log","w")

        logs = get_all_info()
        for log in logs:
            for line in log:
                file.write(str(line)+"\n")



        file.close()
        time.sleep(interval)

write_log_in_file(int(frequence))