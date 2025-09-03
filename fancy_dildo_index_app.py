
import streamlit as st

st.set_page_config(page_title="Dildo Index Calculator", page_icon="🍆", layout="centered")

st.title("🍆 Welcome to the Dildo Index! 🍆")
st.markdown(
    '''
Enter a value in South African Rands, and see how many dildos it's worth!
The more Rands, the longer the bar 😎
'''
)

randvalue = st.number_input(
    "Enter your value in Rands (SA):", min_value=0.0, step=1.0, format="%.2f"
)

average_d = 450
d_index = randvalue / average_d if randvalue > 0 else 0

if randvalue > 0:
    st.success(f"Your item is worth approximately **{d_index:.2f} dildos**!")
    max_display = 20
    bar_value = min(d_index, max_display)
    st.progress(bar_value / max_display)
    num_emojis = int(min(d_index, 50))
    st.markdown(" ".join(["🍆"] * num_emojis))

st.info("Disclaimer: This is purely for entertainment purposes. 😉")
