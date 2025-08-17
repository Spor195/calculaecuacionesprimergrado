import streamlit as st
import random

st.title("Ecuaciones de Primer Grado")

# Menú lateral
st.sidebar.header("Opciones de configuración")
rango_x = st.sidebar.slider("Rango de valores para x", -10, 10, (-5, 5))
rango_a = st.sidebar.slider("Rango para coeficiente a", 1, 10, (1, 5))
rango_b = st.sidebar.slider("Rango para término b", -10, 10, (-5, 5))
nueva_ecuacion = st.sidebar.button("Generar nueva ecuación")

# Inicialización de estado
if "pregunta" not in st.session_state or nueva_ecuacion:
    # Elegir solución entera
    x_sol = random.randint(rango_x[0], rango_x[1])
    a = random.randint(rango_a[0], rango_a[1])
    b = random.randint(rango_b[0], rango_b[1])
    c = a * x_sol + b

    # Guardar en el estado
    st.session_state.pregunta = (a, b, c, x_sol)

a, b, c, solucion = st.session_state.pregunta

# Mostrar la ecuación
st.subheader(f"Resuelve para x: **{a}x + {b} = {c}**")

# Generar opciones (1 correcta + 3 distractores)
opciones = [solucion]
while len(opciones) < 4:
    distractor = solucion + random.choice([-3, -2, -1, 1, 2, 3])
    if distractor not in opciones:
        opciones.append(distractor)
random.shuffle(opciones)

# Pregunta de opción múltiple
respuesta = st.radio("Elige la respuesta correcta:", opciones)

# Botón de verificación
if st.button("Verificar"):
    if respuesta == solucion:
        st.success(f"✅ Correcto: x = {solucion}")
    else:
        st.error(f"❌ Incorrecto. La respuesta correcta era x = {solucion}")
