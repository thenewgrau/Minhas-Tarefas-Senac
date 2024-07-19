import streamlit as st

st.write('Gasolina')
nome = st.text_input("NOME")

st.write(f'Bem vindo {nome}')

distancia = st.number_input('Distância ')
consumido = st.number_input('Consumiu ')

gasto = consumido / distancia

if gasto < 6:
    st.write(f'Média = {gasto}')
    st.write('Ruim !')

elif gasto >= 6 and gasto <= 12:
    st.write(f"Média = {gasto}")
    st.write('Médio !')

else:
    st.write(f"Média = {gasto}")
    st.write('Bom !')
    