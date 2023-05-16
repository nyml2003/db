<template>
    <div>{{ msg }}</div>
  </template>
  
  <script setup>
  import { defineProps } from 'vue';
  const props = defineProps({
    msg: String
  })
  </script>
  