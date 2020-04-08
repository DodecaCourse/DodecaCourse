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
  import api from '../../api.js'
  
  export default {
    name: 'ServerTest',
    mixins: [
      api
    ],
    data: function(){
      return {
        chapters1: 'no chapters1 found',
        settings1: 'no settings1 found',
        currentuser: 'no current user requested',
        allusers: 'no list of all users requested',
        allmodules: 'no list of all modules requested',
        allchapters: 'no list of all chapters requested',
        alltakes: 'no list of all takes requested',
        founduser: 'not found',
        foundsettings: 'no settings found',
        foundchapters: 'no chapters found',
        search: '',
        cookie: '',
        random: 0,
        tmp: 'no'
      };
    },
    created: function(){
      // Testing getchaptersofmodule for module_id 1
      this.getChaptersOfmodule('1')
        .then(data => (this.chapters1 = data));
      // Testing getSettings for user_id test
      this.getSettings('1')
        .then(data => (this.settings1 = data));
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
      this.getAllChapters()
        .then(data => (this.allchapters = data));
      // Testing allchapters
      this.getAllTakes()
        .then(data => (this.alltakes = data));
    
      this.updateCurrentUser();
    }
  }
</script>
