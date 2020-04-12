<template>
  <v-container fluid class="cards">
    <h2>Login or generate a new username to save your progress!</h2>
    <v-row dense>
      <v-col>
        <v-card>
          <v-card-title>Register</v-card-title>
          <v-card-text>
            Generate a random user name. You'll need to save that username somewhere
            in order to restore your progress. You can allow us to set cookies, so you
            don't need to keep track if you are not deleting your cookies.
            Alternatively, you can copy a link or create a bookmark ending on "
            <b>?usr={{user}}</b>", that directly logs you in and puts you back to
            where you stopped.
            We will not save any personal data(e.g. names). By checking the below
            checkmark you allow us to save cookies on your system.
          </v-card-text>
        </v-card>
      </v-col>
      <v-col>
        <v-card>
          <v-card-title>Login</v-card-title>
          <v-card-text>
            Already have a username? Enter it here:
            <v-text-field />
            <v-btn>Login</v-btn>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<style scoped>
.cards {
  width: 80%;
}
</style>