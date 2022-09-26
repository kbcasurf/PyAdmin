# importa a lib scapy
import scapy.all as scapy
# importa a lib requests
import requests
# coloque aqui o endereco IP que deseja pingar
ip_ping = "XXX.XXX.XXX.XXX"
# executa a funcao sr1 e colocando a resposta na variavel resposta
resposta = scapy.sr1(scapy.IP(dst=ip_ping)/scapy.ICMP(), timeout=3)
# verifica se existe resposta
if resposta is not None:
print('resposta')
print(resposta.src)
print(resposta.dst)
else:
print('nao teve resposta')
# coloque aqui o token do seu bot do telegram
TOKEN = "XXXXXXXXXXX"
# coloque aqui o id do chat do seu bot do telegram
chat_id = "XXXXXXXXXX"
# mensagem a ser enviada para o telegram
message = "nao teve resposta"
# url da api de envio de mensagem do telegram
url =
f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&te
xt={message}"
# acessa a url e envia a mensagem
requests.get(url)
