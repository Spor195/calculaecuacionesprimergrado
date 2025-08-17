import streamlit as st
import random

st.set_page_config(page_title="Ecuaciones de Primer Grado", layout="wide")
st.title("Ecuaciones de Primer Grado")

# ----- Menú lateral -----
st.sidebar.header("Opciones de configuración")
rango_x = st.sidebar.slider("Rango de valores para x", -20, 20, (-5, 5))
rango_a = st.sidebar.slider("Rango para coeficiente a", 1, 15, (1, 5))
rango_b = st.sidebar.slider("Rango para término b", -20, 20, (-5, 5))
nueva = st.sidebar.button("Generar nueva ecuación")

# ----- Estado inicial -----
if "qid" not in st.session_state:
    st.session_state.qid = 0  # identificador de pregunta
if "pregunta" not in st.session_state:
    nueva = True  # fuerza la primera pregunta

# ----- Crear NUEVA pregunta y congelar opciones -----
if nueva:
    x_sol = random.randint(rango_x[0], rango_x[1])
    a = random.randint(rango_a[0], rango_a[1])
    b = random.randint(rango_b[0], rango_b[1])
    c = a * x_sol + b
    st.session_state.pregunta = (a, b, c, x_sol)

    # Generar 3 distractores enteros únicos, cercanos a la solución
    distractores = set()
    candidatos = [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]
    random.shuffle(candidatos)
    for d in candidatos:
        if len(distractores) == 3: break
        cand = x_sol + d
        if cand != x_sol:
            distractores.add(cand)

    opciones = [x_sol] + list(distractores)
    random.shuffle(opciones)  # se barajan una sola vez
    st.session_state.opciones = opciones

    # Clave única por pregunta para aislar el radio
    st.session_state.qid += 1
    st.session_state[f"respuesta_{st.session_state.qid}"] = None

# ----- Mostrar en pantalla -----
a, b, c, solucion = st.session_state.pregunta
opciones = st.session_state.opciones
qid = st.session_state.qid

st.subheader(f"Resuelve para x: **{a}x + {b} = {c}**")

respuesta = st.radio(
    "Elige la respuesta correcta:",
    opciones,
    key=f"respuesta_{qid}"   # clave única por pregunta
)

if st.button("Verificar"):
    if respuesta == solucion:
        st.success(f"✅ Correcto: x = {solucion}")
    else:
        st.error(f"❌ Incorrecto. La respuesta correcta era x = {solucion}")
