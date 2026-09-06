<script setup lang="ts">
import { projects } from '~/data/portfolio'

const filters = ['ทั้งหมด', 'Nuxt.js', 'Vue.js', 'Tailwind CSS', 'Pinia', 'TypeScript', 'Vuetify', 'Next.js']
const active = ref('ทั้งหมด')

const filtered = computed(() => {
  if (active.value === 'ทั้งหมด') return projects
  return projects.filter((p) =>
    p.stack.some((s) => s.toLowerCase().includes(active.value.toLowerCase())),
  )
})
</script>

<template>
  <section id="projects" class="scroll-mt-20 py-20 sm:py-28">
    <div class="container-page">
      <SectionHeading
        v-reveal
        eyebrow="ผลงาน"
        :title="`${projects.length} โปรเจกต์ที่ได้ลงมือทำ`"
        description="ส่วนใหญ่เป็นระบบองค์กรที่มีผู้ใช้งานจริง — คัดมาแสดงพร้อมบทบาทที่ผมรับผิดชอบและเทคโนโลยีที่ใช้"
      />

      <div v-reveal="60" class="mt-8 flex flex-wrap gap-2">
        <button
          v-for="f in filters"
          :key="f"
          type="button"
          class="rounded-full border px-3.5 py-1.5 text-xs font-medium transition-colors"
          :class="
            active === f
              ? 'border-accent-500 bg-accent-500/10 text-accent-300'
              : 'border-white/10 text-slate-400 hover:border-white/25 hover:text-white'
          "
          @click="active = f"
        >
          {{ f }}
        </button>
      </div>

      <div class="mt-8 grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
        <ProjectCard
          v-for="(project, i) in filtered"
          :key="project.name"
          :project="project"
          :index="i"
        />
      </div>

      <p v-if="!filtered.length" class="mt-8 text-sm text-slate-500">ไม่พบโปรเจกต์ที่ใช้ {{ active }}</p>
    </div>
  </section>
</template>
