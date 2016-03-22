# CutePetsFrance [@Adoptez_moi](https://twitter.com/Adoptez_Moi)

A twitter bot that posts a random adoptable pet from the [SPA](http://www.spa.asso.fr/adopter-animaux).

Heavily inspired from [CutePetsAustin](https://github.com/open-austin/CutePetsAustin).

Tweeting at [@Adoptez_moi](https://twitter.com/Adoptez_Moi).

## Quickstart

1. Configure `credentials.py`
2. Install the dependencies `pip install -r requirements.txt`
3. (otpional) Crawl the SPA website `rm pets_data.csv && scrapy crawl spa-crawler -o pets_data.csv`
4. Tweet a random adoptable pet `python bot.py`

## Setup

### Installation

- Clone the repo `git clone git@github.com:seiteta/CutePetsFrance.git`
- Configure `credentials.py` with your PetHarbor.com Shelter ID(s), Twitter API Key and Access Token:
	
```py
twitter_api_key = 'XXXXX'
twitter_api_secret = 'XXXXX'
twitter_access_token = 'XXXXX'
twitter_access_token_secret = 'XXXXX'
```

- Optionally, create and activate a [virtual environment](http://virtualenv.readthedocs.org/en/latest/)
- Install the python dependencies with `pip install -r requirements.txt`
- Tweet a random adoptable pet with `python bot.py`
- Optionally, schedule a cron job to execute `meow.py` every few hours and crawl the SPA website every few days

### Twitter

1. Create a new Twitter app.
2. On the API key tab for the Twitter app, modify permissions so the app can `Read` and `Write`.
   Create an access token. On the API Key tab in Twitter for the app, click Create my access token. *Note: It's important to change permissions to `Read/Write` before generating the access token. The access token is keyed for the specific access level and will not be updated when changing permissions.*
4. Copy the `API Key` and `Access Token` into `credentials.py`

## License

The MIT License (MIT)
