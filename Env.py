import logging

def get_env_level():
    """
    :return: the level of logging in the .ven file
    """
    lines = read_file_line(".env")

    for line in lines:

        line = line.split("=")
        if line[0] == "LOG_LEVEL":
            return line[1]


def read_file_line(file):
    """
    :return all the line in a file
    """
    f = open(file,"r")
    lines = f.readlines()
    return lines


def return_env_level():
    """
    return the logging level on the .env
    :param level: env level
    :return: logging.levelOfWarning
    """

    level = get_env_level()
    print()
    if level == '"warning"':
        return logging.WARNING
    if level == '"notset"':
        return logging.NOTSET
    if level == '"debug"':
        return logging.DEBUG
    if level == '"info"':
        return logging.INFO
    if level == '"error"':
        return logging.ERROR
    if level == '"critical"':
        return logging.CRITICAL
