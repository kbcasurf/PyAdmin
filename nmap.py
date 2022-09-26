#importa a lib scapy
import scapy.all as scapy

# coloque aqui o endereco IP que deseja fazer o nmap
ip_nmap = "XXX.XXX.XXX.XXX"

# executa a funcao nmap para portas 1 a 1024
res, unans = sr(IP(dst=ip_nmap)/TCP(flags="S", dport=(1,1024)))

# mostra as portas abertas
res.nsummary(lfilter=lambda s,r: (r.haslayer(TCP) and
(r.getlayer(TCP).flags & 2)))
