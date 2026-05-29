import socket
import struct


s=socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP) 

def parse_packet(data):
    entete_ip=data[0:20]

    ipver=entete_ip[0]>>4

    packet_length=entete_ip[2:4]

    print("Version IP: ", ipver)

    print("Longueur du paquet: ", packet_length)

    protocol=entete_ip[9]

    src_ip=entete_ip[12:16]

    dst_ip=entete_ip[16:20]
    
    src=socket.inet_ntoa(src_ip)
    dst=socket.inet_ntoa(dst_ip)

    print("Adresse IP source: ", src) 
    print("Adresse IP destination: ", dst)

    entete_tcp=data[20:40]

    src_port = struct.unpack('!H', entete_tcp[0:2])[0]
    dst_port = struct.unpack('!H', entete_tcp[2:4])[0]

    flags=entete_tcp[13]

    print("Port source: ", src_port)
    print("Port destination: ", dst_port)
    print("Flags TCP: ", flags)
    
    donnees=data[40:]
    print("Données: ", donnees)

while True:
    raw, addr = s.recvfrom(65535)
    parse_packet(raw)



    