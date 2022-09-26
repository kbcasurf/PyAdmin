# importa a lib scapy
import scapy.all as scapy

# coloque aqui o endereco IP que deseja fazer o trace
ip_traceroute = "XXX.XXX.XXX.XXX"

# executa a funcao traceroute
scapy.traceroute(ip_traceroute)
