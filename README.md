# Aplicação OCR (Optical Character Recognition) com Tesseract e Streamlit

Este repositório contém uma aplicação simples de Reconhecimento Óptico de Caracteres (OCR) desenvolvida em Python utilizando as bibliotecas Streamlit e Tesseract. Com esta aplicação, você pode fazer upload de uma imagem contendo texto e extrair automaticamente o texto dela utilizando o Tesseract OCR.

## Funcionalidades
Upload de Imagem: Permite ao usuário fazer upload de imagens nos formatos JPG, PNG e JPEG.


OCR: Utiliza o Tesseract OCR para extrair texto da imagem carregada.


Exibição do Texto: Mostra o texto extraído da imagem diretamente na interface.

## Como Usar
Instalação: Clone este repositório e instale as dependências listadas no arquivo requirements.txt.

git clone https://github.com/seu-usuario/nome-do-repositorio.git

cd nome-do-repositorio

pip install -r requirements.txt

**Observação**: Baixe e instale o Tesseract, para Windows utilize esse [link](https://github.com/UB-Mannheim/tesseract/wiki). Execute o instalador e siga as instruções de instalação padrão. Certifique-se de lembrar o caminho de instalação (geralmente C:\Program Files\Tesseract-OCR). Adicione o caminho de instalação do Tesseract ao path das variáveis de ambiente do sistema.





Execução: Execute o script OCR_example.py utilizando o Streamlit.

streamlit run OCR_example.py


Utilização: Abra o navegador e acesse o link fornecido pelo Streamlit para interagir com a aplicação. 

## Tecnologias Utilizadas

- Python

- Streamlit

- Tesseract OCR

- PIL (Python Imaging Library) 


# Exemplo

![Exemplo de aplicação OCR para placa de automóveis](imagem_aplicacao.png)
