from dec import my_decorator

@my_decorator
def test_case5():
    import time
    print 'sleeping 4 seconds'
    time.sleep(4)
    print "in test_case5----- hooray"

@my_decorator
def test_case6():
    print "in test_case6----- hooray"

@my_decorator
def test_case7():
    print "in test_case7----- hooray"

