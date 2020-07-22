import sys
#works_only_when_your_girlfriends_wifi_is_turned_on_hA_ha
import subprocess 
import os
from decouple import config

IP_NETWORK = config('IP_NETWORK')
IP_DEVICE = config('IP_DEVICE')

proc = subprocess.Popen(["ping", IP_NETWORK],stdout=subprocess.PIPE)
while True:
  line = proc.stdout.readline()
  if not line:
    break
  #the real code does filtering here
  connected_ip = line.decode('utf-8').split()[3]

  if connected_ip == IP_DEVICE:
      subprocess.Popen(["say", "Linnea just connected to the network"])
