<template>
  <v-layout align-center justify-center row>
    <template v-if="user != null">
      <div id="ear" :style="{ 'background-image': this.createEarBackgroundString() }">
        👂 <!-- TODO: Icon finden -->
      </div>
      <v-flex class="article" xs20>
        <h1>{{this.progress.completed === 0 ? "Welcome!" : "Welcome back!"}}</h1>
        <p>You are logged in as <b>{{user.user_keyword}}</b>!</p>
        <template v-if="this.progress.completed !== 0">
          <h2>{{progress.completed}} \ {{progress.all}}</h2>
          <p>You are <b>{{percent.toFixed(1)}}%</b> through! Keep on training!</p>
        </template>
        <p><i>TODO: Styling </i></p>
        
        <v-btn v-if="this.user.logoff_chapter == null || this.chap == null" to="/">
          start learning
        </v-btn>
        <v-btn v-else :to="this.chap.path">
          continue chapter <b>{{this.chap.num}}</b>: {{this.chap.title}}
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
      // TODO: Modify, if character changes
      offset_top: 15,
      offset_bot: 15,
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
      var left = 100-this.offset_top-this.offset_bot;
      var upper = this.percent.toFixed(1)*left/100 + this.offset_bot;
      var lower = (this.percent + 0.2).toFixed(1)*left/100 + this.offset_bot;
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
        }
      });
    
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