import requests
from bs4 import BeautifulSoup
from app.settings import STATICFILES_DIRS, BASE_DIR
import uuid
import os
import shutil
from app import fake
import json


# delete existing albums
def delete_dir(d):
    if os.path.exists(d):
        shutil.rmtree(d)


def ensure_dir(f):
    d = os.path.dirname(f)
    if not os.path.exists(d):
        os.makedirs(d)


def download_file(url, album, track, ext='.mp3'):
    local_filename = STATICFILES_DIRS[0] + '/albums/' + album.lower().replace(' ',
                                                                              '-') + '/' + track + ext
    ensure_dir(local_filename)
    r = requests.get(url, stream=True)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)
                f.flush()
    return local_filename


if __name__ == "__main__":


    # remove existing albums
    delete_dir(STATICFILES_DIRS[0] + '/albums/')
    ensure_dir(STATICFILES_DIRS[0] + '/albums/')

    base_url = 'http://www.fakemusicgenerator.com'

    discography = []

    for j in range(5):
        response = requests.get(base_url)

        soup = BeautifulSoup(response.text)

        table = soup.find_all('table')[0]

        album = {
            'id': str(uuid.uuid4())[:5],
            'name': soup.find_all('span', attrs={'style': 'font-weight: 700;'})[0].string,
            'year': fake.dateTimeThisDecade().year,
            'tracks': []}

        # get headers
        columns = [str(th.string).lower() for th in table.find_all('th')]

        track_number = 0

        for row in table.find_all('tr', attrs={'class': None}):
            track = {}
            for i, td in enumerate(row.find_all('td')):
                a = td.find_all('a')
                if len(a) > 0:
                    val = a[0].get('href')
                else:
                    try:
                        int(td.string)
                        track_number += 1
                        val = track_number
                    except:
                        val = td.string

                track[columns[i]] = val

            download_file(base_url + track['download'], album['id'], str(track['trk']))
            del track['download']
            album['tracks'].append(track)

        cover_url = soup.find_all('img', attrs={'height': '300'})[0].get('src')
        download_file(base_url + cover_url, album['id'], 'cover', '.jpg')

        discography.append(album)

    with open(STATICFILES_DIRS[0] + '/albums/discography.json', 'w') as f:
        json.dump(discography, f)
