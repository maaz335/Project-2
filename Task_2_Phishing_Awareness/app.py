import streamlit as st

st.set_page_config(page_title="Phishing Awareness Training", page_icon="🎣", layout="centered")

st.title("🎣 Phishing Awareness Training")
st.markdown("Welcome to the Phishing Awareness Training Module. Learn how to protect yourself from social engineering attacks!")

# Navigation Tabs
tabs = st.tabs(["📚 What is Phishing?", "🔍 Real vs Fake", "🧠 Quiz Time!"])

# --- TAB 1: What is Phishing? ---
with tabs[0]:
    st.header("What is Phishing?")
    st.write("Phishing is a cyber attack that uses disguised email as a weapon. The goal is to trick the email recipient into believing that the message is something they want or need — a request from their bank, for instance, or a note from someone in their company — and to click a link or download an attachment.")
    
    st.subheader("Social Engineering Tactics")
    st.markdown("""
    - **Urgency:** Creating a false sense of urgency (e.g., "Your account will be suspended in 24 hours").
    - **Authority:** Pretending to be an executive, IT department, or a government agency.
    - **Curiosity:** Offering something too good to be true, like a free prize.
    """)

    st.subheader("Best Practices to Avoid Phishing")
    st.info("""
    1. **Check the Sender:** Always double-check the sender's email address. Is it `support@paypal.com` or `support@paypa1.security-update.com`?
    2. **Hover Before You Click:** Hover over links to see the actual URL before clicking.
    3. **Don't Download Unexpected Attachments:** Especially `.exe`, `.zip`, or macro-enabled Office files.
    4. **Enable 2FA:** Two-Factor Authentication adds an extra layer of security.
    """)

# --- TAB 2: Real vs Fake ---
with tabs[1]:
    st.header("Spot the Difference")
    st.write("Review the examples below to see how attackers try to trick you.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.error("🚨 Fake Email (Phishing)")
        st.markdown("""
        **From:** security@paypaI-update.com  
        **Subject:** URGENT: Your account has been compromised!
        
        Dear Customer,  
        We have detected suspicious activity. Please click the link below immediately to verify your identity or your account will be permanently locked.
        
        [Verify Now (http://bit.ly/random-link-123)]
        """)
        st.caption("Notice the urgent tone, the generic 'Dear Customer' greeting, the fake domain (paypaI with a capital i instead of l), and the obscured link.")

    with col2:
        st.success("✅ Real Email")
        st.markdown("""
        **From:** service@paypal.com  
        **Subject:** Notice of changes to our Privacy Statement
        
        Hello John Doe,  
        We are writing to let you know about upcoming changes to our Privacy Statement. 
        You can review the changes on our official website by logging into your account.
        
        Sincerely,  
        PayPal
        """)
        st.caption("Notice the personal greeting, lack of aggressive urgency, legitimate email address, and absence of suspicious login links.")

# --- TAB 3: Quiz Time! ---
with tabs[2]:
    st.header("Knowledge Check")
    
    q1 = st.radio(
        "1. You receive an email from your 'Bank' asking you to reply with your password to verify your account. What should you do?",
        ("Reply immediately so my account isn't locked.", "Delete the email and contact the bank via their official phone number.", "Forward it to my friends."),
        index=None
    )
    if st.button("Check Answer 1"):
        if q1 == "Delete the email and contact the bank via their official phone number.":
            st.success("Correct! A legitimate bank will NEVER ask for your password via email.")
        elif q1 is None:
            st.warning("Please select an option.")
        else:
            st.error("Incorrect. Never share your password via email.")

    st.divider()

    q2 = st.radio(
        "2. Which of these URLs is most likely a phishing link trying to steal your Google credentials?",
        ("https://accounts.google.com/login", "https://myaccount.google.com/", "http://google-security-login.com/auth"),
        index=None
    )
    if st.button("Check Answer 2"):
        if q2 == "http://google-security-login.com/auth":
            st.success("Correct! Look out for non-standard domains and lack of HTTPS.")
        elif q2 is None:
            st.warning("Please select an option.")
        else:
            st.error("Incorrect. The first two are legitimate Google domains.")
