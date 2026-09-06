<script setup lang="ts">
import { skillGroups } from '~/data/portfolio'
</script>

<template>
  <section id="skills" class="scroll-mt-20 py-20 sm:py-28">
    <div class="container-page">
      <SectionHeading
        v-reveal
        eyebrow="ทักษะ & เครื่องมือ"
        title="สิ่งที่ใช้ทำงาน"
        description="เชี่ยวชาญ Nuxt.js / Vue.js เป็นหลัก และหยิบเครื่องมือรอบข้างมาใช้ตามโจทย์ของแต่ละระบบ"
      />

      <div class="mt-12 grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
        <div
          v-for="(group, i) in skillGroups"
          :key="group.title"
          v-reveal="i * 60"
          class="card card-hover p-5"
        >
          <p class="flex items-center gap-2 text-sm font-semibold text-white">
            <Icon :name="group.icon" size="18" class="text-accent-400" />
            {{ group.title }}
          </p>
          <div class="mt-4 flex flex-wrap gap-1.5">
            <span v-for="item in group.items" :key="item" class="chip">{{ item }}</span>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
