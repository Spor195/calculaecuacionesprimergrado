import streamlit as st
import random

st.title("Ecuaciones de Primer Grado")

# Generar coeficientes aleatorios
if "a" not in st.session_state:
    st.session_state.a = random.randint(1, 10)
    st.session_state.b = random.randint(-10, 10)
    st.session_state.c = random.randint(-10, 10)

a = st.session_state.a
b = st.session_state.b
c = st.session_state.c

# Mostrar la ecuación
st.write(f"Resuelve para x: **{a}x + {b} = {c}**")

# Campo de entrada para el usuario
respuesta = st.number_input("Tu respuesta para x:", step=0.1, format="%.2f")

# Botón de verificación
if st.button("Verificar"):
    solucion = (c - b) / a
    if abs(respuesta - solucion) < 0.01:
        st.success("✅ ¡Correcto! La solución es x = {:.2f}".format(solucion))
    else:
        st.error("❌ Incorrecto. Intenta otra vez.")

# Botón para nueva ecuación
if st.button("Nueva ecuación"):
    st.session_state.a = random.randint(1, 10)
    st.session_state.b = random.randint(-10, 10)
    st.session_state.c = random.randint(-10, 10)
    st.rerun()
