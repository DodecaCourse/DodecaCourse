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
  <div>
    <div
      v-for="(module, num) in modules"
      :key="module.id"
    >
      <ModuleItem
        :module="module"
        :completed-chapters="completedChapters"
        :empty-chapters="emptyChapters"
        :completed-modules="completedModules"
        :empty-modules="emptyModules"
        :num="num"
        :display-check="displayCheck"
        :active="$route.path.startsWith(module.path)"
      />
    </div>
  </div>
</template>


<script>
import ModuleItem from "./ModuleItem";
import api from "../api.js";
  
export default {
  name: "Modules",
  components: {
    ModuleItem
  },
  mixins: [api],
  data: function () {
    return {
      displayCheck: false,
      completedChapters: [],
      emptyChapters: [],
      completedModules: [],
      emptyModules: []
              
    };
  },
  watch: {
    takes: function() {
      if(this.user != null){
        this.displayCheck = true;
        this.updateCompleted();
      } else {
        this.displayCheck = false;
      }
    }

  },
  methods: {
    updateCompleted: function() {
      // console.log("updating completed chapters and modules. this may take a while...");
          
      // reset
      this.completedChapters = [];
      this.emptyChapters = [{}];
      this.completedModules = [];
      this.emptyModules = [];
      // TODO: Replace with for loops, i like .some() tho
      this.modules.forEach(module => {
        var m_compd = true;
        var m_empty = true;
          
        module.chapters.forEach(chapter => {
          // TODO: Remove
          var c_compd = true;
          var c_empty = true;
          // var total = 0;
          // var completed = 0;
          // var t_level_compd = [];
          this.targets.forEach(target => {
                
            if (chapter.id === target.chapter_id){
                  
              var take = this.takes[target.id];
                  
              if(target.levels !== 0){
                // completed += target.levels;
                c_empty = false;
                m_empty = false;
                  
                // does take exist?
                if (take != null){
                  //console.log(take)
                  if (target.levels === 1) {
                    if (take[1].completed === false) {
                      // console.log(target.id, " not completed")
                      c_compd = false;
                    } // else {
                    //   completed += 1;
                    // }
                  } else {
                    // At the moment a target is counted as completed, if at
                    // least one level is completed
                    // TODO: Change this behaviour
                    var t_compd = false;
                    for (var i=1; i<=target.levels;i++){
                      if (take[i] != null){
                        if (take[i].completed === true){
                          // completed += 1;
                          t_compd = true;
                          break;
                        }
                      }
                    }
                    if (!t_compd){
                      c_compd = false;
                    }
                  }
                      
                } else {
                  // console.log(target.id, " missing")
                  c_compd = false;
                }
              }
            }
          });
            
          if(c_empty){
            // console.log("empty chapter", chapter.id)
            this.emptyChapters.push(chapter.id);
          } else if(c_compd) {
            // this.completedChapters.push({
            //   "id": chapter.id,
            //   "total": total,
            //   "completed": completed
            // });
            this.completedChapters.push(chapter.id);
          } else {
            m_compd = false;
          }
        });
            
        if(m_empty){
          //console.log("empty module", module.id)
          this.emptyModules.push(module.id);
        } else if(m_compd) {
          this.completedModules.push(module.id);
        } else {
          m_compd = false;
        }
      });
          
    }
      
  }
};
</script>

<style scoped>
</style>
