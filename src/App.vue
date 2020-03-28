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
    * {
        box-sizing: border-box;
        margin: 0;
        padding: 0;
    }

    body {
        font-family: 'Rubik', sans-serif;
        line-height: 1.4;
    }
</style>