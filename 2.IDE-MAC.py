# Скрипт смены МАС-адреса

import subprocess  # Не нашел библиотеку чтобы установить
import argparse

parser = argparse.ArgumentParser()  # Обязательный элемент при использовании библиотеки argparse

parser.add_argument("-i", "--interface", dest="intpars", help="Interface 2 change mac address")
parser.add_argument("-m", "--mac", dest="macpars", help="New MAC address")

opt = parser.parse_args()
interface = opt.intpars
newmac = opt.macpars

print("[+] Changing MAC address for " + interface + " to " + newmac)
print("-> shooting down " + interface)

subprocess.call("ifconfig " + interface + " down", shell=True)
print("-> changing mac to " + newmac)
subprocess.call("ifconfig %s hw ether %s" % (interface, newmac), shell=True)
print("-> powering up " + interface)
subprocess.call("ifconfig %s up" % (interface), shell=True)
print("result: ")
subprocess.call("ifconfig " + interface, shell=True)
