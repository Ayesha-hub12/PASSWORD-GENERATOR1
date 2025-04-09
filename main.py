import streamlit as st
import re

# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")
    
    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")
    
    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")
    
    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")
    
    # Strength Rating
    if score == 4:
        feedback.append("✅ Strong Password!")
    elif score == 3:
        feedback.append("⚠️ Moderate Password - Consider adding more security features.")
    else:
        feedback.append("❌ Weak Password - Improve it using the suggestions above.")
    
    return feedback

# Function to generate a strong password
def generate_strong_password():
    import random
    import string

    password_length = random.randint(12, 16)  # A good strong password length
    all_characters = string.ascii_letters + string.digits + "!@#$%^&*"
    password = ''.join(random.choice(all_characters) for _ in range(password_length))
    return password

# Streamlit UI
st.title("Password Strength Meter")
st.subheader("Check your password strength and improve its security!")

password_input = st.text_input("Enter your password:")

# Check password strength when the user enters a password
if password_input:
    result = check_password_strength(password_input)
    for line in result:
        st.write(line)

# Password Generator Feature
if st.button("Generate a Strong Password"):
    strong_password = generate_strong_password()
    st.write(f"Your generated strong password: **{strong_password}**")

# Add additional info about common weak passwords
st.sidebar.title("Additional Info")
st.sidebar.write("Common weak passwords like 'password123', '123456', or 'qwerty' should be avoided.")
st.sidebar.write("Use a mix of uppercase, lowercase, digits, and special characters.")
