<template>
  <v-layout align-center justify-center row>
    <v-flex class="article" xs10>
      <v-col align="center">
      <template v-if="user != null">
          <h1>{{this.progress.completed === 0 ? "Welcome!" : "Welcome back!"}}</h1>
          <p>You are logged in as <b>{{user.user_keyword}}</b>!</p>
          <object
            type="image/svg+xml"
            id="ear"
            :height="$vuetify.breakpoint.xsOnly ? 200 : 300"
            data="/img/ear.svg"
            :style="{ 'background-image': this.createEarBackgroundString() }"
          >
            Ear
          </object>
          <!-- <div id="ear" :style="{ 'background-image': this.createEarBackgroundString() }"> -->
            <!-- TODO: Icon finden 👂 -->
          <!-- </div> -->
          <br>
          <br>
          <template v-if="this.progress.completed !== 0">
            <h2>{{progress.completed}} \ {{progress.all}}</h2>
            <p>You are <b>{{percent.toFixed(1)}}%</b> through!</p>
            <p v-if="this.progress.ratio !== 1">Keep on training!</p>
            <p v-else>Well done!</p>
            <!-- TODO: funktioniert noch nicht -->
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
      chap: null,
      loaded: false
    };
  },
  computed: {
      percent: function() {
        return this.progress.ratio*100;
      }
  },
  methods: {
    createEarBackgroundString() {
      // TODO: Modify, if character changes
      const offset_bottom_percent = 4.5;
      const offset_top_percent = 95.2;
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
            this.chap["title"] = this.$vuetify.breakpoint.xsOnly ? chapter.title : module.title + " / " + chapter.title;
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
    },
    update: function() {
      this.progress = this.getProgress();
      if (this.user != null) {
        if (this.user.logoff_chapter != null) {
          this.updateChapterInfo(this.user.logoff_chapter)
        }
      } else {
        if(this.$route.query.usr == null){
          this.$router.push("/");
        }
      }
    }
  },
  created: function() {
    if(this.user != null){
      this.update();
    }
  },
  watch: {
    takes: function() {
      if(this.user != null){
        this.progress = this.getProgress();
      }
    },
    user: function () {
      this.update();
      this.loaded = true;
    }
  }
}


</script>

<style scoped>
  #ear {
    /* fill: linear-gradient(180deg, #E5E5E5 41.3%, #2B81D6 41.4%);
    height: 50%;
    
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent; */
    /* height: 100px; */
    mask: url(/img/ear_mask.svg);
    background: black;
    mask-size: 100% 100%;
  }
  
  /* .icon {
    fill: url("data:image/svg+xml,<svg xmlns='img/ear.svg'><linearGradient id='grad'><stop offset='0%' stop-color='%23ff00cc'/><stop offset='100%' stop-color='%23333399'/></linearGradient></svg>#grad") purple;

  } */
  /* TODO: Support dark-theme */
  /* #ear .theme--dark {
    background-image:linear-gradient(180deg, #363636 49.9%, rgba(43,129,214) 50.1%);
  }*/
</style>