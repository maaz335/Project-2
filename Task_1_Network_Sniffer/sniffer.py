import sys

# Try to import streamlit. If it fails, we are in a pure CLI environment without it.
try:
    import streamlit as st
    # Check if we are running inside Streamlit web environment
    in_streamlit = st.runtime.exists()
except ImportError:
    in_streamlit = False

if in_streamlit:
    st.set_page_config(page_title="Network Sniffer", page_icon="🌐")
    st.title("🌐 Task 1: Network Sniffer")
    st.error("🚨 **Deployment Notice:** Real-time network packet sniffing cannot be performed on Streamlit Cloud due to lack of Administrator/Root network privileges on their servers.")
    
    st.info("💡 **How to run this properly:**\nOpen your local computer's terminal/command prompt as Administrator and run:\n\n`python sniffer.py`")
    
    st.subheader("Simulated Output Example")
    st.write("Since we cannot capture packets on the cloud, here is what the output looks like when you run it locally:")
    st.code("""
[TCP] Source: 192.168.1.5 -> Destination: 142.250.190.46
   Payload: b'GET / HTTP/1.1\\r\\nHost: www.google.com\\r\\n...'
--------------------------------------------------
[UDP] Source: 192.168.1.5 -> Destination: 8.8.8.8
   Payload: b'\\xab\\xcd\\x01\\x00\\x00\\x01\\x00\\x00\\x00\\x00\\x00\\x00\\x06google...'
--------------------------------------------------
[TCP] Source: 104.21.75.52 -> Destination: 192.168.1.5
   Payload: b'HTTP/1.1 200 OK\\r\\nDate: Mon, 15 Jun 2026...'
--------------------------------------------------
    """, language="text")

else:
    # We are running locally in a terminal! Run the actual sniffer.
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
        print("Starting Network Sniffer...")
        print("Press Ctrl+C to stop.")
        try:
            sniff(prn=packet_callback, store=False)
        except Exception as e:
            print(f"An error occurred: {e}")
            print("Make sure you are running with Administrative privileges.")
