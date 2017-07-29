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
    file_name = "breaking_bad_s0{}.txt".format(file_name)
    if os.path.isdir(CURRENT_DIR + '/tmp'):
        if len(os.listdir(CURRENT_DIR + '/tmp')) > 0:
            print('tmp is not empty')
            return 0
    else:
        os.mkdir('tmp')
        tmp = CURRENT_DIR + '/tmp'
        with open(os.path.join(tmp, file_name), 'w+') as f_handler:
            f_handler.write(title + '\n')
            f_handler.write(data)


def get_bb_scripts(episodes, url):

    for episode in enumerate(episodes, 1):
        for e in range(1, episode[1] + 1):
            s_e_num = "{}e{}".format(episode[0], str(e).zfill(2))
            page = requests.get("{}{}".format(url, s_e_num))

            soup = BeautifulSoup(page.content, 'html.parser')
            title = soup.find_all('h3')
            title = title[0].contents[0]
            script = soup.find_all('div', class_='scrolling-script-container')
            script = script[0]
            write_file(s_e_num, str(title), str(script))
            break


def main():
    episodes = [7, 13, 13, 13, 16]
    breaking_bad = 'http://www.springfieldspringfield.co.uk/view_episode_scripts.php?tv-show=breaking-bad&episode=s0'
    get_bb_scripts(episodes, breaking_bad)

if __name__ == '__main__':
    main()
