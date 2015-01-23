from app import fake
from app.settings import STATICFILES_DIRS
import json


def generate_events(num):
    """
    Function generates a number of events using the faker python package.
    :param num:
    :return: List
    """
    tour_events = []

    for i in range(num):
        events.append({
            'date': fake.dateTimeBetween('now', '+1y'),
            'city': fake.city(),
            'state': fake.stateAbbr(),
            'description': fake.text()
        })

    tour_events.sort(key=lambda x: x['date'])

    return tour_events


def get_discography():
    """
    Opens discography json file and loads the data to be passed to templates.
    :return:
    """
    with open(STATICFILES_DIRS[0] + '/albums/discography.json') as f:
        return json.load(f)


events = generate_events(10)
discography = get_discography()
