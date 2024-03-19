<template>
  <div id="app">
    <!-- Use router-view to render the component based on the current route -->
    <router-view></router-view>
  </div>
</template>

<script>
// No need to import LoginForm here as it will be dynamically rendered by Vue Router

export default {
  name: 'App'
}
</script>
