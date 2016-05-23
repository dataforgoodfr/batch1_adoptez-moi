# [@Adoptez_moi](https://twitter.com/Adoptez_Moi)

A twitter bot that posts a random adoptable pet from the [SPA](http://www.spa.asso.fr/adopter-animaux).

Heavily inspired by [CutePetsAustin](https://github.com/open-austin/CutePetsAustin).

Tweeting at [@Adoptez_moi](https://twitter.com/Adoptez_Moi).

## Quickstart

1. Configure `credentials.py`
2. Install the dependencies `pip install -r requirements.txt`
3. (optional) Crawl the SPA website `rm pets_data.csv && scrapy crawl spa-crawler -o pets_data.csv`
4. Tweet a random adoptable pet `python bot.py`

## Setup

### Installation

- Clone the repo `git clone git@github.com:seiteta/CutePetsFrance.git`
- Configure `credentials.py` with your Twitter API Key and Access Token:
	
```py
twitter_api_key = 'XXXXX'
twitter_api_secret = 'XXXXX'
twitter_access_token = 'XXXXX'
twitter_access_token_secret = 'XXXXX'
```

- Optionally, create and activate a [virtual environment](http://virtualenv.readthedocs.org/en/latest/)
- Install the python dependencies with `pip install -r requirements.txt`
- Tweet a random adoptable pet with `python bot.py`
- Optionally, schedule a cron job to execute `cp pets_data.csv{,.bak} && rm pets_data.csv && scrapy crawl spa-crawler -o pets_data.csv` every few days
- Optionally, schedule a cron job to execute `bot.py` every few hours

### Twitter

1. Create a new [Twitter app](https://apps.twitter.com/).
2. On the Keys and Access Tokens tab in Twitter for the app, click Create my access token.
3. Copy the `API Key` and `Access Token` into `credentials.py`

## License

The MIT License (MIT)
