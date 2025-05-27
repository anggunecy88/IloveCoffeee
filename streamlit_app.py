import streamlit as st

st.title("☕️ I Love Coffe")
st.write(
   "Brewed from darkness, coffee teaches us how to turn bitter into"
)
st.image("Unknown 21.jpeg", width=200)
st.image("Paul mescal and Daisy edgar jones.jpeg", width=200)


st.title("How i'm with her is my normal personality.")
st.header("I love Normal People & Coffe)  
angka = st.number_input("Tulis sebuah Angka:", value=0, step=1)

if (angka % 2) == 0:
  st.write(f"{angka} adalah Bilangan Genap")
else:
  st.write(f"{angka} adalah Bilangan Ganjil")
