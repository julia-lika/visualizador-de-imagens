# Visualizador de Imagens com Filtros

Este projeto é um visualizador de imagens com filtros em Python, utilizando `tkinter` e `Pillow`.

## Funcionalidades

- Carregamento de imagens
- Aplicação dos seguintes filtros:
    - Escala de cinza
    - Inversão de cores
    - Aumento de contraste
    - Desfoque
    - Nitidez
    - Detecção de bordas
- Visualização da imagem original e processada lado a lado
- Salvamento da imagem final

## Requisitos

- Python 3.x
- Pillow

## Como executar

### Passo 1: Instale as dependências

Certifique-se de que você tem o Python 3.x instalado no seu sistema. Para instalar as dependências, execute o seguinte comando no terminal:

```bash
pip install -r requirements.txt
```

### Passo 2: Execute o programa

No terminal, navegue até o diretório do projeto e execute o seguinte comando:

```bash
python main.py
```

### Observação para usuários Linux

Se você estiver utilizando Linux, pode ser necessário instalar o `tkinter` separadamente, caso ele não esteja incluído na sua instalação do Python. Para instalá-lo, use o gerenciador de pacotes da sua distribuição. Por exemplo:

- **Ubuntu/Debian**:
    ```bash
    sudo apt-get install python3-tk
    ```

- **Fedora**:
    ```bash
    sudo dnf install python3-tkinter
    ```

Após instalar o `tkinter`, repita os passos acima para executar o programa.