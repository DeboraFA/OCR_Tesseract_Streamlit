import streamlit as st
import pytesseract
from PIL import Image



# Título da aplicação
st.title("Aplicação OCR com Tesseract e Streamlit")

# Upload de imagem
uploaded_file = st.file_uploader("Selecione uma imagem...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Abrir a imagem
    image = Image.open(uploaded_file)
    st.image(image, caption='Imagem Carregada', use_column_width=True)
    


    # Usar o pytesseract para fazer OCR na imagem
    text = pytesseract.image_to_string(image)
    
    # Mostrar o texto extraído
    st.write("Texto extraído:")
    st.write(text)
