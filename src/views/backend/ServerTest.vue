<template>
<div class="article">
  <h1>Hello World</h1>
  <v-form method="post" action="http://localhost:5000/setcookie">
    <v-text-field name="nm" label="userId" solo></v-text-field>
    <v-btn type="submit" rounded color="primary" dark>Set Cookie</v-btn>
  </v-form>
  <p><b>msg:</b> {{msg}} </p>
</div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'ServerTest',
  data() {
    return {
      msg: '',
    };
  },
  methods: {
    getCookie() {
      const path = 'http://localhost:5000/getcookie';
      axios.get(path)
        .then((res) => {
          this.msg = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getCookie();
  },
};
</script>
