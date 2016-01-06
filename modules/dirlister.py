import os

def run(**args):
    print "[*] In dirlister modle."
    files = os.listdir(".")
    print "files: %s" % files
    return "dirlister done"
 #   return str(files)
  