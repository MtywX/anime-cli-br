"""
    Anime cli br
    Um script com o objetivo de assistir anime no cmd

    Eu não vou criar uma documentação do script porque não tenho motivos para isso :>

    Source de vídeo: AnimeFire
    Author: TheLowRam
"""

# Libraries

import os
import click
import json
import requests
import subprocess
from bs4 import BeautifulSoup
from colorama import Fore

# Vars

base_url="https://animefire.net"
player="vlc" # Change if you want the main player

# Clear function, it switchs between the os

def clear():
    if os.name == "nt": # Windows
        os.system("cls")
    else: # Others
        os.system("clear")

def search_anime(anime, page = 1):
    clear()

    html = requests.get(
        url=base_url + '/pesquisar/' + anime + f"/{page}",
        data=None,
        headers={'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36'}
    )

    if html.status_code >= 300:
        print(Fore.RED + "Não foi possível fazer o request, Status Code : " + str(html.status_code) + Fore.RESET)
        exit()

    soup = BeautifulSoup(html.text, 'html.parser')

    anime_container = soup.find('div', {"class" : "row ml-1 mr-1"})

    anime_view = ''
    anime_json = {}
    count = 0

    for i in anime_container.findAll('a', href=True):
        count += 1
        anime_json[count] = i['href']

    count = 0

    for i in anime_container.findAll('h3', {"class": "animeTitle"}):
        count += 1
        anime_view += f"[{str(count)}] " + i.text + '\n'

    if anime_json == {}:
        print(Fore.RED + "O anime que você procurou não existe ou está sem episódios." + Fore.RESET)
        exit()

    print(
        anime_view,
        Fore.GREEN + "\nPágina Atual: " + Fore.WHITE + str(page),
        Fore.YELLOW + "\n\nAções: p [Próxima Página], a [Página Anterior], números [Anime]" + Fore.RESET
    )

    option = input(Fore.CYAN + "\nSelecione o anime: " + Fore.RESET).lower()

    if option == 'p':
        return search_anime(anime, page + 1)
    elif option == 'a':
        if page > 1:
            return search_anime(anime, page - 1)
        else:
            exit()
    elif option.isnumeric():
        option = int(option)
        return anime_json[option]
    else:
        print(Fore.RED + "\nOpção inválida" + Fore.RESET)
        exit()

def gather_episodes(anime):
    clear()

    html = requests.get(
        url=anime,
        data=None,
        headers={'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36'}
    )
    
    if html.status_code >= 300:
        print(Fore.RED + "Não foi possível fazer o request, Status Code : " + str(html.status_code) + Fore.RESET)
        exit()

    soup = BeautifulSoup(html.text, 'html.parser')

    episodes_container = soup.find('div', {"class" : "div_video_list"})

    global episodes_json

    episodes_view = ''
    episodes_json = {}
    count = 0

    for i in episodes_container.findAll('a', href=True):
        count += 1
        episodes_view += f"[{str(count)}] " + i.text + '\n'
        episodes_json[count] = i['href']

    print(
        episodes_view,
        Fore.YELLOW + "\nAções: números [Episódios]" + Fore.RESET
    )

    option = input(Fore.CYAN + "\nSua opção: " + Fore.RESET)

    if option.isnumeric():
        global current_episode
        global last_episode

        current_episode = int(option)
        last_episode = list(episodes_json)[-1]

        if current_episode in episodes_json:
            return episodes_json[current_episode]
        else:
            print(Fore.RED + "\nEpisódio não existe" + Fore.RESET)
            exit()
    else:
        print(Fore.RED + "\nOpção inválida" + Fore.RESET)
        exit()

def play_video(episode_result):
    clear()

    html = requests.get(
        url=episode_result,
        data=None,
        headers={'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36'}
    )
    
    if html.status_code >= 300:
        print(Fore.RED + "Não foi possível fazer o request, Status Code : " + str(html.status_code) + Fore.RESET)
        exit()

    soup = BeautifulSoup(html.text, 'html.parser')

    main_div_video = soup.find('div', {"id" : "main_div_video"})

    light_player_backend = main_div_video.find('video', {"id" : "my-video"})
    external_player = main_div_video.find('iframe')
    light_player = ''

    if light_player_backend == None:
        confirm = input(Fore.CYAN + "Esse player infelizmente não é streamable, pois é um player do youtube encryptado. Deseja continuar no navegador? (Sim/s): " + Fore.RESET).lower()

        if confirm == "sim" or confirm == "s":
            if os.name == 'nt':
                os.system(f"start {external_player['src']}")
            else:
                os.system(f"xdg-open {external_player['src']}")
        else:
            print(Fore.RED + "\nVocê escolheu não dar play no vídeo" + Fore.RESET)
    else:
        light_html = requests.get(
            url=light_player_backend['data-video-src'],
            data=None,
            headers={'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36'}
        )
    
        if light_html.status_code >= 300:
            print(Fore.RED + "Não foi possível fazer o request, Status Code : " + str(light_html.status_code) + Fore.RESET)
            exit()

        content = json.loads(light_html.text)
        video_quality_view = ''
        light_json = {}
        
        for i in range(0, len(content['data'])):
            video_quality_view += f"{content['data'][i]['label']} "
            light_json[content['data'][i]['label']] = content['data'][i]['src']

        print(Fore.YELLOW + video_quality_view)

        option = input(Fore.CYAN + "\nEscolha a qualidade: " + Fore.RESET)

        if option in light_json:
            light_player = subprocess.Popen(f"{player} {light_json[option]}", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        else:
            print(Fore.RED + "\nOpção invalida" + Fore.RESET)
            exit()

    clear()

    global current_episode
    global episodes_json

    print(
        Fore.GREEN + "Episódio Atual: " + Fore.WHITE + str(current_episode),
        Fore.YELLOW + "\n\nAções: p [Próximo Episódio], a [Episódio anterior], s [Selecionar Episódio], r [Replay], q [Sair]" + Fore.RESET
    )

    option = input(Fore.CYAN + "\nSua opção: " + Fore.RESET)
    
    if light_player_backend != None:
        light_player.terminate()

    if option == 'p':
        if current_episode == last_episode:
            exit()

        current_episode += 1
        return play_video(episodes_json[current_episode])
    elif option == 'a':
        if current_episode == 1:
            exit()

        current_episode -= 1
        return play_video(episodes_json[current_episode])
    elif option == 's':
        return play_video(gather_episodes(anime_result))
    elif option == 'r':
        return play_video(episodes_json[current_episode])
    elif option == 'q':
        exit()
    else:
        print(Fore.RED + "\nOpção invalida" + Fore.RESET)
        exit()

@click.command()
def main():

    clear()

    anime = input(Fore.CYAN + "Procurar pelo o anime: " + Fore.RESET)
    keyword = anime.lower().replace(' ', '-')

    global anime_result

    anime_result = search_anime(keyword)

    episode_result = gather_episodes(anime_result)

    play_video(episode_result)

if __name__ == "__main__":
    main()