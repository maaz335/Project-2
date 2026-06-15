from scapy.all import sniff, IP, TCP, UDP

def packet_callback(packet):
    """
    This function processes each packet captured by the sniffer.
    """
    # Check if the packet has an IP layer
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        
        # Determine the protocol
        if TCP in packet:
            proto_name = "TCP"
            try:
                payload = bytes(packet[TCP].payload)
            except:
                payload = b""
        elif UDP in packet:
            proto_name = "UDP"
            try:
                payload = bytes(packet[UDP].payload)
            except:
                payload = b""
        else:
            proto_name = "Other"
            try:
                payload = bytes(packet[IP].payload)
            except:
                payload = b""
        
        print(f"[{proto_name}] Source: {src_ip} -> Destination: {dst_ip}")
        
        # Print a short preview of the payload if it exists
        if payload:
            # Print only the first 50 bytes for readability
            print(f"   Payload: {payload[:50]}")
            print("-" * 50)

if __name__ == "__main__":
    print("Starting Network Sniffer...")
    print("Press Ctrl+C to stop.")
    print("Note: If you get permission errors, run this script as Administrator (Windows) or with sudo (Linux/Mac).")
    
    # Start sniffing
    # store=False ensures we don't keep all packets in memory
    try:
        sniff(prn=packet_callback, store=False)
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Make sure you are running with Administrative privileges and have Npcap (Windows) or libpcap (Linux) installed.")
