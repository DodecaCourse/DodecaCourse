<!--
Copyright 2020 Maximilian Herzog, Hans Olischläger, Valentin Pratz, Philipp Tepel
This file is part of Dodeca Course.

Dodeca Course is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Dodeca Course is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Dodeca Course.  If not, see <https://www.gnu.org/licenses/>.
-->
<template>
  <v-layout
    align-center
    justify-center
    row
  >
    <v-flex
      class="article"
      xs10
    >
      <v-col align="center">
        <template v-if="user != null">
          <h1>{{ progress.completed === 0 ? "Welcome!" : "Welcome back!" }}</h1>
          <p>You are logged in as <b>{{ user.user_keyword }}</b>!</p>
          <object
            id="ear"
            type="image/svg+xml"
            :height="$vuetify.breakpoint.xsOnly ? 200 : 300"
            data="/img/ear.svg"
            :style="{ 'background-image': createEarBackgroundString() }"
          >
            Ear
          </object>
          <br>
          <br>
          <template v-if="progress.completed !== 0">
            <h2>{{ progress.completed }} \ {{ progress.all }}</h2>
            <p>You are <b>{{ percent.toFixed(1) }}%</b> through!</p>
            <p v-if="progress.ratio !== 1">
              Keep on training!
            </p>
            <p v-else>
              Well done!
            </p>
          </template>

          <v-btn
            v-if="user.logoff_chapter == null || chap == null"
            to="/intro"
          >
            start learning
          </v-btn>
          <v-btn
            v-else
            id="continue"
            :to="chap.path"
            style="max-width: 90vw; height:auto;min-height: 36px"
          >
            continue chapter <b>{{ chap.num }}:</b> {{ chap.title }}
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
  name: "Home",
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
  },
  created: function() {
    this.update();
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
    },
    update: function() {
      this.progress = this.getProgress();
      if (this.user != null) {
        if (this.user.logoff_chapter != null) {
          this.updateChapterInfo(this.user.logoff_chapter);
        }
      } else {
        if(this.$route.query.usr == null){
          const self = this;
          setTimeout(function () {
            if (self.user == null) {
              this.$router.push("/intro");
            }
          });
        }
      }
    }
  }
};


</script>

<style>
  #ear {
    mask: url(/img/ear_mask.svg);
    background: black;
    mask-size: 100% 100%;
  }
  #continue .v-btn__content {
    max-width: 100%;
    flex-wrap: wrap;
  }
</style>