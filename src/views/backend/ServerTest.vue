<template>

  <div class="article">
    <h1>Hello World</h1>
    <h2>Welcome to Testing Area 51</h2>
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
    <p><b>allchapters:</b> {{allchapters}} </p>
    <p><b>allsections:</b> {{allsections}} </p>
    <p><b>sections1:</b> {{sections1}} </p>
    <p><b>random:</b> {{random}} </p>
    <v-text-field name="search" v-model="search" label="search.." @input="updateSearch" solo></v-text-field>
    <p><b>founduser:</b> {{founduser}} </p>
    <p v-for="user in allusers" :key="user">
      <b>{{user.user_keyword}}</b>
    </p>
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
        allusers: 'no users found',
        allchapters: 'no chapters found',
        allsections: 'no sections found',
        sections1: 'no sections found',
        founduser: 'not found',
        search: '',
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
          .catch(err => console.log(err))
      },
      getUserID(user_keyword) {
        return this.fetch('getuser_bykey/' + user_keyword)
      },
      getAllUsers() {
        return this.fetch('getallusers')
      },
      getAllChapters() {
        return this.fetch('getallchapters')
      },
      getAllSections() {
        return this.fetch('getallsections')
      },
      getRandom() {
        return this.fetch('random')
      },
      getSectionsOfChapter(chapter_id) {
        return this.fetch('getsections_bychapter_id/' + chapter_id)
      },
      updateSearch() {
        if (this.search.trim().length > 2) {
          this.getUserID(this.search.trim()).then(data => (this.founduser = data))
        }
      }
    },
    created() {
      // Testing getUserID for user_keyword test
      this.getUserID('test')
        .then(data => (this.founduser = data))
      // Testing allUsers
      this.getAllUsers()
        .then(data => (this.allusers = data))
      // Testing random functionality
      this.getRandom()
        .then(data => (this.random = data.rand))
      // Testing allChapters
      this.getAllChapters()
        .then(data => (this.allchapters = data))
      // Testing allSections
      this.getAllSections()
        .then(data => (this.allsections = data))
      // Testint getSectionsofChapter for chapter_id 1
      this.getSectionsOfChapter('1')
        .then(data => (this.sections1 = data))
    }
  }

</script>
