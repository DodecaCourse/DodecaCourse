<template>
  <v-layout align-center justify-center row>
    <template v-if="user != null">
      <div class="mdi mdi-ear-hearing" id="ear" :style="{ 'background-image': this.createEarBackgroundString() }" />
      <v-flex class="article" xs20>
    
        
        <h1>Hi!</h1>
        <p>You are logged in as <b>{{user.user_keyword}}</b>!</p>
        <h2>{{progress.completed}} \ {{progress.all}}</h2>
        <p>You are <b>{{percent.toFixed(1)}}%</b> through! Keep on training!</p>
        <p><i>TODO: Styling </i></p>
        
        <v-btn v-if="this.user.logoff_chapter == null" to="/introduction">
          start learning
        </v-btn>
        <v-btn v-else to="/introduction">
          continue chapter {{this.user.logoff_chapter}}
        </v-btn>
      </v-flex>
    </template>
    <template v-else>
      <h1>You shouldn't be here!</h1>
    </template>
  </v-layout>
</template>

<script>
import api from "../api.js";
import structure from "../../public/structure.json";
export default {
  name: 'Home',
  mixins: [api],
  data: function() {
    return {
      progress: {
        all: 100,
        completed: 0,
        ratio: 0
      },
      empty_color: "#E5E5E5",
      filled_color: "#2B81D6",
      
      
    };
  },
  computed: {
      targets: function() {
        return structure["targets"];
      },
      percent: function() {
        return this.progress.ratio*100;
      }
  },
  methods: {
    createEarBackgroundString() {
      const offset_bottom_percent = 24;
      const offset_top_percent = 80.3;
      const to_set = offset_top_percent - offset_bottom_percent;
      var upper = (this.percent * to_set / 100 + offset_bottom_percent).toFixed(1);
      var lower = (this.percent * to_set / 100 + offset_bottom_percent+ 0.2).toFixed(1);
      var str = `linear-gradient(0deg, ${this.filled_color} ${lower}%, ${this.empty_color} ${upper}%)`;
      // console.log(str);
      return str;
    },
    getProgress: function() {
      var count = 0;
      var count_completed = 0;
      this.targets.forEach(target => {
        count+= target.levels;
        var take = this.takes[target.id];
        if (take != null){
          //console.log(take);
          for(var i=1; i<=target.levels; i++) {
            if(take[i] != null){
              if (take[i].completed) {
                count_completed++;
              }
            }
          }
        }
        
      });
      return {
        all: count,
        completed: count_completed,
        ratio: count_completed/count
      };
    }
  },
  created: function() {
    this.progress = this.getProgress();
  },
  watch: {
    takes: function() {
      if(this.user != null){
        this.progress = this.getProgress();
      }
    }
    
  }
}


</script>

<style scoped>
  #ear {
    font-size: 15em;
    /*background-image: linear-gradient(180deg, #E5E5E5 41.3%, #2B81D6 41.4%);*/
    /* */
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
  }
  /* TODO: Support dark-theme */
  /* #ear .theme--dark {
    background-image:linear-gradient(180deg, #363636 49.9%, rgba(43,129,214) 50.1%);
  }*/
</style>