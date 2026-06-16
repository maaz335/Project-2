import sys
import time
import random

# Try to import streamlit. If it fails, we are in a pure CLI environment without it.
try:
    import streamlit as st
    # Check if we are running inside Streamlit web environment
    in_streamlit = st.runtime.exists()
except ImportError:
    in_streamlit = False

if in_streamlit:
    st.set_page_config(page_title="Network Sniffer", page_icon="🌐", layout="wide")
    st.title("🌐 Task 1: Network Sniffer (Cloud Simulator)")
    
    st.warning("🚨 **Technical Notice:** Real hardware packet sniffing requires `root`/`Administrator` access, which is not allowed on cloud servers (unprivileged containers). Therefore, this is a **Live Simulation** to demonstrate how the sniffer works!")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("🎛️ Controls")
        packet_count = st.slider("How many packets to capture?", min_value=5, max_value=50, value=15)
        start_sniffing = st.button("Start Sniffing 🚀", type="primary")
        
    with col2:
        st.subheader("📡 Live Packet Terminal")
        terminal_placeholder = st.empty()
        
        if not start_sniffing:
            terminal_placeholder.code("Waiting for packets... \nPress 'Start Sniffing' to intercept network traffic.", language="text")
    
    if start_sniffing:
        protocols = ["TCP", "UDP", "ICMP", "HTTP", "HTTPS", "DNS"]
        base_ips = ["192.168.1.", "10.0.0.", "172.16.0.", "142.250.190.", "104.21.75.", "8.8.8."]
        
        captured_data = "Starting Live Capture...\n" + "="*50 + "\n\n"
        st_text = terminal_placeholder.code(captured_data, language="text")
        
        for i in range(packet_count):
            proto = random.choice(protocols)
            src = random.choice(base_ips) + str(random.randint(1, 254))
            dst = random.choice(base_ips) + str(random.randint(1, 254))
            
            payload = ""
            if proto == "HTTP":
                payload = "b'GET /login HTTP/1.1\\r\\nHost: target.com\\r\\n'"
            elif proto == "DNS":
                payload = "b'\\x08\\x00\\x00\\x01\\x00\\x00\\x00\\x00\\x00\\x00\\x06google\\x03com...'"
            elif proto == "HTTPS":
                payload = "b'\\x16\\x03\\x01\\x02\\x00\\x01\\x00\\x01... (Encrypted)'"
            elif proto == "ICMP":
                payload = "b'PING request data...'"
            else:
                payload = f"b'\\x{random.randint(10,99)}\\x{random.randint(10,99)}... raw payload ...'"
            
            packet_str = f"[{proto}] {src}  --->  {dst}\n    Payload: {payload}\n" + "-"*60 + "\n"
            captured_data += packet_str
            
            # Update the terminal in real-time
            terminal_placeholder.code(captured_data, language="text")
            time.sleep(random.uniform(0.2, 0.8)) # Simulate natural delay between packets
            
        st.success(f"✅ Successfully captured {packet_count} packets!")

else:
    # We are running locally in a terminal! Run the ACTUAL hardware sniffer.
    from scapy.all import sniff, IP, TCP, UDP
    
    def packet_callback(packet):
        if IP in packet:
            src_ip = packet[IP].src
            dst_ip = packet[IP].dst
            
            if TCP in packet:
                proto_name = "TCP"
                try: payload = bytes(packet[TCP].payload)
                except: payload = b""
            elif UDP in packet:
                proto_name = "UDP"
                try: payload = bytes(packet[UDP].payload)
                except: payload = b""
            else:
                proto_name = "Other"
                try: payload = bytes(packet[IP].payload)
                except: payload = b""
            
            print(f"[{proto_name}] Source: {src_ip} -> Destination: {dst_ip}")
            if payload:
                print(f"   Payload: {payload[:50]}")
                print("-" * 50)

    if __name__ == "__main__":
        print("Starting Hardware Network Sniffer...")
        print("Press Ctrl+C to stop.")
        try:
            sniff(prn=packet_callback, store=False)
        except Exception as e:
            print(f"An error occurred: {e}")
            print("Make sure you are running with Administrative privileges.")
