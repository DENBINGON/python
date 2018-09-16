################################################
######### https://github.com/DENBINGON #########
############  Created by DENBINGON  ############
############ https://denbingon.com/ ############
############## crossplatform time ##############
################################################
def time():
    from datetime import datetime
    import os
    import sys
    time = 1
    while time == 1:
        print(datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S"))
        for num in range(5000000, 0, -1):
            stopping = 1
        if sys.platform == 'win32' or 'cygwin':
            os.system("clear")
        else:
            os.system("cls")
check = input("Show time ?\n")
if check == "":
    print("stop")
else:
    time()
