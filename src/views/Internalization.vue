<template>

  <div class="content">
    <h1>Internalization</h1>
    <InternalizationPlayer></InternalizationPlayer>
  </div>

</template>

<script>

  import InternalizationPlayer from '../components/InternalizationPlayer'
  export default {
    name: 'Internalization',
    components: { InternalizationPlayer }
  }

</script>

<style scoped>
h1 {
  padding: 10px;
}
</style>
