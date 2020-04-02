<template>
<div class="article">
  <h1>Hello World</h1>
  <v-form method="post" action="http://localhost:5000/set">
    <v-text-field name="nm" label="userId" solo></v-text-field>
    <v-btn type="submit" rounded color="primary" dark>Set Cookie</v-btn>
  </v-form>
  <p><b>msg:</b> {{user}} </p>
  <p><b>random:</b> {{random}} </p>
</div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'ServerTest',
  data() {
    return {
      user: 'userID not set!',
      random: 0
    };
  },
  methods: {
    getUserID() {
      const path = 'http://localhost:5000/get';
      axios.get(path)
        .then((res) => {
          console.log(res)
          this.user = res.data;
        })
        .catch(err => console.log(err) );
    },
    getRandom() {
      const path = 'http://localhost:5000/random';
      axios.get(path)
      .then(res => {
        this.random = res.data.rand;
        // console.log(res)
      })
      .catch(err => console.log(err) );
    }
  },
  created() {
    this.getUserID();
    this.getRandom();
  },
};
</script>
