import streamlit as st

# 1. CONFIGURACIÓN DE PÁGINA (Estilo más íntimo)
st.set_page_config(page_title="Para Ti... ❤️", page_icon="✨")

# 2. ESTILO CSS PERSONALIZADO (Minimalista Oscuro y Romántico)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Cormorant+Garamond:ital,wght@1,400;1,600&display=swap');

    /* Fondo oscuro elegante */
    .stApp {
        background-color: #0d0d0d;
    }

    .titulo {
        font-family: 'Dancing Script', cursive;
        color: #d4a373; /* Un dorado champagne elegante */
        text-align: center;
        font-size: 65px;
        margin-top: 40px;
        margin-bottom: 10px;
    }

    .mensaje {
        font-family: 'Cormorant Garamond', serif;
        font-style: italic;
        text-align: center;
        color: #e5e5ea;
        font-size: 26px;
        padding: 10px 20px;
        line-height: 1.6;
    }

    /* Modificación de los botones para que se vean súper finos */
    .stButton>button {
        border-radius: 50px;
        border: 1px solid #d4a373 !important;
        background-color: transparent !important;
        color: #d4a373 !important;
        font-family: 'Cormorant Garamond', serif;
        font-style: italic;
        font-size: 20px !important;
        font-weight: 600;
        height: 3em;
        width: 100%;
        transition: 0.4s;
        cursor: pointer;
    }

    .stButton>button:hover {
        background-color: #d4a373 !important;
        color: #0d0d0d !important;
        box-shadow: 0px 4px 20px rgba(212, 163, 115, 0.4);
        transform: translateY(-2px);
    }
    </style>
""", unsafe_allow_html=True)

# 3. CONTENIDO PRINCIPAL
st.markdown("<h1 class='titulo'>Para Siempre...</h1>", unsafe_allow_html=True)

# Divisor estético sutil
st.markdown("<div style='text-align:center; color:#d4a373; opacity:0.4; margin-bottom:40px;'>✦ ─── ✦ ─── ✦</div>", unsafe_allow_html=True)

# Tu frase matadora, limpia y directa en el centro de la pantalla
st.markdown(
    "<p class='mensaje'>Quédate conmigo... <br><br>y hagamos de cada pequeño momento, una eternidad completa. ❤️</p>",
    unsafe_allow_html=True)

# Espaciado estético inferior antes de la pregunta
st.markdown("<br><br>", unsafe_allow_html=True)

# 4. BOTONES DE RESPUESTA
col1, col2 = st.columns(2)

with col1:
    if st.button("✨ Sí, me quedo"):
        st.balloons()
        st.success("Hagamos historia... 🌹")
        
        # Tu número de teléfono configurado
        mi_numero = "50232347376"
        link_wa = f"https://wa.me/{mi_numero}?text=Acepto...%20hagamos%20de%20cada%20momento%20una%20eternidad%20❤️"
        
        st.markdown(f"""
            <a href="{link_wa}" target="_blank" style="text-decoration:none;">
                <div style="background-color:transparent; color:#d4a373; border: 1px dashed #d4a373; padding:12px; border-radius:30px; text-align:center; font-family:'Cormorant Garamond', serif; font-style:italic; font-size:18px; font-weight:bold; margin-top:15px;">
                    Confirmar al WhatsApp 📱
                </div>
            </a>
        """, unsafe_allow_html=True)

with col2:
    if st.button("🔒 Ya es un hecho"):
        st.balloons()
        st.info("No esperaba menos de nosotros. ✨")
        
        mi_numero = "50232347376"
        link_wa = f"https://wa.me/{mi_numero}?text=Ya%20es%20un%20hecho,%20para%20siempre%20✨"
        
        st.markdown(f"""
            <a href="{link_wa}" target="_blank" style="text-decoration:none;">
                <div style="background-color:transparent; color:#d4a373; border: 1px dashed #d4a373; padding:12px; border-radius:30px; text-align:center; font-family:'Cormorant Garamond', serif; font-style:italic; font-size:18px; font-weight:bold; margin-top:15px;">
                    Decírmelo ahora mismo 📱
                </div>
            </a>
        """, unsafe_allow_html=True)
