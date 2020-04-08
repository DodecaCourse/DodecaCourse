import axios from 'axios'

export default {
  data() {
    return {
      debug: true,
      flask_server: 'http://localhost:5000/',
      connection: true,
      
      // TODO: Siehe unten
      // currentuser: 'no current user requested',
      // allusers: 'no list of all users requested',
      // allmodules: 'no list of all modules requested',
      // allchapters: 'no list of all chapters requested',
      // alltakes: 'no list of all takes requested',
      // founduser: 'not found',
      // foundsettings: 'no settings found',
      // foundchapters: 'no chapters found',
      // search: '',
      // cookie: '',
      // random: 0,
      // tmp: 'no'
    }
  },
  methods: {
    fetch(url, cookies=false) {
      const path = this.flask_server + url
      if (this.debug) {
        console.log('FETCH: ' + path)
      }
      
      var axios_instance = null;
      if (cookies){
        axios_instance = axios.create({
          withCredentials: true
        })
      } else {
        axios_instance = axios.create()
      }
      // Promisse return
      // var instance = axios.create({
      //   withCredentials: true
      // })
      
      return axios_instance
        .get(path)
        .then(res => {
          return res.data;
        })
        .catch(err => {
          console.log(err)
          this.connection = false;
        });
    },
    getUserID(user_keyword) {
      return this.fetch('getuser_bykey/' + user_keyword);
    },
    getAllUsers() {
      return this.fetch('getallusers');
    },
    getAllmodules() {
      return this.fetch('getallmodules');
    },
    getAllChapters() {
      return this.fetch('getallchapters');
    },
    getAllTakes() {
      return this.fetch('getalltakes');
    },
    getRandom() {
      return this.fetch('random');
    },
    getChaptersOfmodule(module_id) {
      return this.fetch('getchapters_bymodule_id/' + module_id);
    },
    getChapters(user_id){
      return this.fetch('getchapters_byuser_id/' + user_id);
    },
    updateCurrentUser(){
      this.fetch('getcurrentuser', true)
        .then(usr => this.currentuser = usr);
    },
    getCurrentUser(){
      return this.fetch('getcurrentuser', true);
    },
    setCurrentUserToTextfield(){
      this.fetch('setcurrentuser/' + this.cookie, true)
        .then(res => {
          console.log(res);
          this.updateCurrentUser();
        });
    },
    updateSearch() {
      if (this.search.trim().length > 2) {
        this.getUserID(this.search.trim())
          .then(data => {
            this.founduser = data;
            if (!(this.founduser.user_id == null)) {
              this.getSettings(this.founduser.user_id)
                .then(data => (this.foundsettings = data));
              this.getChapters(this.founduser.user_id)
                .then(data => (this.foundchapters = data));
            } else {
              this.foundsettings = "";
              this.foundchapters = "";
            }
          });
      }

    },
    getSettings(user_id){
      return this.fetch('getsettings/' + user_id);
    }
  },
  // TODO: Überlegen ob beim mixin von von Daten "vorgeladen" werden
  // created() {
  //   // Testing getUserID for user_keyword test
  //   this.getUserID('test')
  //     .then(data => (this.founduser = data));
  //   // Testing allUsers
  //   this.getAllUsers()
  //     .then(data => (this.allusers = data));
  //   // Testing random functionality
  //   this.getRandom()
  //     .then(data => (this.random = data.rand));
  //   // Testing allmodules
  //   this.getAllmodules()
  //     .then(data => (this.allmodules = data));
  //   // Testing allchapters
  //   this.getAllChapters()
  //     .then(data => (this.allchapters = data));
  //   // Testing allchapters
  //   this.getAllTakes()
  //     .then(data => (this.alltakes = data));
  //
  //   this.updateCurrentUser();
  // }
}