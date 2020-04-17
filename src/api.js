import axios from 'axios';
import structure from '../public/structure.json';

export default {
  data() {
    return {
      debug: false,
      flask_server: process.env.VUE_APP_BACKEND_SERVER,
      connection: true,
    }
  },
  computed: {
    user: {
      get: function () {
        return this.$root.$children[0].userProp;
      },
      set: function (usr) {
        this.$root.$children[0].userProp = usr;
      }
    },
    takes: {
      get: function () {
        return this.$root.$children[0].takesProp;
      },
      set: function (usr) {
        this.$root.$children[0].takesProp = usr;
      }
    },
    modules: function() {
      return structure['modules'];
    },
    targets: function() {
      return structure['targets']
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
          if(this.debug){
            console.log(err)
          }
          this.connection = false;
        });
    },
    getUserID(user_keyword) {
      return this.fetch('getuser_bykey/' + user_keyword);
    },
    getTakes(){
      return this.fetch('get_takes_by_user_id/' + this.user['user_id']);
    },
    updateCurrentUser(){
      // try gettin from session
      return this.fetch('getcurrentuser', true)
        .then(usr => {
          this.user = usr
          // try getting from query params
          if(this.user == null) {
            // Check if user with query params exists
            // and update
            this.getUserID(this.$route.query.usr)
              .then(usr => {
                if(usr != null){
                  this.setCurrentUser(usr.user_keyword);
                  this.user = usr;
                }
              });
          }
      });
      
    },
    // unused // Test
    // getCompletedLists(){
    //   return this.fetch('get_completed_by_user_id/' + this.user['user_id'])
    // },
    getCurrentUser(){
      return this.fetch('getcurrentuser', true);
    },
    setCurrentUser(user){
      return this.fetch('setcurrentuser/' + user, true)
          .then(usr => this.user = usr).then(this.updateTakes);
    },
    updateTakes(){
      return this.fetch('get_takes_by_user_id/' + this.user['user_id'])
          .then(takes => this.takes = takes);
    },
    setLogoffChapter(chapter_id){
      return this.fetch('set_logoff_chapter/' + this.user['user_id'] + "/" + chapter_id);
    },
    // getSettings(){
    //   return this.fetch('getsettings/' + this.user['user_id']);
    // },
    generateUser() {
      return this.fetch('generateuser');
    },
    logout(){
      this.user = null;
      return this.fetch('logout', true);
    },
    completeTarget(target_id, level) {
      return this.fetch('complete_target/' + this.user['user_id'] + '/' + target_id + '/' + level)
    },
    unsetCompleteTarget(target_id, level) {
      return this.fetch('unset_complete_target/' + this.user['user_id'] + '/' + target_id + '/' + level)
    }
  },
}
