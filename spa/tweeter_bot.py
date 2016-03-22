# -*- coding: utf-8 -*-

import json
import random
import pandas as pd
import requests
from requests_oauthlib import OAuth1Session
from pprint import pprint
from credentials import twitter_api_key, twitter_api_secret, twitter_access_token, twitter_access_token_secret

# Read the .csv wrote by scrapy in a pandas.Dataframe
pets_data = pd.read_csv("pets_data.csv")

# Remove pets that are neither cats nor dogs
# TODO: add support for pets that are neither cats nor dogs
pets_data = (pets_data[pets_data["species"] != "autre"]).reset_index()

# Create a list of greetings
greetings = [
    "Salut ! Je suis",
    "Salut ! Je m'appelle",
    "Hey ! Je suis",
    "On m'appelle",
    "Bonjour, je suis",
    "Salut salut ! C'est",
    "Je suis",
    "Coucou, je suis",
    "Hello, c'est",
    "Coucou ! Je m'appelle",
    "Coucou, c'est"
]


def tweet(status, media=None):
    """Post a tweet on Twitter.
    
    The tweet can include an image.
    
    Parameters
    ----------
    status : str
        The status to be posted
    media : str, default to ``None``
        If present, add an image to the tweet.
        
    Returns
    -------
    Data about the tweet sent by the Twitter API
    
    """

    twitter = OAuth1Session(twitter_api_key, twitter_api_secret, twitter_access_token, twitter_access_token_secret)
    url = 'https://api.twitter.com/1.1/statuses/update{}.json'.format('_with_media' if media else '')
    params = {'status': status}
    files = {'media': media} if media else None
    print('POST', url, params)

    response = twitter.post(url=url, params=params, files=files)
    print(response.status_code, response.request.url)

    response.raise_for_status()
    data = response.json()
    pprint(data)

    return data


def has_tweeted_pet_already(pet_url, tweeted_path='.tweeted.json'):
    """Check if an item has already been tweeted.
    
    If not, the item is added to the "already tweeted" list.
    
    Parameters
    ----------
    pet_url : str
        The url of the item that is being checked. It acted like an UUID.
    tweeted_path : str, default to ``.tweeted.json``
        The .json file aka the "already tweeted" list.
        
    Returns
    -------
    ``True`` is the url is in the "already tweeted" list.
    ``False`` otherwise.
    
    """
    
    try:
        with open(tweeted_path) as already_tweeted:
            data = json.loads(already_tweeted.read())
    except IOError:
        data = {'tweeted': []}

    if pet_url in data['tweeted']:
        return True
    else:
        data['tweeted'].append(pet_url)
        with open(tweeted_path, 'w+') as already_tweeted:
            already_tweeted.write(json.dumps(data))
        return False



def choose_pet(pet_urls):
    """Choose the url of a pet that haven't been tweeted yet amongst a ndarray of urls.
        
    Parameters
    ----------
    pet_urls : pandas.Series
        A ndarray containing urls.
        
    Returns
    -------
    The url of a pet that haven't been tweeted yet.
    
    """

    random.shuffle(pet_urls)
    for pet_url in pet_urls:
        if not has_tweeted_pet_already(pet_url):
            return pet_url


def main():
    # Create a copy of the pandas.Dataframe so the shuffle doesn't affect the original one 
    pet_urls = pets_data['item_url'].copy()
    
    # Choose a pet to tweet
    pet_url = choose_pet(pet_urls)
    if not pet_url:
        print('All pets have already been tweeted')
        return

    print('Chose pet', pet_url)

    # Get the data of the chosen pet
    pet_data = pets_data[pets_data.item_url == pet_url]
    
    # Create the tweet status
    tweet_format = '[{departement}] {greeting} {name} ! Je suis {species} de type {breed}.\nPlus d\'infos : {url}'    
    status = tweet_format.format(
        greeting=random.choice(greetings),
        departement=pet_data.departement.tolist()[0],
        name=pet_data.name.tolist()[0],
        species=pet_data.species.tolist()[0],
        breed=pet_data.breed.tolist()[0],
        url=pet_data.item_url.tolist()[0]
    )
    print('Tweet ({} chars): {}'.format(len(status), status))

    # Add an image to the tweet, using the ``image_url`` data
    url = pet_data.image_url.tolist()[0]
    response = requests.get(url)
    pet_image = response.content

    # Tweet!!!
    tweet(status, media=pet_image)


if __name__ == '__main__':
    main()   
    