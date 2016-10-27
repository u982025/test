#!/usr/bin/python

import sys, getopt

def main(argv):
   config_file = ''
   job_filefile = ''
   try:
      opts, args = getopt.getopt(argv,"hc:j:",["cfg=","job="])
   except getopt.GetoptError:
      print 'test.py -c <config_file> -j <job_filefile>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'test.py -i <config_file> -o <job_filefile>'
         sys.exit()
      elif opt in ("-c", "--cfg"):
         config_file = arg
      elif opt in ("-j", "--job"):
         job_filefile = arg

       
   print 'Config file is "', config_file
   print 'Job file is "', job_filefile

if __name__ == "__main__":
   main(sys.argv[1:])

