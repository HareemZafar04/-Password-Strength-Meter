import streamlit as st
import re
from zxcvbn import zxcvbn

# Set the page configuration
st.set_page_config(page_title="🔐 Password Strength Meter", layout="centered")

# Define the function to evaluate password strength
def evaluate_password_strength(password):
    # Use the zxcvbn library to evaluate the password strength
    strength = zxcvbn(password)
    score = strength['score']  # Score between 0 and 4
    feedback = strength['feedback']['suggestions']

    return score, feedback

# Define the password strength meter function
def password_strength_meter(password):
    score, feedback = evaluate_password_strength(password)

    # Display password strength feedback
    if score == 0:
        strength_level = "Very Weak"
        color = "red"
    elif score == 1:
        strength_level = "Weak"
        color = "orange"
    elif score == 2:
        strength_level = "Fair"
        color = "yellow"
    elif score == 3:
        strength_level = "Strong"
        color = "lightgreen"
    else:
        strength_level = "Very Strong"
        color = "green"

    # Display the strength level with feedback
    st.markdown(f"<h2 style='color:{color};'>{strength_level}</h2>", unsafe_allow_html=True)
    for suggestion in feedback:
        st.markdown(f"- {suggestion}")

# Main app logic
def main():
    st.title("🔐 Password Strength Meter")

    password = st.text_input("Enter your password:", type="password")

    if password:
        password_strength_meter(password)
    else:
        st.write("Please enter a password to check its strength.")

# Run the app
if __name__ == "__main__":
    main()
