def my_decorator(wrapped):
    def inner(*args, **kwargs):
        print('in inner')
        return wrapped(*args, **kwargs)
    return inner

if __name__ == '__main__':
    import sys
    import importlib
    script_name = sys.argv[1].split('.')[0]
    print('----script: %s ' %(script_name))
    try:
        p = importlib.import_module(script_name)
        func = getattr(p,sys.argv[2])
        func()
    except NameError as e:
        print('NameError: %s' %(e))
     
