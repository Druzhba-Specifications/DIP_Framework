import os
class Console:
    def write(write):
        print(write)
    def clear():
        try:
            if os.name == 'nt':
                os.system('cls')
            else:
                os.system('clear')
        except Exception as e:
            raise print(e)
    