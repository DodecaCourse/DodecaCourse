<template>
  <v-dialog
    width="500"
  >
    <template #activator="{ on }">
      <v-btn
        icon
        v-on="on"
      >
        <v-icon>
          mdi-cog
        </v-icon>
      </v-btn>
    </template>
    
    
    
    <v-card v-if="user!=null">
      <v-card-title
        class="headline grey lighten-2"
        primary-title
      >
        Settings
      </v-card-title>
      <v-list>
        <v-list-item-group
          v-model="settings"
          multiple
          active-class=""
        >
          <v-list-item>
            <v-list-item-content>
              <v-list-item-title>Theme</v-list-item-title>
              <v-list-item-subtitle>Select a theme and make the course easier to read</v-list-item-subtitle>
            </v-list-item-content>
            <v-list-item-action>
              <v-select
                :items="themes"
                append-outer-icon="mdi-theme-light-dark"
                menu-props="auto"
                hide-details
                label="Theme"
                single-line
              />
            </v-list-item-action>
          </v-list-item>
        </v-list-item-group>
      </v-list>
      <v-divider />

      <v-card-actions>
        <v-spacer />
        <v-btn
          color="primary"
          text
        >
          Return to course
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
import api from "./../api.js";

export default {
  name: "SettingsDialog",
  mixins: [api],
  props: {
    dialog: {
      type: Boolean,
      default: false
    }
  },
  data: function() {
    return {
      themes: [
        "Light", "Dark"
      ]
    };
  }
};
</script>