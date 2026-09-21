import streamlit as st
import streamlit.components.v1 as components

# 1. CONFIGURACIÓN DE PÁGINA (Sin HTML suelto para evitar el SyntaxError)
st.set_page_config(
    page_title="Para Ti... ❤️",
    page_icon="🌻",
    layout="centered"
)

# Initialize Session State para saber si ya se presionó el botón
if "flores_visibles" not in st.session_state:
    st.session_state.flores_visibles = False

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
        color: #f4d03f; /* Amarillo cálido */
        font-size: 25px;
        padding: 15px 20px;
        line-height: 1.6;
        border-radius: 15px;
        background: rgba(212, 163, 115, 0.05);
        border: 1px dashed rgba(212, 163, 115, 0.3);
        margin-top: 20px;
    }

    /* Botones minimalistas finos */
    .stButton>button {
        border-radius: 50px;
        border: 2px solid #ffd166 !important;
        background-color: transparent !important;
        color: #ffd166 !important;
        font-family: 'Cormorant Garamond', serif;
        font-style: italic;
        font-size: 22px !important;
        font-weight: 600;
        height: 3.2em;
        width: 100%;
        transition: 0.4s;
        cursor: pointer;
    }

    .stButton>button:hover {
        background-color: #ffd166 !important;
        color: #0d0d0d !important;
        box-shadow: 0px 4px 25px rgba(255, 209, 102, 0.5);
        transform: translateY(-2px);
    }
    </style>
""", unsafe_allow_html=True)

# 3. CONTENIDO PRINCIPAL
st.markdown("<h1 class='titulo'>Un detalle para ti...</h1>", unsafe_allow_html=True)

# Divisor estético sutil
st.markdown("<div style='text-align:center; color:#d4a373; opacity:0.4; margin-bottom:20px;'>✦ ─── 🌻 ─── ✦</div>", unsafe_allow_html=True)

# 4. BOTÓN INTERACTIVO PRINCIPAL
if not st.session_state.flores_visibles:
    st.markdown("<p style='text-align:center; color:#e5e5ea; font-family:\"Cormorant Garamond\", serif; font-size:20px; font-style:italic;'>Tengo algo que decirte...</p>", unsafe_allow_html=True)
    if st.button("✨ Presiona aquí ✨"):
        st.session_state.flores_visibles = True
        st.rerun()

# 5. MOSTRAR LAS FLORES Y LA ANIMACIÓN AL PRESIONAR EL BOTÓN
if st.session_state.flores_visibles:
    # Efecto de Globos/Fiesta nativo
    st.balloons()
    
    # Animación en Javascript de Lluvia de Flores Amarillas
    components.html("""
        <script>
            function crearFlor() {
                const flor = document.createElement('div');
                const tipos = ['🌻', '🌼', '💛', '✨', '🌸'];
                flor.innerText = tipos[Math.floor(Math.random() * tipos.length)];
                flor.style.position = 'fixed';
                flor.style.left = Math.random() * 100 + 'vw';
                flor.style.top = '-50px';
                flor.style.fontSize = (Math.random() * 25 + 20) + 'px';
                flor.style.zIndex = '99999';
                flor.style.pointerEvents = 'none';
                flor.style.transition = 'transform 4s linear, opacity 4s ease-out';
                document.body.appendChild(flor);

                setTimeout(() => {
                    flor.style.transform = `translateY(${window.innerHeight + 100}px) rotate(${Math.random() * 360}deg)`;
                    flor.style.opacity = '0';
                }, 100);

                setTimeout(() => { flor.remove(); }, 4000);
            }
            setInterval(crearFlor, 150);
        </script>
    """, height=0)

    # Imagen de Flores Amarillas tipo Lego
    st.image(
        "https://images.unsplash.com/photo-1643122818988-cb941e73993f?q=80&w=1200&auto=format&fit=crop",
        use_container_width=True,
        caption="Tus flores amarillas para siempre 🌻"
    )

    # El mensaje especial
    st.markdown("""
        <div class='mensaje'>
            No puedo comprarte tus flores... <br>
            pero puedo hacértelas, pieza por pieza, con mucho cariño. 🌻✨
        </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Botón para volver a ver la animación de flores
    if st.button("🌻 ¡Quiero más flores amarillas! ✨"):
        st.balloons()
