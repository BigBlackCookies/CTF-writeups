#!/usr/bin/env python3
import pyshark

FILE = "ping-pong.pcapng"

def extract_flag(filename):
    cap = pyshark.FileCapture(filename, display_filter="tcp")

    ports = []

    for pkt in cap:
        try:
            dport = int(pkt.tcp.dstport)
            if 10000 <= dport <= 10125:
                ports.append(dport)
        except:
            continue

    cap.close()

    # Deduplicate: keep every odd index (requests or responses)
    cleaned = ports[::2]

    # Convert ports → ASCII
    flag = "".join(chr(p - 10000) for p in cleaned)

    return flag


if __name__ == "__main__":
    flag = extract_flag(FILE)
    print("Decoded flag:")
    print(flag)
