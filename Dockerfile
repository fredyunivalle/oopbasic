FROM python:3.7-slim

WORKDIR /app

COPY . .

CMD [ "python" , "App.py" ]
##docker run --rm -v F:\Univalle\2022\01\DS2\OOPcode:/app fredyball/poo