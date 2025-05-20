# Visualizador de Arquivos - Ponderada de Programação

Esse projeto é um editor de imagens simples e funcional feito com Python, usando o Streamlit para a interface e a biblioteca Pillow (PIL) para manipulação das imagens.

## Funcionalidades

Você pode:

- Girar a imagem (de 0° a 360°)
- Ajustar o brilho
- Alterar o contraste
- Deixar a imagem mais nítida
- Converter para tons de cinza
- Espelhar a imagem na horizontal ou vertical
- Recortar a imagem manualmente
- Baixar a imagem final com um clique

## Como usar

1. Instale as dependências (se ainda não tiver):
    ```bash
    pip install streamlit pillow
    ```

2. Execute o app:

    ```bash
    streamlit run main.py
    ```

3. Acesse no navegador o link que o Streamlit gerar (geralmente `http://localhost:8501`).

4. Faça upload de uma imagem `.jpg`, `.jpeg` ou `.png`, ajuste os controles na barra lateral e veja as alterações em tempo real.

5. Quando terminar, é só clicar no botão de download para salvar a imagem editada.


## Sobre o código

O projeto foi feito com o objetivo de estudar manipulação de imagens e criação de interfaces rápidas com Streamlit. Cada funcionalidade foi implementada usando recursos nativos da PIL.

## Exemplos de Uso
Com este código, é possível manipular imagens de diversas maneiras:

![Diagrama de Sequência do Algoritmo de IA](/img/teste.png)