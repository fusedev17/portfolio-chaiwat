<script setup lang="ts">
import { personal } from '~/data/portfolio'

useHead({
  script: [
    {
      type: 'application/ld+json',
      innerHTML: JSON.stringify({
        '@context': 'https://schema.org',
        '@type': 'Person',
        name: personal.name,
        alternateName: personal.nickname,
        jobTitle: personal.title,
        email: personal.email[0],
        address: personal.location,
        knowsAbout: ['Nuxt.js', 'Vue.js', 'Frontend Development', 'TypeScript'],
      }),
    },
  ],
})

const showTop = ref(false)
function onScroll() {
  showTop.value = window.scrollY > 800
}
onMounted(() => {
  onScroll()
  window.addEventListener('scroll', onScroll, { passive: true })
})
onUnmounted(() => window.removeEventListener('scroll', onScroll))
</script>

<template>
  <div class="min-h-screen">
    <AppHeader />

    <main>
      <HeroSection />
      <AboutSection />
      <ExperienceSection />
      <SkillsSection />
      <ProjectsSection />
      <ContactSection />
    </main>

    <AppFooter />

    <Transition
      enter-active-class="transition duration-200"
      enter-from-class="opacity-0 translate-y-2"
      leave-active-class="transition duration-150"
      leave-to-class="opacity-0 translate-y-2"
    >
      <a
        v-if="showTop"
        href="#top"
        aria-label="กลับขึ้นบน"
        class="fixed bottom-6 right-6 z-40 grid h-11 w-11 place-items-center rounded-full border border-white/12 bg-ink-800/90 text-slate-200 backdrop-blur transition-colors hover:border-accent-500/50 hover:text-white"
      >
        <Icon name="mdi:arrow-up" size="18" />
      </a>
    </Transition>
  </div>
</template>
