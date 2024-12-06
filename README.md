# wolna_patologia

Aplikacja stworzona jako owoc bądź zalążek integracji chłopaków z Wolności.


## How to run:

Clone repository using `git clone` command and run:
```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python pato_appka/app.py
```

or build and run docker file using:

```
docker build -t flask-app .
docker run -p 5000:5000 flask-app
```
