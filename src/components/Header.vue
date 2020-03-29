<template>
    <header class="header">
        <img src="../assets/fett.png" alt="FETT" width="80px">
        <h1><b>FETT</b></h1>
        <u>F</u>unctional <u>E</u>ar <u>T</u>raining <u>T</u>ool

        <div id="nav">
            <router-link to="/">Courses</router-link>  |
            <router-link to="/about">About</router-link>
        </div>
    </header>
</template>

<script>
    export default {
        name: 'Header'
    }
</script>

<style scoped>
    .header {
        background: #333333;
        color: white;
        text-align: left;
        padding: 10px;
    }

    .header a {
        color: #FFFFFF;
        padding-right: 2px;
        text-decoration: none;
    }

    .header * {
        box-sizing: border-box;
        margin: 0;
        padding: 0;
    }
</style>
