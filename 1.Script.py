# #Мой код
# import scapy-python3 as scapy # Требуется установить библиотеку Scapy и Libpcap (Линукс) для винды надо Wincap, то что
# # есть не подходи, нет нужных атрибутов
#
#
# def scan(ip):
#     # scapy.arping(ip) #arping - выполняет запросы и получет ответы, по сути полноценный скрипт. &Не понятно как работает
# # работает на МАС, на винде нет
#     arp_req = scapy.ARP(pdst=ip)
#     # arp_req.pdst = ip #строчка не нужна, т.к. в предыдущей прописали "pdst = ip"
#     scapy.ls(scapy.ARP()) #scapy.ls -  выводит то, что мы попросим
#     # print(arp_req.summery())
#     broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
#     # scapy.ls(scapy.Ether())
#     arp_sum = broadcast/arp_req
#     # print(arp_sum.summary())
#     # arp_req.show()
#     # broadcast.show()
#     # arp_sum.show()
#     ans, unans = scapy.srp(apr_sum, timeout=1, verbose=False) # spr - отправляет данные; timeout - ограничивает ожидание
# # до 1 сек, иначе будет долго ждать и постоянно запрашивать
#     # print(ans.summary())
#     print("IP\t\t\t\tMAC")
#     print("---------------------------------------------")
#     for a in ans:
#         # print(a[1].show()) #Получаем много данных: наш запрос и ответ на наш запрос.
#         print(a[1].psrc + "\t\t\t" + a[1].hwsrc)
#
# scan("192.168.0.1/24")



#Код от Skillfactory

arp_req=scapy.ARP()
scapy.ls(scapy.ARP())

import scapy.all as scapydef scan(ip):# scapy.arping(ip)arp_req=scapy.ARP(pdst=ip)broadcast =
# scapy.Ether()scapy.ls(scapy.Ether())scan("192.168.2.1/24")

arp_sum = broadcast/arp_req
import scapy.all as scapydef scan(ip):# scapy.arping(ip)arp_req=scapy.ARP(pdst=ip)broadcast =
# scapy.Ether(dst="ff:ff:ff:ff:ff:ff")arp_sum = broadcast/arp_reqans, unans= scapy.srp(arp_sum, timeout=1,
# verbose=False)print("IP\t\t\t\tMAC")print("-------------------------------------------")for a in ans:print(a[1].psrc
# + "\t\t\t" + a[1].hwsrc)scan("192.168.2.1/24")

import scapy.all as scapydef scan(ip):# scapy.arping(ip)arp_req=scapy.ARP(pdst=ip)broadcast =
# scapy.Ether(dst="ff:ff:ff:ff:ff:ff")arp_sum = broadcast/arp_reqans, unans= scapy.srp(arp_sum, timeout=1,
# verbose=False)print("IP\t\t\t\tMAC")print("-------------------------------------------")for a in ans:print(a[1].psrc
# + "\t\t\t" + a[1].hwsrc)scan("192.168.2.1/24")
