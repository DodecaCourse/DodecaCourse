# FETT
Functional Ear Training Tool

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

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).

### Knowledge base
Use
```
/* global var_name */
```
to avoid `no-undef` errors in `eslint` (https://stackoverflow.com/questions/58579425/vue-npm-run-serve-eslint-global-variable-is-not-defined-within-a-component)