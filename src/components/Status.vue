<tamplate>
  
  <pre>Logged in as: </pre><b>{{user}}</b>
  <v-btn icon>
    <v-icon>mdi-logout</v-icon>
  </v-btn>
  <v-btn icon>
    <v-icon>mdi-heart</v-icon>
  </v-btn>
  <v-btn icon>
    <v-icon>mdi-cog</v-icon>
  </v-btn>
</template>

<script>
  export default {
      name: "Status",
      created () {
      }
  }
</script>
