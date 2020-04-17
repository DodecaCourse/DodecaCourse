<template>
  <v-layout align-center justify-center row>
    <v-flex class="article" xs10>
      <v-col align="center">
      <template v-if="user != null">
          <h1>{{this.progress.completed === 0 ? "Welcome!" : "Welcome back!"}}</h1>
          <p>You are logged in as <b>{{user.user_keyword}}</b>!</p>
          <v-img src="/img/ear.svg"></v-img>
          <div id="ear" :style="{ 'background-image': this.createEarBackgroundString() }">
            <!-- TODO: Icon finden 👂 -->
          </div>
          <template v-if="this.progress.completed !== 0">
            <h2>{{progress.completed}} \ {{progress.all}}</h2>
            <p>You are <b>{{percent.toFixed(1)}}%</b> through! Keep on training!</p>
          </template>

          <v-btn v-if="this.user.logoff_chapter == null || this.chap == null" to="/">
            start learning
          </v-btn>
          <v-btn v-else :to="this.chap.path">
            continue chapter <b>{{this.chap.num}}</b>: {{this.chap.title}}
          </v-btn>
      </template>
      <template v-else>
        <h1>You shouldn't be here!</h1>
      </template>
      </v-col>
    </v-flex>
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
      
      // offset_top: 15,
      // offset_bot: 15,
      chap: null
    };
  },
  computed: {
      targets: function() {
        return structure["targets"];
      },
      modules: function() {
        return structure["modules"];
      },
      percent: function() {
        return this.progress.ratio*100;
      }
  },
  methods: {
    createEarBackgroundString() {
      // TODO: Modify, if character changes
      const offset_bottom_percent = 24;
      const offset_top_percent = 80.3;
      const to_set = offset_top_percent - offset_bottom_percent;
      const lower = (this.percent * to_set / 100 + offset_bottom_percent).toFixed(1);
      let upper;
      if (this.percent < 0.1) upper = lower;
      else upper = (this.percent * to_set / 100 + offset_bottom_percent+0.1).toFixed(1);
      return `linear-gradient(0deg, ${this.filled_color} ${lower}%, ${this.empty_color} ${upper}%)`;
    },
    getProgress: function() {
      var count = 0;
      var count_completed = 0;
      this.targets.forEach(target => {
        count+= target.levels;
        var take = this.takes[target.id];
        if (take != null){
          //console.log(take);
          for(var i=target.levels; i>=0; i--) {
            if(take[i] != null){
              if (take[i].completed) {
                count_completed+=i;
                break;
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
    },
    updateChapterInfo: function(chapter_id){
      var num = `${Math.floor(chapter_id/1000)}.${chapter_id%1000}`;
      this.chap = null;
      this.modules.forEach(module => {
        module.chapters.forEach(chapter => {
          if(chapter.id === chapter_id){
            this.chap = this.copy(chapter);
            // modify path and title to also include module
            this.chap["path"] = module.path + chapter.path;
            this.chap["title"] = module.title + " / " + chapter.title;
          }
        });
      });
      
      if(this.chap != null){
        this.chap["num"] = num;
        return this.chap;
      } else {
        console.error("no chapter with chapter_id " + chapter_id + " was found");
        return null;
      }
    },
    copy: function(src) {
      return Object.assign({}, src);
    }
  },
  created: function() {
    this.progress = this.getProgress();
    var self = this;
    this.updateCurrentUser()
      .then( function() {
        if (self.user != null) {
          if (self.user.logoff_chapter != null) {
            self.updateChapterInfo(self.user.logoff_chapter)
          }
        } else {
          if(self.$route.query.usr == null){
            self.$router.push("/");
          }
        }
      });
    
  },
  watch: {
    takes: function() {
      if(this.user != null){
        this.progress = this.getProgress();
      }
    },
    user: function () {
      if (this.user == null) {
        this.$router.push("/");
      }
    }
  }
}


</script>

<style scoped>
  #ear {
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