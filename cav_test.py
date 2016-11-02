import runner
import sys
from subprocess import Popen, PIPE, TimeoutExpired

if __name__ == '__main__':
    if sys.argv[1]:
        script_name = sys.argv[1]
    if sys.argv[2]:
        test_cases = sys.argv[2].split()
    print (test_cases)
    for test_case in test_cases:
        cmd = ('python2.7', 'runner.py', script_name, test_case)
        try:
            child = Popen(cmd, stdout=sys.stdout, stderr=sys.stderr)
        except OSError as e:
            print('OSError: %s' %(e))
        except ValueError as e:
            print('ValueError: %s' %(e))

        #Check if timeout expired, and kill the process
        try:
            retVal = child.communicate(timeout=5)
        except TimeoutExpired as e:
            child.kill()
            print('TimeoutExpired: %s' %(e))
