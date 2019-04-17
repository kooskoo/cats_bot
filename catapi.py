import requests


def get_breeds_list():
    breeds_request = requests.get('https://api.thecatapi.com/v1/breeds').json()
    breeds_list = ''
    for i in breeds_request:
        item = (i['name'] + ': ' + i['id'] + '\n')
        breeds_list += item
    return breeds_list


def cat_by_breed(breed=''):
    if not breed:
        breed = ''
    else:
        breed = breed[0]
    request = requests.get('https://api.thecatapi.com/v1/images/search?breed_ids=' + str(breed)).json()
    pic_url = request[0]['url']
    return pic_url


breeds = get_breeds_list()
