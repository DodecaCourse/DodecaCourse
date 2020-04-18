# Dodeca
Functional Ear Training Course

## Project setup
```
git clone https://repo.wavel.de/vp/FETT.git
cd FETT
git submodule update --init 
npm install
```

Soundfonts: https://github.com/gleitz/midi-js-soundfonts
### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

## Backend server setup
### Create virtual environment and install packages
```
python3 -m venv env
source env/bin/activate
pip install -r reqs.txt
```
### Configuration
```
cp server/.env.example .env
```
Change the `SECRET_KEY` if you want to run in production.
### Running the development server
```
cd server
python app.py
```
### Running the production server
```
cd server
gunicorn --bind 0.0.0.0:5000 wsgi
```

## Linting
Lint your code by running
```
eslint --ext .js,.vue src
```
This will lint all .js and .vue files in the src folder. Run with `--fix` if you
want to automatically fix fixable warnings and erros.