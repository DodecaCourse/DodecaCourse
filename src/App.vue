<template>
    <div id="app">
        <Header />
        <router-view/>
    </div>
</template>

<script>
import Header from "./components/Header";

export default {
    name: "App",
    components: {
        Header
    }
}
</script>

<style>

    body {
        font-family: 'Rubik', sans-serif;
        line-height: 1.4;
        margin: 0;
        padding: 0;
    }

    div.content {
        margin: 5%;
    }

    .noselect {
      -webkit-touch-callout: none; /* iOS Safari */
        -webkit-user-select: none; /* Safari */
         -khtml-user-select: none; /* Konqueror HTML */
           -moz-user-select: none; /* Old versions of Firefox */
            -ms-user-select: none; /* Internet Explorer/Edge */
                user-select: none; /* Non-prefixed version, currently
                                      supported by Chrome, Opera and Firefox */
    }
</style>
