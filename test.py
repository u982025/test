from dec import my_decorator
import time
@my_decorator
def test_case1():
    for item in range(9):
        time.sleep(1)
        print("in test_case1----- hooray")

@my_decorator
def test_case2():
    for item in range(9):
        time.sleep(1)
        print("in test_case2----- hooray")

@my_decorator
def test_case3():
    for item in range(9):
        time.sleep(1)
        print("in test_case3----- hooray")

