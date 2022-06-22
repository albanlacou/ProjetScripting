import psutil

def print_virtual_memory():
    """
    print virtual memory
    :return: virtual memory
    """
    return ["virtual memory",psutil.virtual_memory()]

def print_swap_memory():
    """
        print swap memory
        :return: swap memory
        """
    return ["swap memory",psutil.swap_memory()]

def print_all_info_memory():
    """
    :return: all info memory
    """
    allinfo = []

    allinfo.append(print_virtual_memory())
    allinfo.append(print_swap_memory())

    return allinfo

