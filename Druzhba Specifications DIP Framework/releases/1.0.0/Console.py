import os

@staticmethod
def write(write):
    print(write)

@staticmethod
def clear():
    try:
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
    except Exception as e:
        raise print(e)
    