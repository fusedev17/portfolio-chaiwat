<script setup lang="ts">
import { personal, stats, socials } from '~/data/portfolio'

const roles = ['Nuxt.js / Vue.js', 'ระบบองค์กร & Backoffice', 'SAP / LINE Integration', 'UI ที่ใช้งานได้จริง']
const roleIndex = ref(0)
let timer: ReturnType<typeof setInterval>
onMounted(() => {
  timer = setInterval(() => {
    roleIndex.value = (roleIndex.value + 1) % roles.length
  }, 2600)
})
onUnmounted(() => clearInterval(timer))
</script>

<template>
  <section id="top" class="relative overflow-hidden pt-32 pb-20 sm:pt-40 sm:pb-28">
    <div class="container-page">
      <p v-reveal class="section-eyebrow flex-wrap normal-case tracking-normal">
        <span class="relative flex h-2 w-2 shrink-0">
          <span class="absolute inline-flex h-full w-full animate-ping rounded-full bg-lime-glow/70" />
          <span class="relative inline-flex h-2 w-2 rounded-full bg-lime-glow" />
        </span>
        <span>Portfolio</span>
        <span class="text-slate-600">·</span>
        <span class="text-slate-500">ผลงาน ประสบการณ์ ความสามารถ</span>
      </p>

      <h1 v-reveal="80" class="mt-6 text-4xl font-bold leading-[1.1] sm:text-6xl">
        {{ personal.name }}
        <span class="mt-2 block text-slate-500">“{{ personal.nickname }}”</span>
      </h1>

      <div v-reveal="140" class="mt-6 flex items-center gap-3 font-mono text-sm text-accent-400 sm:text-base">
        <Icon name="mdi:chevron-right" size="18" />
        <span class="relative inline-block h-6 overflow-hidden">
          <Transition
            enter-active-class="transition duration-500 ease-out"
            enter-from-class="opacity-0 translate-y-4"
            leave-active-class="transition duration-500 ease-in absolute inset-0"
            leave-to-class="opacity-0 -translate-y-4"
            mode="out-in"
          >
            <span :key="roleIndex" class="block">{{ roles[roleIndex] }}</span>
          </Transition>
        </span>
      </div>

      <p v-reveal="200" class="mt-6 max-w-xl text-sm leading-relaxed text-slate-400 sm:text-base">
        Frontend Developer ประสบการณ์ {{ personal.yearsOfExperience }} ปี
        โฟกัสงานพัฒนา Frontend Developer ของระบบต่างๆ ด้วย Nuxt.js, Vue.js และ Next.js
        ตั้งแต่วางโครงสร้างโปรเจกต์ เชื่อมต่อ API ไปจนถึงส่งมอบระบบที่ใช้งานจริงในองค์กร
      </p>

      <div v-reveal="260" class="mt-8 flex flex-wrap items-center gap-3">
        <a
          href="#projects"
          class="inline-flex items-center gap-2 rounded-lg bg-accent-500 px-5 py-2.5 text-sm font-semibold text-ink-950 transition-colors hover:bg-accent-400"
        >
          ดูผลงาน
          <Icon name="mdi:arrow-down" size="16" />
        </a>
        <a
          href="#contact"
          class="inline-flex items-center gap-2 rounded-lg border border-white/12 px-5 py-2.5 text-sm font-semibold text-white transition-colors hover:border-accent-500/40"
        >
          ติดต่อ
        </a>
        <div class="ml-1 flex items-center gap-1">
          <a
            v-for="s in socials"
            :key="s.label"
            :href="s.href"
            target="_blank"
            rel="noopener"
            :aria-label="s.label"
            class="grid h-9 w-9 place-items-center rounded-lg text-slate-400 transition-colors hover:bg-white/5 hover:text-white"
          >
            <Icon :name="s.icon" size="18" />
          </a>
        </div>
      </div>

      <dl v-reveal="320" class="mt-14 grid grid-cols-2 gap-px overflow-hidden rounded-2xl border border-white/8 bg-white/8 sm:grid-cols-4">
        <div v-for="stat in stats" :key="stat.label" class="bg-ink-900 p-5">
          <dt class="font-display text-2xl font-semibold text-white sm:text-3xl">{{ stat.value }}</dt>
          <dd class="mt-1 text-xs text-slate-500">{{ stat.label }}</dd>
        </div>
      </dl>
    </div>
  </section>
</template>
