# Dodeca - Functional Ear Training Course
[Dodeca](https://dodeca.wavel.de) is a Creative Commons online course to get started with functional ear training.
Structure & content are based on material of [Ear Training HQ](https://eartraininghq.com/), but
interactive exercises, tests and translations have been added, to make the course more accessible.

## Contributing
Being an open source project, everyone can help to make this course better. So if you find
a typo, have an idea how to rephrase a paragraph or even want to add a translation,
just open an issue to get in touch or file a pull request.

## Credits
This project uses:
- [Vue.js](https://vuejs.org/) - Frontend JavaScript Framework
- [Vuetify](https://vuetifyjs.com/) - Material Design Component Framework for Vue.js
- [WebAudioMIDI.js](https://github.com/valentin12/WebAudioMIDI.js) - Play MIDI notes in the browser
- [MIDI.js Soundfonts](https://github.com/mudcube/MIDI.js) - Soundfonts for MIDI.js
- [PitchDetect](https://github.com/cwilso/PitchDetect) - Simple pitch detection

## Project setup
```
git clone https://github.com/DodecaCourse/DodecaCourse.git
cd DodecaCourse
git submodule update --init 
npm install
```

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

## Linting & Code Style
```
eslint --ext .js,.vue src
```
This will lint all .js and .vue files in the src folder. Run with `--fix` if you
want to automatically fix fixable warnings and errors.

Run pycodestyle (pep8) in `server` to apply Python style checking:
```
pycodestyle --show-pep8 --show-source *.py
```

## Licensing
The Dodeca Course structure & content is based on the Ear Training HQ product suite -
80/20 Ear Training, Hear. Sing. Win. and Play & Train, created by Scott Edwards.
It was originally published at <a href="https://EarTrainingHQ.com">https://EarTrainingHQ.com</a>.
The material is used under [CC BY-SA](http://creativecommons.org/licenses/by-sa/4.0/).

The content of the Dodeca Course is licensed under [CC BY-SA](http://creativecommons.org/licenses/by-sa/4.0/),
the frontend and backend code is licensed under [GNU GPL](https://www.gnu.org/licenses/licenses.html#GPL).
