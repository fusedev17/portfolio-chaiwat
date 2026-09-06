<script setup lang="ts">
const links = [
  { label: 'เกี่ยวกับ', href: '#about' },
  { label: 'ประสบการณ์', href: '#experience' },
  { label: 'ทักษะ', href: '#skills' },
  { label: 'ผลงาน', href: '#projects' },
  { label: 'ติดต่อ', href: '#contact' },
]

const scrolled = ref(false)
const menuOpen = ref(false)

function onScroll() {
  scrolled.value = window.scrollY > 12
}
onMounted(() => {
  onScroll()
  window.addEventListener('scroll', onScroll, { passive: true })
})
onUnmounted(() => window.removeEventListener('scroll', onScroll))
</script>

<template>
  <header
    class="fixed inset-x-0 top-0 z-50 transition-all duration-300"
    :class="scrolled ? 'border-b border-white/8 bg-ink-900/80 backdrop-blur-lg' : 'border-b border-transparent'"
  >
    <div class="container-page flex h-16 items-center justify-between">
      <a href="#top" class="font-display text-sm font-semibold text-white">
        Chaiwat Singkibut<span class="text-accent-400">.</span>
      </a>

      <nav class="hidden items-center gap-7 md:flex">
        <a
          v-for="link in links"
          :key="link.href"
          :href="link.href"
          class="text-sm text-slate-400 transition-colors hover:text-white"
        >
          {{ link.label }}
        </a>
      </nav>

      <div class="flex items-center gap-2">
        <a
          href="#contact"
          class="hidden rounded-lg border border-white/12 px-4 py-2 text-xs font-semibold text-white transition-colors hover:border-accent-500/40 sm:inline-flex"
        >
          ติดต่อ
        </a>

        <button
          type="button"
          class="grid h-9 w-9 place-items-center rounded-lg border border-white/10 text-slate-300 md:hidden"
          aria-label="เมนู"
          @click="menuOpen = !menuOpen"
        >
          <Icon :name="menuOpen ? 'mdi:close' : 'mdi:menu'" size="18" />
        </button>
      </div>
    </div>

    <Transition
      enter-active-class="transition duration-200 ease-out"
      enter-from-class="opacity-0 -translate-y-2"
      leave-active-class="transition duration-150 ease-in"
      leave-to-class="opacity-0 -translate-y-2"
    >
      <nav
        v-if="menuOpen"
        class="border-t border-white/8 bg-ink-900/95 px-5 py-3 backdrop-blur-lg md:hidden"
      >
        <a
          v-for="link in links"
          :key="link.href"
          :href="link.href"
          class="block py-2 text-sm text-slate-300"
          @click="menuOpen = false"
        >
          {{ link.label }}
        </a>
      </nav>
    </Transition>
  </header>
</template>
