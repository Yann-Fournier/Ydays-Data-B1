# Pour le lancer : streamlit run demo.py
import streamlit as st

st.title("Hello streamlit")

st.header("Header")

st.subheader("Sub Header")

st.text("I like apple")

st.markdown(""" # h1 tag
## h2 tag
### h3 tag
:moon:<br>
:sunglasses:
**bold**
_italics_
""",True)

st.latex(r''' a + ar + a r^2 + a r^3 + \cdots + a r^{n-} = 
            \sum_{k=0}^{n-1} ar^k = 
            a \left(\frac{1-r^{n}}{1-r}\right)''')


d = {
    "name":"Harsh",
    "language":"Python",
    "topic":"Streamlit"
}
st.write(d)

