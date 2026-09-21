<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Para Ti... ❤️</title>
    <!-- Fuentes de Google -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@1,400;1,600&family=Dancing+Script:wght@700&display=swap" rel="stylesheet">
    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- Canvas Confetti para la lluvia de flores y destellos -->
    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>
    
    <style>
        body, html {
            margin: 0;
            padding: 0;
            width: 100%;
            height: 100%;
            overflow: hidden;
            background-color: #0d0d0d;
            font-family: 'Cormorant Garamond', serif;
            user-select: none;
            -webkit-user-select: none;
            touch-action: manipulation;
        }

        .titulo {
            font-family: 'Dancing Script', cursive;
            color: #d4a373;
            text-shadow: 0 0 15px rgba(212, 163, 115, 0.4);
        }

        .mensaje {
            font-family: 'Cormorant Garamond', serif;
            font-style: italic;
            color: #e5e5ea;
        }

        /* Tarjeta con efecto cristal oscuro */
        .tarjeta-cristal {
            background: rgba(18, 18, 18, 0.85);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border: 1px solid rgba(212, 163, 115, 0.3);
            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.8);
        }

        /* Botón elegante con brillo dorado */
        .boton-romantico {
            background: linear-gradient(135deg, rgba(212, 163, 115, 0.2), rgba(255, 215, 0, 0.15));
            border: 2px solid #d4a373;
            color: #ffd700;
            font-family: 'Cormorant Garamond', serif;
            font-style: italic;
            text-shadow: 0 0 10px rgba(255, 215, 0, 0.5);
            box-shadow: 0 0 20px rgba(212, 163, 115, 0.3);
            transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            animation: pulsoBrillo 2s infinite;
        }

        .boton-romantico:hover, .boton-romantico:active {
            transform: scale(1.08);
            background: #d4a373;
            color: #0d0d0d;
            box-shadow: 0 0 35px rgba(255, 215, 0, 0.8);
            text-shadow: none;
        }

        @keyframes pulsoBrillo {
            0%, 100% {
                box-shadow: 0 0 15px rgba(212, 163, 115, 0.3);
                transform: scale(1);
            }
            50% {
                box-shadow: 0 0 30px rgba(255, 215, 0, 0.6);
                transform: scale(1.04);
            }
        }

        /* Flor flotante animada que aparece en pantalla */
        .flor-lego-flotante {
            position: absolute;
            pointer-events: none;
            transform: translate(-50%, -50%) scale(0);
            animation: brotarFlor 0.7s cubic-bezier(0.175, 0.885, 0.32, 1.275) forwards;
            z-index: 10;
        }

        @keyframes brotarFlor {
            0% {
                transform: translate(-50%, -50%) scale(0) rotate(-20deg);
                opacity: 0;
            }
            70% {
                transform: translate(-50%, -50%) scale(1.2) rotate(10deg);
                opacity: 1;
            }
            100% {
                transform: translate(-50%, -50%) scale(1) rotate(0deg);
                opacity: 0.95;
            }
        }

        /* Destello y corazon ascendente */
        .corazon-flotante {
            position: absolute;
            color: #ffd700;
            font-size: 24px;
            pointer-events: none;
            animation: elevarCorazon 1.8s ease-out forwards;
            z-index: 20;
        }

        @keyframes elevarCorazon {
            0% { opacity: 1; transform: translate(-50%, 0) scale(0.6); }
            100% { opacity: 0; transform: translate(-50%, -100px) scale(1.4); }
        }

        /* Partículas de fondo */
        .particula-dorada {
            position: absolute;
            background: radial-gradient(circle, #ffd700 0%, rgba(212, 163, 115, 0) 70%);
            border-radius: 50%;
            pointer-events: none;
            animation: flotarParticula 5s ease-in-out infinite;
        }

        @keyframes flotarParticula {
            0%, 100% { transform: translateY(0) scale(0.8); opacity: 0.2; }
            50% { transform: translateY(-30px) scale(1.3); opacity: 0.7; }
        }
    </style>
</head>
<body class="flex flex-col justify-between items-center h-screen w-screen select-none overflow-hidden relative">

    <div id="contenedor-destellos" class="absolute inset-0 pointer-events-none overflow-hidden"></div>

    <!-- Encabezado y mensaje central -->
    <main class="w-full max-w-xl mx-auto pt-8 px-4 z-20 text-center flex flex-col items-center my-auto">
        <div class="tarjeta-cristal rounded-3xl p-6 sm:p-8 w-full transition-all duration-500">
            <h1 class="titulo text-5xl sm:text-6xl font-bold mb-3">Para Ti... ❤️</h1>
            
            <div class="flex items-center justify-center space-x-2 my-3">
                <span class="h-[1px] w-12 bg-[#d4a373] opacity-40"></span>
                <span class="text-[#ffd700] text-lg">✦ 🌻 ✦</span>
                <span class="h-[1px] w-12 bg-[#d4a373] opacity-40"></span>
            </div>

            <p class="mensaje text-xl sm:text-2xl leading-relaxed text-gray-200 mt-4 mb-6">
                Tal vez no pude comprarte tus flores... <br>
                pero preferí <span class="text-[#ffd700] font-semibold">hacértelas</span> con todo mi cariño. 🌻✨
            </p>

            <!-- Botón Principal -->
            <div class="my-4">
                <button id="boton-principal" class="boton-romantico px-8 py-4 rounded-full text-2xl font-bold cursor-pointer transition-all">
                    Presiona aquí ✨
                </button>
            </div>

            <!-- Contador de flores acumuladas -->
            <div id="contenedor-contador" class="mt-6 opacity-0 transition-opacity duration-500">
                <div class="inline-flex items-center gap-2 px-5 py-2 rounded-full bg-[#d4a373]/10 border border-[#d4a373]/40 text-[#d4a373] text-base font-semibold">
                    <span>🌻 Flores amarillas para ti:</span>
                    <span id="contador-flores" class="text-xl font-bold text-[#ffd700]">0</span>
                </div>
            </div>
        </div>
    </main>

    <!-- Indicador para seguir tocando la pantalla -->
    <div id="mensaje-continuar" class="fixed bottom-6 left-1/2 transform -translate-x-1/2 text-center pointer-events-none z-20 opacity-0 transition-opacity duration-500 w-full px-4">
        <div class="inline-block px-6 py-2.5 rounded-full tarjeta-cristal border border-[#ffd700]/40 text-[#ffd700] text-sm sm:text-base font-medium shadow-xl">
            ✨ Toca la pantalla para seguir apareciendo más flores amarillas 🌻
        </div>
    </div>

    <script>
        let totalFlores = 0;
        const botonPrincipal = document.getElementById('boton-principal');
        const contadorFlores = document.getElementById('contador-flores');
        const contenedorContador = document.getElementById('contenedor-contador');
        const mensajeContinuar = document.getElementById('mensaje-continuar');
        const contenedorDestellos = document.getElementById('contenedor-destellos');

        // Generar destellos dorados en el fondo
        for (let i = 0; i < 35; i++) {
            const particula = document.createElement('div');
            particula.className = 'particula-dorada';
            const tamano = Math.random() * 5 + 2;
            particula.style.width = `${tamano}px`;
            particula.style.height = `${tamano}px`;
            particula.style.left = `${Math.random() * 100}%`;
            particula.style.top = `${Math.random() * 100}%`;
            particula.style.animationDelay = `${Math.random() * 5}s`;
            particula.style.animationDuration = `${Math.random() * 3 + 3}s`;
            contenedorDestellos.appendChild(particula);
        }

        // Paletas de tonos de Flores Amarillas estilo Lego
        const paletasAmarillas = [
            { petalo: '#FFD700', centro: '#8B4513', tallo: '#4CAF50' }, // Girasol brillante
            { petalo: '#FFEB3B', centro: '#FF9800', tallo: '#388E3C' }, // Amarillo cálido
            { petalo: '#FFC107', centro: '#5D4037', tallo: '#2E7D32' }, // Ámbar Lego
            { petalo: '#FFEE58', centro: '#E65100', tallo: '#43A047' }, // Amarillo pastel
            { petalo: '#FBC02D', centro: '#3E2723', tallo: '#1B5E20' }  // Dorado clásico
        ];

        // Función para crear el vector SVG de la flor estilo LEGO
        function crearSVGFlorLego(paleta, escalaAltura) {
            const altoTallo = 100 * escalaAltura;
            return `
            <svg width="110" height="${altoTallo + 80}" viewBox="0 0 110 ${altoTallo + 80}" fill="none" xmlns="http://www.w3.org/2000/svg">
                <!-- Tallo estilo bloque Lego -->
                <g id="tallo">
                    <rect x="50" y="55" width="10" height="${altoTallo}" rx="2" fill="${paleta.tallo}" stroke="#1B5E20" stroke-width="1.5"/>
                    <rect x="48" y="${55 + altoTallo * 0.4}" width="14" height="4" rx="1" fill="#81C784"/>
                    <!-- Hojas Lego -->
                    <path d="M 50 ${55 + altoTallo * 0.5} L 28 ${55 + altoTallo * 0.38} L 32 ${55 + altoTallo * 0.58} Z" fill="#388E3C" stroke="#1B5E20" stroke-width="1"/>
                    <path d="M 60 ${55 + altoTallo * 0.35} L 82 ${55 + altoTallo * 0.23} L 78 ${55 + altoTallo * 0.42} Z" fill="#388E3C" stroke="#1B5E20" stroke-width="1"/>
                </g>

                <!-- Cabeza de Flor Lego Amarilla -->
                <g id="cabeza" transform="translate(55, 45)">
                    <!-- Pétalos en bloques angulares -->
                    <rect x="-11" y="-42" width="22" height="22" rx="4" fill="${paleta.petalo}" stroke="#F57F17" stroke-width="1.2"/>
                    <circle cx="0" cy="-31" r="4.5" fill="${paleta.petalo}" filter="brightness(1.15)"/>

                    <rect x="-11" y="20" width="22" height="22" rx="4" fill="${paleta.petalo}" stroke="#F57F17" stroke-width="1.2"/>
                    <circle cx="0" cy="31" r="4.5" fill="${paleta.petalo}" filter="brightness(1.15)"/>

                    <rect x="-42" y="-11" width="22" height="22" rx="4" fill="${paleta.petalo}" stroke="#F57F17" stroke-width="1.2"/>
                    <circle cx="-31" cy="0" r="4.5" fill="${paleta.petalo}" filter="brightness(1.15)"/>

                    <rect x="20" y="-11" width="22" height="22" rx="4" fill="${paleta.petalo}" stroke="#F57F17" stroke-width="1.2"/>
                    <circle cx="31" cy="0" r="4.5" fill="${paleta.petalo}" filter="brightness(1.15)"/>

                    <!-- Pétalos diagonales -->
                    <rect x="-30" y="-30" width="18" height="18" rx="3" fill="${paleta.petalo}" transform="rotate(45)" filter="brightness(0.95)"/>
                    <rect x="12" y="-30" width="18" height="18" rx="3" fill="${paleta.petalo}" transform="rotate(45)" filter="brightness(0.95)"/>
                    <rect x="-30" y="12" width="18" height="18" rx="3" fill="${paleta.petalo}" transform="rotate(45)" filter="brightness(0.95)"/>
                    <rect x="12" y="12" width="18" height="18" rx="3" fill="${paleta.petalo}" transform="rotate(45)" filter="brightness(0.95)"/>

                    <!-- Centro Botón/Conector Lego -->
                    <circle cx="0" cy="0" r="16" fill="${paleta.centro}" stroke="#3E2723" stroke-width="1"/>
                    <circle cx="0" cy="0" r="10" fill="${paleta.centro}" filter="brightness(1.2)"/>
                    <circle cx="0" cy="0" r="6" fill="none" stroke="rgba(255,255,255,0.3)" stroke-width="1.5"/>
                </g>
            </svg>
            `;
        }

        // Función para brotar una flor en una posición (x, y)
        function brotarFlor(x, y) {
            const florContenedor = document.createElement('div');
            florContenedor.className = 'flor-lego-flotante';
            florContenedor.style.left = `${x}px`;
            florContenedor.style.top = `${y}px`;

            const paleta = paletasAmarillas[Math.floor(Math.random() * paletasAmarillas.length)];
            const escalaLego = (Math.random() * 0.4 + 0.75).toFixed(2);
            const escalaAltura = (Math.random() * 0.4 + 0.8).toFixed(2);

            florContenedor.style.transform = `translate(-50%, -50%) scale(${escalaLego})`;
            florContenedor.innerHTML = crearSVGFlorLego(paleta, escalaAltura);

            document.body.appendChild(florContenedor);

            // Corazón flotante arriba de la flor
            const corazon = document.createElement('div');
            corazon.className = 'corazon-flotante';
            corazon.innerHTML = Math.random() > 0.4 ? '🌻' : '✨';
            corazon.style.left = `${x}px`;
            corazon.style.top = `${y - 30}px`;
            document.body.appendChild(corazon);
            setTimeout(() => corazon.remove(), 1800);

            totalFlores++;
            contadorFlores.textContent = totalFlores;
        }

        // Ráfaga masiva de flores y confeti amarillo
        function rafagaFloresAmarillas() {
            // Lluvia de confeti amarillo y dorado
            confetti({
                particleCount: 80,
                spread: 100,
                origin: { y: 0.6 },
                colors: ['#FFD700', '#FFEB3B', '#FFC107', '#ffffff', '#d4a373']
            });

            // Generar un racimo de muchas flores amarillas por la pantalla
            const ancho = window.innerWidth;
            const alto = window.innerHeight;

            for (let i = 0; i < 14; i++) {
                setTimeout(() => {
                    const posX = Math.random() * (ancho - 100) + 50;
                    const posY = Math.random() * (alto - 150) + 80;
                    brotarFlor(posX, posY);
                }, i * 90);
            }
        }

        // Evento del botón principal "Presiona aquí"
        botonPrincipal.addEventListener('click', (e) => {
            e.stopPropagation();
            
            // Mostrar contador e instrucciones para continuar
            contenedorContador.classList.remove('opacity-0');
            mensajeContinuar.classList.remove('opacity-0');

            rafagaFloresAmarillas();
        });

        // Permitir seguir tocando/haciendo clic en cualquier parte de la pantalla para seguir sacando más flores
        document.body.addEventListener('pointerdown', (e) => {
            // Evitar que vuelva a dispararse doble si se hace clic exactamente sobre el botón
            if (e.target.closest('#boton-principal')) return;

            brotarFlor(e.clientX, e.clientY);

            // Confeti sutil adicional por cada toque
            confetti({
                particleCount: 12,
                spread: 50,
                origin: { x: e.clientX / window.innerWidth, y: e.clientY / 
