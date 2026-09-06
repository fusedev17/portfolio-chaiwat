<script setup lang="ts">
const year = new Date().getFullYear()
</script>

<template>
  <footer class="border-t border-white/8 py-8">
    <div class="container-page flex flex-col items-center justify-between gap-3 text-xs text-slate-600 sm:flex-row">
      <p>© {{ year }} ชัยวัฒน์ สิงคิบุตร</p>
      <p class="font-mono">สร้างด้วย Nuxt 4 · Tailwind CSS</p>
    </div>
  </footer>
</template>
