import datetime
from mydep import test as mydep_test
mydep_test()
print (datetime.datetime.now())
def wait_for_print():
    from time import sleep
    sleep(3)
    print('Hello world')
wait_for_print()
