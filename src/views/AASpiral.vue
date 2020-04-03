<template>
    <v-card
            class="d-inline-flex px-1 align-center justify-center" elevation="5" width="100%"
    >
        <v-container>
            <v-row>
                <v-speed-dial
                        v-model="fab"
                        transition="scale-transition"
                        fixed
                        direction="right"
                        open-on-hover
                >
                    <v-btn slot="activator" fab flat small color="info">
                        <v-icon>account_circle</v-icon>
                        <v-icon>close</v-icon>
                    </v-btn>
                </v-speed-dial>
            </v-row>
            <v-row>
                <v-btn color="blue" small fab elevation="1" v-on:click="bt(1)">
                </v-btn>
                <v-btn color="red" small fab elevation="1" v-on:click="bt(2)">
                </v-btn>
            </v-row>
        </v-container>
    </v-card>
</template>

<script>
    export default {
        name: "AASpiral",

        data : function(){
            return{
                scale: "major",
                root:"c",

                octave: 0,

                degree: 1,
            }
        },

        watch: {},

        methods: {
           playDegree : function (scale, root, degree, octave) {
                const note = degree + 7 * octave;
                window.alert(root + scale + note);
            },

            bt : function(deg){
                this.playDegree(this.key, deg, this.octave);
            },
        },


    }



</script>

<style scoped>

</style>