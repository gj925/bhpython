import os

def run(**args):
    print "[*] In dirlister modle."
    files = os.listdir(".")
    return str(files)
  