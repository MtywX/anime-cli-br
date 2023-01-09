# Nota

Coisas para adicionar no anime-cli-br:

- Histórico
- Download
- Fetch Update
- Checar Versão
- Botão de voltar a pesquisar enquanto o vídeo estiver tocando

# Anime cli br

O anime cli é uma interface no terminal em que facilita o uso para assistir animes de código aberto. Esse script não é feito para ser um projeto grande.

**Source de vídeos: [AnimeFire](https://animefire.net)**<br>
**Versão: 1.2.0**<br>
**Author: TheLowRam**

## Showcase

https://user-images.githubusercontent.com/61241512/169169317-6207a76f-b071-4237-8ea9-f63f6d2e0eb3.mp4

## Tabela de Conteúdo

- [Anime cli br](#anime-cli-br)
  - [Showcase](#showcase)
  - [Tabela de Conteúdo](#tabela-de-conteúdo)
  - [Como Instalar](#como-instalar)
    - [Python](#python)
    - [VLC](#vlc)
    - [Windows & Linux](#windows--linux)
  - [Dependências](#dependências)

## Como Instalar

### Python

Instalando o python, é preciso da versão >= 3.9 e o PIP no path do terminal.

Baixe ele nesse link abaixo:

[Python (3.9.12)](https://www.python.org/downloads/release/python-3912/)

### VLC

O "vlc" é um player usado para rodar os vídeos, pode baixar nesse link abaixo:

[VLC Media Player](https://www.videolan.org/vlc/)

*Caso você não queira ele é só modificar o script*

### Windows & Linux

Depois de ter instalado os outros agora basta seguir esses simples passos
```sh
git clone https://github.com/MtywX/anime-cli-br
cd anime-cli-br
pip install .
```

Ainda não foi testado no MacOS e no Android, então sinta-se livre para testá-lo.

**Uma nota é que para ter as cores no cmd igual a da showcase é necessário o suporte de ANSI Colors no cmd**

## Dependências

- click
- bs4
- colorama
