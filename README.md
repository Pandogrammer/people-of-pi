# People of Politeia

People of Politeia (PoP) is an alternative explorer for Politeia data. Instead of providing proposal centered views, it focuses on users and discussions.

This web app was first built for the Decred en Español Hackathon.

## Rankings

At the core of PoP are these ranking views which allow to view user participation during a period of time.

Currently, PoP only offers 3 rankings:

1. Current Season (current month) `/current`
1. Previous Season (previous month) `/previous`
1. Historical Ranking (since the beginning of Pi) `/historical`

## User pages

`/user/<username>`
PoP also uses Politeia data to provide much richer user profiles than Pi.

## Deploying and Running

People of Politeia is a Flask web application. In order to run your own instance you must:

1. Run the updater `update_db.py` and wait for it to finish once. If not stopped it will run every 1 hour.
1. set up an environment variable called `FLASK_APP` and set it to `app.py`. Command: `export FLASK_APP=app.py`
`export FLASK_ENV=production`
1. Run the flask app with `flask run`

## Development

To run a development instance first set up an environment variable called `FLASK_ENV` and set it to `development`.
`export FLASK_ENV=development`

## Demo

Demo with preloaded data here: http://34.86.240.81:8080/