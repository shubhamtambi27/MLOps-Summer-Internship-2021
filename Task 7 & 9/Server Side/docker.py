#!/usr/bin/python3




print("content-type: text/html")
print()


import cgi 
import subprocess
import os
f= cgi.FieldStorage()
cmd = f.getvalue("docker_cmd")

print(subprocess.getoutput("sudo "+cmd))



