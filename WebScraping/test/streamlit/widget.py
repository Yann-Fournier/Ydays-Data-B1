# Pour le lancer : streamlit run widget.py
import streamlit as st

st.title("WIDGETS")

if st.button("Subscribe"):
    st.write("Like the video")


name = st.text_input("Name")
st.write(name)

address = st.text_area("Enter your address")
st.write(address)

date = st.date_input("enter the date")
#st.write(date)

time = st.time_input("enter the time")
#st.write(time)

if st.checkbox("you accept the T&C", value=False):
    st.write("Thank you")


v1 = st.radio("Colours", ["r", "g", "b"], index=0)
v2 = st.selectbox("Colours", ["r", "g", "b"], index=0)
#st.write(v1, v2)

v3 = st.multiselect("Colours", ["r", "g", "b"])
#st.write(v3)

st.slider("age", min_value=18, max_value=60, value=30, step=2)

st.number_input("numbers",min_value=18.0, max_value=60.0, value=30.0, step=2.0)

img = st.file_uploader("Upload a file")
st.image(img)

