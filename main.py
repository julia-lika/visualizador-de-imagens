import streamlit as st
from PIL import Image, ImageEnhance, ImageOps, ImageFilter
import io

# Funções auxiliares
def apply_enhancements(image, rotate, brightness, contrast, sharpness):
    image = image.rotate(rotate)
    image = ImageEnhance.Brightness(image).enhance(brightness)
    image = ImageEnhance.Contrast(image).enhance(contrast)
    image = ImageEnhance.Sharpness(image).enhance(sharpness)
    return image

def apply_filters(image, grayscale, invert, blur, edge_detect):
    if grayscale:
        image = ImageOps.grayscale(image)
    if invert:
        image = ImageOps.invert(image.convert("RGB"))
    if blur:
        image = image.filter(ImageFilter.BLUR)
    if edge_detect:
        image = image.filter(ImageFilter.FIND_EDGES)
    return image

def apply_transformations(image, flip_option, resize, new_width, new_height, crop, crop_box):
    if flip_option == "Horizontal":
        image = ImageOps.mirror(image)
    elif flip_option == "Vertical":
        image = ImageOps.flip(image)

    if resize:
        image = image.resize((new_width, new_height))

    if crop:
        image = image.crop(crop_box)

    return image

def main():
    st.set_page_config(page_title="Editor de Arquivos", layout="wide")
    st.title(":fire: Editor de Arquivos :fire:")

    with st.sidebar:
        st.header("📁 Upload")
        uploaded_file = st.file_uploader("Escolha uma imagem", type=["jpg", "jpeg", "png"])

    if uploaded_file:
        original_image = Image.open(uploaded_file)

        # Sidebar - Configurações
        with st.sidebar.expander("Ajustes Básicos"):
            rotate = st.slider("Rotação", 0, 360, 0, step=10)
            brightness = st.slider("Brilho", 1.0, 3.0, 1.0, step=0.1)
            contrast = st.slider("Contraste", 1.0, 3.0, 1.0, step=0.1)
            sharpness = st.slider("Nitidez", 1.0, 3.0, 1.0, step=0.1)

        with st.sidebar.expander("Filtros"):
            grayscale = st.checkbox("Escala de Cinza")
            invert = st.checkbox("Inversão de Cores")
            blur = st.checkbox("Desfoque")
            edge_detect = st.checkbox("Detecção de Bordas")

        with st.sidebar.expander("Transformações"):
            flip_option = st.selectbox("Inverter Imagem", ["Nenhum", "Horizontal", "Vertical"])
            resize = st.checkbox("Redimensionar")
            new_width = st.number_input("Nova Largura", 1, original_image.width * 5, original_image.width) if resize else original_image.width
            new_height = st.number_input("Nova Altura", 1, original_image.height * 5, original_image.height) if resize else original_image.height

            crop = st.checkbox("Cortar Imagem")
            left = st.number_input("Esquerda", 0, original_image.width, 0) if crop else 0
            top = st.number_input("Cima", 0, original_image.height, 0) if crop else 0
            right = st.number_input("Direita", 0, original_image.width, original_image.width) if crop else original_image.width
            bottom = st.number_input("Esquerda", 0, original_image.height, original_image.height) if crop else original_image.height
            crop_box = (left, top, right, bottom)

        # Processamento da imagem
        edited_image = apply_enhancements(original_image.copy(), rotate, brightness, contrast, sharpness)
        edited_image = apply_filters(edited_image, grayscale, invert, blur, edge_detect)
        edited_image = apply_transformations(edited_image, flip_option, resize, new_width, new_height, crop, crop_box)

        # Layout das imagens
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Original")
            st.image(original_image, use_container_width=True)
        with col2:
            st.subheader("Editada")
            st.image(edited_image, use_container_width=True)

        # Botão de download
        st.sidebar.markdown("---")
        buffered = io.BytesIO()
        edited_image.save(buffered, format="JPEG")
        st.sidebar.download_button(
            label="💾 Download",
            data=buffered.getvalue(),
            file_name="imagem_editada.jpg",
            mime="image/jpeg"
        )

if __name__ == "__main__":
    main()
