import argparse

def configCLI():
    """
    config the argpars
    :return: nothing
    """
    parser = argparse.ArgumentParser()

    parser.add_argument("-f", "--frequence", help="the file update frequence",required=True)
    args = parser.parse_args()
    print(args.frequence)



configCLI()