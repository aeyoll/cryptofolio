# Cryptofolio

Track gain and loss of your cryptocurrency portfolio.

## Installation

Requires [pipenv](https://github.com/pypa/pipenv)

```commandline
pipenv install
./manage.py migrate
```

## Setup

To fetch prices, set up a cron to an interval of your choice, launching this
command:

```commandline
./manage.py fetch_prices
```

## Usage

Go to the /admin/ section of the website, and add cryptocurrencies infos.
Then, just go to the homepage, and if the prices are fetched correctly, you
should see all the informations.
