#!/usr/bin/python3

import cgi 
import subprocess


print("content-type: text/html")
print("Access-Control-Allow-Origin:*")
print()

f= cgi.FieldStorage()
cmd = f.getvalue("kube_cmd")

print(subprocess.getoutput(cmd+" --kubeconfig admin.conf"))
#print(subprocess.getoutput("kubectl get pods --kubeconfig admin.conf"))
