import time
import datetime

def is_summer(day):
    print("It is day {} of the year".format(day))

    if 171 <= day <= 265:
        return True
    else:
        return False

def main():
    datetime = time.localtime()
    day = datetime.tm_yday

    if is_summer(day):
        print("You should wear white pants")
    else:
        print("You should wear black pants")

main()