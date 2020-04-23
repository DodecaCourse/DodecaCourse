/*
Copyright 2020 Maximilian Herzog, Hans Olischläger, Valentin Pratz, Philipp Tepel
This file is part of Dodeca Course.

Dodeca Course is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Dodeca Course is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Dodeca Course.  If not, see <https://www.gnu.org/licenses/>.
*/
import axios from "axios";
import structure from "../public/structure.json";

export default {
  data() {
    return {
      debug: false,
      flask_server: process.env.VUE_APP_BACKEND_SERVER,
      connection: true,
    };
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
      return structure["modules"];
    },
    targets: function() {
      return structure["targets"];
    }
    
  },
  methods: {
    fetch(url, cookies=false) {
      const path = this.flask_server + url;
      if (this.debug) {
        console.log("FETCH: " + path);
      }
      
      var axios_instance = null;
      if (cookies){
        axios_instance = axios.create({
          withCredentials: true
        });
      } else {
        axios_instance = axios.create();
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
            console.log(err);
          }
          this.connection = false;
        });
    },
    getUserID(user_keyword) {
      return this.fetch("getuser_bykey/" + user_keyword);
    },
    getTakes(){
      return this.fetch("get_takes_by_user_id/" + this.user["user_id"]);
    },
    
    updateCurrentUser(){
      // try gettin from session
      return this.fetch("getcurrentuser", true)
        .then(usr => {
          this.user = usr;
          // try getting from query params
          if(this.user == null && this.$route.query.usr !== undefined) {
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
      return this.fetch("getcurrentuser", true);
    },
    setCurrentUser(user){
      return this.fetch("setcurrentuser/" + user, true)
        .then(usr => this.user = usr).then(this.updateTakes);
    },
    updateTakes(){
      return this.fetch("get_takes_by_user_id/" + this.user["user_id"])
        .then(takes => this.takes = takes);
    },
    setLogoffChapter(chapter_id){
      return this.fetch("set_logoff_chapter/" + this.user["user_id"] + "/" + chapter_id);
    },
    // getSettings(){
    //   return this.fetch('getsettings/' + this.user['user_id']);
    // },
    generateUserKeyword() {
      return this.fetch("generate_user_keyword");
    },
    confirmUserKeyword(keyword) {
      return this.fetch("confirm_user_keyword/" + keyword)
        .then(usr => this.user = usr).then(this.updateTakes);
    },
    setLike(like) {
      var like_int = (like ? "1" : "0");
      return this.fetch("set_like/" + this.user["user_id"] + "/" + like_int);
    },
    getLikes() {
      return this.fetch("get_likes/");
    },
    logout(){
      this.user = null;
      return this.fetch("logout", true);
    },
    completeTarget(target_id, level) {
      return this.fetch("complete_target/" + this.user["user_id"] + "/" + target_id + "/" + level);
    },
    unsetCompleteTarget(target_id, level) {
      return this.fetch("unset_complete_target/" + this.user["user_id"] + "/" + target_id + "/" + level);
    }
  },
};
