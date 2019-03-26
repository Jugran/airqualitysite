import json
from urllib.request import urlopen

URL = 'https://api.openaq.org/v1/{QUERY}'


def get_data(query, param='', limit=10000):
    param = param.replace(' ', '+')
    url = URL.format(QUERY=query) + '?' + param + '&limit=' + str(limit)

    response = urlopen(url)
    assert response.code == 200, 'Response code %d' % response.code

    json_data = json.loads(response.read())

    if query == 'latest':
        data = {}
        measurements = json_data['results'][0]['measurements']
        for pollutant in measurements:
                data[pollutant['parameter']] = str(pollutant['value']) + ' ' + pollutant['unit']
        return data
    elif query == 'countries':  # return list of tuples of name an code
        return tuple((country['code'], country['name']) for country in json_data['results'])
    elif query == 'cities':
        return tuple((city['city'] for city in json_data['results']))
    elif query == 'locations':
        return tuple((location['location'] for location in json_data['results']))
