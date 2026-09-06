<script setup lang="ts">
defineProps<{
  eyebrow: string
  title: string
  description?: string
}>()
</script>

<template>
  <div class="max-w-2xl">
    <span class="section-eyebrow">
      <span class="h-px w-6 bg-accent-400/60" />
      {{ eyebrow }}
    </span>
    <h2 class="mt-3 text-2xl font-semibold sm:text-3xl">{{ title }}</h2>
    <p v-if="description" class="mt-3 text-sm leading-relaxed text-slate-400 sm:text-base">
      {{ description }}
    </p>
  </div>
</template>
