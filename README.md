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
### Run the development server
```
cd server
python app.py
```
