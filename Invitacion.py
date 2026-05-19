import streamlit as st

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(page_title="Invitación Especial 🎬", page_icon="🍿")

# 2. ESTILO CSS PERSONALIZADO
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Quicksand:wght@300;500&display=swap');

    .main {
        background-color: #fff5f5; /* Un tono rosado muy sutil */
    }

    .titulo {
        font-family: 'Dancing Script', cursive;
        color: #d32f2f;
        text-align: center;
        font-size: 55px;
        margin-top: 20px;
    }

    .mensaje {
        font-family: 'Quicksand', sans-serif;
        text-align: center;
        color: #444;
        font-size: 22px;
        padding: 20px;
        line-height: 1.5;
    }

    .stButton>button {
        border-radius: 50px;
        border: none;
        background-color: #ff4b4b;
        color: white;
        font-family: 'Quicksand', sans-serif;
        font-weight: 700;
        height: 3.5em;
        transition: 0.3s;
        box-shadow: 0px 4px 15px rgba(255, 75, 75, 0.3);
    }

    .stButton>button:hover {
        background-color: #d32f2f;
        transform: translateY(-3px);
    }
    </style>
""", unsafe_allow_html=True)

# 3. CONTENIDO
st.markdown("<h1 class='titulo'>¡Hola! ✨</h1>", unsafe_allow_html=True)

# Imagen de respaldo (esta es de un servidor muy estable de iconos/fotos)
st.image("https://cdn.pixabay.com/photo/2017/11/24/10/43/ticket-2974645_1280.jpg",
         caption="¿Qué vas ha hacer el sabado?",
         use_container_width=True)

st.markdown(
    "<p class='mensaje'>¿Vemos una pelicula, como amigos?. <br><br><b>¿Qué dices? 🍿🎬</b></p>",
    unsafe_allow_html=True)

# 4. BOTONES DE RESPUESTA
col1, col2 = st.columns(2)

with col1:
    if st.button("💖 ¡SÍ, ME ENCANTARÍA!"):
        st.balloons()
        st.success("¡Wuju!")
        # REEMPLAZA EL NÚMERO ABAJO (sin el + solo el código de país y número)
        mi_numero = "50232347376"
        link_wa = f"https://wa.me/{mi_numero}?text=¡Acepto%20la%20invitación%20🍿🎬"
        st.markdown(f"""
            <a href="{link_wa}" target="_blank" style="text-decoration:none;">
                <div style="background-color:#25d366; color:white; padding:10px; border-radius:10px; text-align:center; font-weight:bold;">
                    Confirmar por WhatsApp 📱
                </div>
            </a>
        """, unsafe_allow_html=True)

with col2:
    if st.button("😊 DÉJAME PENSARLO"):
        st.info("¿Segura? va ser bonito. ✨")
