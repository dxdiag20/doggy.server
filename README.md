# doggy.server
### A server that receive an image and respond with best-similar dog

## Requirements
Flask==1.0.2
waitress==1.1.0

## Deploying
pip install -r requirements.txt
waitress-serve --call 'app:create_app'
