import os

def run(**args):
    print "[*] In environment module."
    env = str(os.environ)
    print "env: %s" % env
    #return str(os.environ)
    return "environment done"
  
