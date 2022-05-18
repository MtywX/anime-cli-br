# Anime cli br

O anime cli é uma interface no terminal em que facilita o uso para assistir animes de código aberto. Esse projeto não é feito para ser um projeto grande, pois você pode ir lá e assistir no site.

**Source de vídeos: [AnimeFire](https://animefire.net)**<br>
**Author: TheLowRam**

## Showcase

https://user-images.githubusercontent.com/61241512/169169317-6207a76f-b071-4237-8ea9-f63f6d2e0eb3.mp4

## Tabela de Conteúdo

- [Anime cli br](#anime-cli-br)
  - [Showcase](#showcase)
  - [Tabela de Conteúdo](#tabela-de-conteúdo)
  - [Instalar](#instalar)
    - [Python](#python)
    - [VLC Player](#vlc-player)
    - [Windows e Linux](#windows-e-linux)
  - [Dependências](#dependências)

## Instalar

### Python

Para instalar o Anime cli br você precisa do python com a versão >= 3.9 e o módulo pip no path do terminal.

[Python 3.9](https://www.python.org/downloads/release/python-3912/)

Uma nota importante é que para rodar as cores igual a da showcase você precisa do suporte para ANSI code no cmd

### VLC Player

O "vlc" é um player necessário para rodar os vídeos, você pode encontra-lo nesse link abaixo

[Vlc](https://www.videolan.org/vlc/)

Caso você não queira ele é so modificar o script

### Windows e Linux

Para instalar é so seguir esses passos bem simples no terminal
```sh
git clone https://github.com/iiKylerX/anime-cli-br
cd anime-cli-br
pip install .
```

Ele ainda não foi testado no MacOS, então sinta-se livre para testar-lo.

## Dependências

- click
- bs4
- colorama