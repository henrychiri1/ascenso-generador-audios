import streamlit as st
import os

st.set_page_config(layout="centered", page_title="Plataforma FDMERC")

st.markdown("<h1 style='text-align: center;'>Preparación Ascenso 2026</h1>", unsafe_allow_html=True)

# Ruta segura a la carpeta de audios
ruta_audios = os.path.join(os.path.dirname(__file__), "audios")

# --- LÓGICA DE LISTADO ---
if os.path.exists(ruta_audios):
    # Solo listamos los MP3 que tú hayas subido previamente
    archivos = [f for f in os.listdir(ruta_audios) if f.endswith('.mp3')]
    
    if archivos:
        seleccion = st.selectbox("Selecciona un audio para escuchar:", sorted(archivos))
        if seleccion:
            ruta_final = os.path.join(ruta_audios, seleccion)
            st.audio(ruta_final, format="audio/mp3")
    else:
        st.warning("La carpeta 'audios' está vacía. Sube archivos .mp3.")
else:
    st.error("No se encontró la carpeta 'audios'. Asegúrate de que existe en el repositorio.")

# --- BOTÓN DE SUBIDA (PARA TI) ---
if st.checkbox("Mostrar panel de subida"):
    arch_subido = st.file_uploader("Subir nuevo audio", type=['mp3'])
    if arch_subido:
        with open(os.path.join(ruta_audios, arch_subido.name), "wb") as f:
            f.write(arch_subido.getbuffer())
        st.success(f"Archivo {arch_subido.name} guardado.")
        st.rerun()