import streamlit as st

# 1. CONFIGURACIÓN DE PÁGINA 
st.set_page_config(page_title="Flores Para Ti... ❤️", page_icon="🌻")

# 2. ESTILO CSS PERSONALIZADO (Minimalista Oscuro, Elegante y Romántico)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Cormorant+Garamond:ital,wght@1,400;1,600&display=swap');

    /* Fondo oscuro elegante */
    .stApp {
        background-color: #0d0d0d;
    }

    .titulo {
        font-family: 'Dancing Script', cursive;
        color: #d4a373; /* Dorado champagne */
        text-align: center;
        font-size: 55px;
        margin-top: 10px;
        margin-bottom: 5px;
    }

    .mensaje {
        font-family: 'Cormorant Garamond', serif;
        font-style: italic;
        text-align: center;
        color: #e5e5ea;
        font-size: 24px;
        padding: 10px 20px;
        line-height: 1.6;
    }

    /* Botones minimalistas finos */
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
st.markdown("<h1 class='titulo'>Flores que no se marchitan...</h1>", unsafe_allow_html=True)

# Divisor estético sutil
st.markdown("<div style='text-align:center; color:#d4a373; opacity:0.4; margin-bottom:20px;'>✦ ─── 🌻 ─── ✦</div>", unsafe_allow_html=True)

# IMAGEN DE FLORES DE LEGO
# Fotografía con tono estético y elegante de flores Lego
st.image("https://images.unsplash.com/photo-1643122818988-cb941e73993f?q=80&w=1200&auto=format&fit=crop",
         use_container_width=True)

# Frase de regalo con el toque especial
st.markdown(
    "<p class='mensaje'>No podía comprarte flores normales que se marchiten en unos días... <br>así que preferí construirtelas, pieza por pieza, para que te duren para siempre. 🌻✨</p>",
    unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# 4. BOTONES DE RESPUESTA
col1, col2 = st.columns(2)

mi_numero = "50232347376"

with col1:
    if st.button("🌻 Me encantaron"):
        st.balloons()
        st.success("Tus flores eternas ya tienen dueña... 🌹")
        
        link_wa = f"https://wa.me/{mi_numero}?text=Me%20encantaron%20mis%20flores%20de%20Lego...%20gracias%20por%20construirlas%20para%20m%C3%AD%20❤️"
        
        st.markdown(f"""
            <a href="{link_wa}" target="_blank" style="text-decoration:none;">
                <div style="background-color:transparent; color:#d4a373; border: 1px dashed #d4a373; padding:12px; border-radius:30px; text-align:center; font-family:'Cormorant Garamond', serif; font-style:italic; font-size:18px; font-weight:bold; margin-top:15px;">
                    Decírmelo por WhatsApp 📱
                </div>
            </a>
        """, unsafe_allow_html=True)

with col2:
    if st.button("✨ Las guardaré para siempre"):
        st.balloons()
        st.info("Un detalle eterno para alguien inolvidable. ✨")
        
        link_wa = f"https://wa.me/{mi_numero}?text=Prometo%20guardar%20mis%20flores%20para%20siempre%20✨"
        
        st.markdown(f"""
            <a href="{link_wa}" target="_blank" style="text-decoration:none;">
                <div style="background-color:transparent; color:#d4a373; border: 1px dashed #d4a373; padding:12px; border-radius:30px; text-align:center; font-family:'Cormorant Garamond', serif; font-style:italic; font-size:18px; font-weight:bold; margin-top:15px;">
                    Confirmar entrega 📱
                </div>
            </a>
        """, unsafe_allow_html=True)
