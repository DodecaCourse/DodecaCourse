<template>
  <div>
    <div v-bind:key="module.id" v-for="(module, num) in modules">
        <ModuleItem
          v-bind:module="module"
          :completed_chapters="completed_chapters"
          :empty_chapters="empty_chapters"
          :completed_modules="completed_modules"
          :empty_modules="empty_modules"
          :num="num"
          :display_check="display_check"
          :active="$route.path.startsWith(module.path)"/>
    </div>
  </div>
</template>


<script>
  import ModuleItem from "./ModuleItem";
  import structure from "../../public/structure.json";
  import api from "../api.js"
  
  export default {
      name: `Modules`,
      mixins: [api],
      components: {
          ModuleItem
      },
      props: ['curCourse'],
      data: function () {
          return {
              structure: {
                  "modules": [],
                  "chapters": [],
                  "targets": []
              },
              display_check: false,
              completed_chapters: [],
              empty_chapters: [],
              completed_modules: [],
              empty_modules: []
              
          }
      },
      computed: {
          modules: function () {
              return structure["modules"];
          },
          targets: function() {
            return structure["targets"];
          }
      },
      methods: {
        updateCompleted: function() {
          console.log("updating completed chapters and modules. this may take a while...");
          
          // reset
          this.completed_chapters = [];
          this.empty_chapters = [];
          this.completed_modules = [];
          this.empty_modules = [];
          // TODO: Replace with for loops, i like .some() tho
          this.modules.forEach(module => {
            var m_compd = true;
            var m_empty = true;
          
            module.chapters.forEach(chapter => {
              var c_compd = true;
              var c_empty = true;
              // var t_level_compd = [];
              this.targets.forEach(target => {
                
                if (chapter.id === target.chapter_id){
                  
                  var take = this.takes[target.id];
                  c_empty = false;
                  m_empty = false;
                  // does take exist?
                  if (take != null){
                    //console.log(take)
                    if (target.levels === 1) {
                      if (take[1].completed === false) {
                        // console.log(target.id, " not completed")
                        c_compd = false;
                      }
                    } else {
                      // At the moment a target is counted as completed, if at
                      // least one level is completed
                      // TODO: Change this behaviour
                      var t_compd = false;
                      for (var i=1; i<=target.levels;i++){
                        if (take[i] != null){
                          if (take[i].completed === true){
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
              });
            
              if(c_empty){
                // console.log("empty chapter", chapter.id)
                this.empty_chapters.push(chapter.id);
              } else if(c_compd) {
                this.completed_chapters.push(chapter.id);
              } else {
                m_compd = false;
              }
            });
            
            if(m_empty){
              //console.log("empty module", module.id)
              this.empty_modules.push(module.id);
            } else if(m_compd) {
              this.completed_modules.push(module.id);
            } else {
              m_compd = false;
            }
          });
          
        }
      
      },
      watch: {
        // user: function () {
        //   if(this.user != null){
        //     this.display_check = true;
        //     this.updateCompleted();
        //   } else {
        //     this.display_check = false;
        //   }
        // },
        takes: function() {
          if(this.user != null){
            this.display_check = true;
            this.updateCompleted();
          } else {
            this.display_check = false;
          }
        }
        
      }
  }
</script>

<style scoped>
</style>
