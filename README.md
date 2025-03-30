# yt2mp3 Downloader

## Introdução

Este projeto é uma aplicação web desenvolvida com Streamlit para permitir o download de áudio de vídeos do YouTube no formato MP3. O processo de download é gerenciado utilizando a biblioteca `yt_dlp`, e o progresso do download é exibido dinamicamente na interface.

## Tecnologias Utilizadas

- **Python** (Linguagem de programação principal)
- **Streamlit** (Framework para desenvolvimento de aplicações web)
- **yt\_dlp** (Biblioteca para download de vídeos e áudio do YouTube)
- **FFmpeg** (Utilitário para conversão e manipulação de mídia)

## Instalação

Antes de executar o projeto, certifique-se de instalar as dependências necessárias:

```bash
pip install streamlit yt-dlp
```

### Configuração do FFmpeg

É necessário ter o `FFmpeg` instalado para converter os arquivos de áudio corretamente. Siga os passos abaixo:

1. Faça o download do `FFmpeg` [aqui](https://ffmpeg.org/download.html).
2. Extraia os arquivos e mova a pasta para a raiz do projeto.
3. No código, configure a variável de localização do `FFmpeg` para apontar para a raiz do projeto:
   ```python
   'ffmpeg_location': 'ffmpeg/ffmpeg.exe'
   ```

## Como Executar

Para iniciar a aplicação, utilize o comando:

```bash
streamlit run nome_do_arquivo.py
```

Substitua `nome_do_arquivo.py` pelo nome correto do script Python.

## Estrutura do Código

O script está dividido nas seguintes seções:

### 1. **Importação de Bibliotecas**

O código importa as bibliotecas necessárias para o funcionamento da aplicação:

```python
import streamlit as st
import yt_dlp
import os
import re
import tempfile
```

### 2. **Função ****`baixar_mp3`**

Esta função é responsável por realizar o download do áudio do vídeo fornecido.

#### Parâmetros:

- `url` (str): URL do vídeo do YouTube.
- `progress_callback` (função): Função utilizada para atualizar o progresso do download.

#### Fluxo de execução:

1. Exibe uma mensagem informando que o arquivo está sendo preparado.
2. Define um diretório temporário para armazenar o arquivo MP3.
3. Cria um hook para atualizar a barra de progresso dinamicamente.
4. Configura os parâmetros do `yt_dlp`, incluindo:
   - Formato de melhor qualidade para áudio.
   - Conversão para MP3 utilizando `FFmpeg`.
   - Definição do caminho de saída.
   - Adição do hook de progresso.
5. Tenta baixar o vídeo e converter para MP3.
6. Retorna o caminho do arquivo MP3 baixado ou exibe um erro em caso de falha.

### 3. **Interface com Streamlit**

O Streamlit é usado para criar uma interface interativa:

- **Título da página**:

  ```python
  st.title("🎵 MP3 Downloader com Progresso")
  ```

- **Entrada para URL do vídeo**:

  ```python
  url_direta = st.text_input("📌 Insira um link do YouTube:")
  ```

- **Barra de progresso**:

  ```python
  progress = st.progress(0)
  ```

- **Função para atualizar a barra de progresso**:

  ```python
  def atualizar_progresso(valor):
      progress.progress(int(valor))
  ```

- **Botão de download**:

  ```python
  if url_direta:
      if st.button("Baixar pelo Link"):
          arquivo_mp3 = baixar_mp3(url_direta, atualizar_progresso)
          if arquivo_mp3:
              st.success("Finalizado!  Clique no botão abaixo para fazer o download do arquivo.")
              with open(arquivo_mp3, "rb") as file:
                  st.download_button(label="📥 Baixar MP3", data=file, file_name=os.path.basename(arquivo_mp3),
                                     mime="audio/mpeg")
  ```

## Possíveis Erros e Soluções

1. **FFmpeg não encontrado**:

   - Certifique-se de que o `FFmpeg` foi baixado e colocado na raiz do projeto.
   - Verifique se o caminho do `FFmpeg` está correto no código:
     ```python
     'ffmpeg_location': 'ffmpeg/ffmpeg.exe'
     ```

2. **Erro ao baixar o vídeo**:

   - O vídeo pode estar indisponível, bloqueado ou a URL pode estar incorreta.
   - Verifique se o link inserido é válido e funcional.

3. **O arquivo não aparece para download**:

   - Pode ter ocorrido uma falha na conversão do arquivo. Verifique as mensagens de erro exibidas no Streamlit.

## Conclusão

Este projeto fornece uma interface intuitiva para baixar áudio do YouTube no formato MP3 com visualização de progresso em tempo real. Ele pode ser expandido para oferecer suporte a outros formatos de download ou recursos adicionais.

Caso deseje modificar ou melhorar o projeto, basta editar o script conforme necessário.

---

**Autor:** Danilo Tavares

