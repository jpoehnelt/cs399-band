import requests
from bs4 import BeautifulSoup
from app.settings import STATICFILES_DIRS, BASE_DIR
import uuid
import os
import shutil
from app import fake
import json

# TODO make this into a command based argument

def delete_dir(d):
    """
    Deletes a directory if it exists.
    :param d: 
    :return:
    """
    if os.path.exists(d):
        shutil.rmtree(d)


def ensure_dir(f):
    """
    Checks if directory of the filename exists. 
    If it does not, it builds it.
    :param f: 
    :return:
    """
    d = os.path.dirname(f)
    if not os.path.exists(d):
        os.makedirs(d)


def download_file(url, album, name, ext='.mp3'):
    """
    Downloads a file and saves it to the album folder.
    :param url: actual url
    :param album: unique album identifier
    :param name: name for the file
    :param ext: extension defaults to mp3
    :return: new filename
    """
    local_filename = STATICFILES_DIRS[0] + '/albums/' + album.lower().replace(' ',
                                                                              '-') + '/' + name + ext
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
    # build album direcotry
    ensure_dir(STATICFILES_DIRS[0] + '/albums/')

    # where we are getting the data
    base_url = 'http://www.fakemusicgenerator.com'

    discography = []

    # how many albums to get and loop through
    for j in range(5):
        response = requests.get(base_url)

        soup = BeautifulSoup(response.text)

        # get the table, luckily only one, but no id, class etc to find it by
        table = soup.find_all('table')[0]

        album = {
            'id': str(uuid.uuid4())[:5],  # unique identifier
            'name': soup.find_all('span', attrs={'style': 'font-weight: 700;'})[0].string,
            'year': fake.dateTimeThisDecade().year,
            'tracks': []}

        # get column headers as store in array
        columns = [str(th.string).lower() for th in table.find_all('th')]

        track_number = 0

        # loop through the rows of the table
        for row in table.find_all('tr', attrs={'class': None}):
            track = {}
            # loop through the fields in the row
            for i, td in enumerate(row.find_all('td')):

                # todo clean this up
                a = td.find_all('a')
                if len(a) > 0:
                    # probably the url for the mp3
                    val = a[0].get('href')
                else:
                    # not the mp3 link
                    try:
                        # might be a track number
                        int(td.string)
                        track_number += 1
                        val = track_number
                    except:
                        # nope, something else
                        val = td.string

                # add key to track dictionary
                track[columns[i]] = val

            # download mp3 and then remove download url from track dictionary
            download_file(base_url + track['download'], album['id'], str(track['trk']))
            del track['download']

            # add track to album
            album['tracks'].append(track)

        # get cover and download to album folder
        cover_url = soup.find_all('img', attrs={'height': '300'})[0].get('src')
        download_file(base_url + cover_url, album['id'], 'cover', '.jpg')

        # add the album to the discography
        discography.append(album)

    with open(STATICFILES_DIRS[0] + '/albums/discography.json', 'w') as f:
        # save data as json file in static folder
        json.dump(discography, f)
