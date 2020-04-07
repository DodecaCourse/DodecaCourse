<template>

  <div class="article">
    <h1>Hello World</h1>
    <v-chip
      v-if="connection"
      class="ma-2"
      text-color="white"
      color="green"
    >
      Connected
      <v-icon right>mdi-server-network</v-icon>
    </v-chip>
    <v-chip
      v-if="!connection"
      class="ma-2"
      text-color="white"
      color="red"
    >
      Disconnected
      <v-icon right>mdi-server-network-off</v-icon>
    </v-chip>
    <v-form method="post" action="http://localhost:5000/adduser">
      <v-text-field name="nm" label="userId" solo></v-text-field>
      <v-btn type="submit" rounded color="primary" dark>Add User</v-btn>
    </v-form>
    <v-form method="post" action="http://localhost:5000/generateuser">
      <v-btn type="submit" rounded color="error" dark>Generate User</v-btn>
    </v-form>
    <br>
    <br>
    <p><b>allusers:</b> {{allusers}} </p>
    <p><b>allmodules:</b> {{allmodules}} </p>
    <p><b>allchapters:</b> {{allchapters}} </p>
    <p><b>alltakes:</b> {{alltakes}} </p>
    <p><b>chapters1:</b> {{chapters1}} </p>
    <p><b>settings1:</b> {{settings1}} </p>
    <p><b>random:</b> {{random}} </p>
    <v-text-field name="search" v-model="search" label="search.." @input="updateSearch" solo></v-text-field>
    <p><b>founduser:</b> {{founduser}} </p>
    <p><b>foundsettings:</b> {{foundsettings}} </p>
    <p><b>foundchapters:</b> {{foundchapters}} </p>
    <!-- <p v-for="user in allusers" :key="user">
      <b>{{user.user_keyword}}</b>
    </p> -->
    <v-text-field name="cookie" v-model="cookie" label="set current user.." @input="updateCurrentUser" solo></v-text-field>
    <v-btn type="submit" rounded @click="setCurrentUserToTextfield" color="secondary" dark>Set Current User</v-btn>
    <p><b>currentuser:</b> {{currentuser}} </p>
  </div>

</template>

<script>

  import axios from 'axios'

  export default {
    name: 'ServerTest',
    data() {
      return {
        debug: true,
        flask_server: 'http://localhost:5000/',
        connection: true,
        currentuser: 'no current user',
        allusers: 'no users found',
        allmodules: 'no modules found',
        allchapters: 'no chapters found',
        alltakes: 'no takes found',
        chapters1: 'no chapters found',
        founduser: 'not found',
        foundsettings: 'no settings found',
        foundchapters: 'no chapters found',
        settings1: 'no settings found',
        search: '',
        cookie: '',
        random: 0,
        tmp: 'no'
      }
    },
    methods: {
      fetch(url) {
        const path = this.flask_server + url
        if (this.debug) {
          console.log('FETCH: ' + path)
        }
        // Promisse return
        return axios
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
      getAllchapters() {
        return this.fetch('getallchapters');
      },
      getAllTakes() {
        return this.fetch('getalltakes');
      },
      getRandom() {
        return this.fetch('random');
      },
      getchaptersOfmodule(module_id) {
        return this.fetch('getchapters_bymodule_id/' + module_id);
      },
      getchapters(user_id){
        return this.fetch('getchapters_byuser_id/' + user_id);
      },
      updateCurrentUser(){
        this.fetch('getcurrentuser')
          .then(usr => this.currentuser = usr);
      },
      setCurrentUserToTextfield(){
        this.fetch('setcurrentuser/' + this.cookie);
      },
      updateSearch() {
        if (this.search.trim().length > 2) {
          this.getUserID(this.search.trim())
            .then(data => {
              this.founduser = data;
              if (!(this.founduser.user_id == null)) {
                this.getSettings(this.founduser.user_id)
                  .then(data => (this.foundsettings = data));
                this.getchapters(this.founduser.user_id)
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
    created() {
      // Testing getUserID for user_keyword test
      this.getUserID('test')
        .then(data => (this.founduser = data));
      // Testing allUsers
      this.getAllUsers()
        .then(data => (this.allusers = data));
      // Testing random functionality
      this.getRandom()
        .then(data => (this.random = data.rand));
      // Testing allmodules
      this.getAllmodules()
        .then(data => (this.allmodules = data));
      // Testing allchapters
      this.getAllchapters()
        .then(data => (this.allchapters = data));
      // Testing allchapters
      this.getAllTakes()
        .then(data => (this.alltakes = data));
      // Testing getchaptersofmodule for module_id 1
      this.getchaptersOfmodule('1')
        .then(data => (this.chapters1 = data));
      // Testing getSettings for user_id test
      this.getSettings('1')
        .then(data => (this.settings1 = data));
        
      this.updateCurrentUser();
    }
  }

</script>
