from scapy.all import sniff
import psutil

stats = {"packets": 0, "upload_speed": 0, "download_speed": 0}

def packet_callback(packet):
    stats["packets"] += 1

def capture_packets():
    sniff(prn=packet_callback, store=0)

def get_latest_stats():
    net_io = psutil.net_io_counters()
    stats["upload_speed"] = net_io.bytes_sent / 1024 / 1024
    stats["download_speed"] = net_io.bytes_recv / 1024 / 1024
    return stats
