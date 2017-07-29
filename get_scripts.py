import os

import requests
from bs4 import BeautifulSoup
"""
Season 01(7)
Season 02(13)
Season 03(13)
Season 04(13)
Season 05(16)
"""


CURRENT_DIR = os.getcwd()


def write_file(*args):
    file_name, title, data = args
    file_name = "breaking_bad_{}.txt".format(file_name)
    if os.path.isdir(CURRENT_DIR + '/tmp'):
        if len(os.listdir(CURRENT_DIR + '/tmp')) > 0:
            print('tmp is not empty')
            return 0
    else:
        os.mkdir('tmp')
        tmp = CURRENT_DIR + '/tmp'
        with open(os.path.join(tmp, file_name), 'w+') as f_handler:
            f_handler.write(title)
            f_handler.write(data)


def generate_urls(episodes, url):
    urls = {}
    for episode in enumerate(episodes, 1):
        for e in range(1, episode[1] + 1):
            s_e_num = "s0{}e{}".format(episode[0], str(e).zfill(2))
            urls[s_e_num] = "{}{}".format(url, s_e_num)
    return urls


def get_script(url):
    title_script = []
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    # Website used a single h3 for the script title
    title = soup.find_all('h3')
    if len(title) == 1:
        title = title[0].text
    else:
        # warn user ?
        title = 'Title Not Located'
    # Check for zero length string
    script = soup.find_all('div', class_='scrolling-script-container')
    title_script = [title, script[0].text]

    return title_script


def get_all_scripts(episode_url):
    breaking_bad_scripts = {}
    for episode, url in episode_url.items():
        scraped_scripe = get_script(url)
        breaking_bad_scripts[episode] = scraped_scripe
    return breaking_bad_scripts


def main():
    episodes = [7, 13, 13, 13, 16]
    scrape_url = 'http://www.springfieldspringfield.co.uk/view_episode_scripts.php?tv-show=breaking-bad&episode='
    scripts = generate_urls(episodes, scrape_url)
    all_scripts = get_all_scripts(scripts)


if __name__ == '__main__':
    main()
