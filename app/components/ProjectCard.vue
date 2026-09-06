<script setup lang="ts">
import type { ProjectItem } from '~/data/portfolio'

const props = defineProps<{ project: ProjectItem; index: number }>()

const open = ref(false)
const period = computed(() =>
  props.project.startDate === props.project.endDate
    ? props.project.startDate
    : `${props.project.startDate}–${props.project.endDate}`,
)
const visibleStack = computed(() => (open.value ? props.project.stack : props.project.stack.slice(0, 6)))
const hiddenCount = computed(() => props.project.stack.length - 6)
</script>

<template>
  <article
    v-reveal="(index % 3) * 70"
    class="card card-hover group flex flex-col p-5"
  >
    <div class="flex items-start justify-between gap-3">
      <span class="chip">{{ period }}</span>
      <Icon
        name="mdi:folder-outline"
        size="20"
        class="text-slate-600 transition-colors group-hover:text-accent-400"
      />
    </div>

    <h3 class="mt-3 text-base font-semibold leading-snug text-white">{{ project.name }}</h3>
    <p class="mt-1.5 text-xs font-medium text-accent-400/90">{{ project.type }}</p>

    <p
      class="mt-3 text-xs leading-relaxed text-slate-400"
      :class="open ? '' : 'line-clamp-3'"
    >
      {{ project.description }}
    </p>

    <div v-if="open" class="mt-3 rounded-lg border border-white/8 bg-white/[0.02] p-3">
      <p class="font-mono text-[10px] uppercase tracking-wider text-slate-600">บทบาทของ</p>
      <p class="mt-1.5 text-xs leading-relaxed text-slate-300">{{ project.role }}</p>
    </div>

    <button
      type="button"
      class="mt-3 inline-flex w-fit items-center gap-1 text-[11px] font-medium text-accent-400 hover:text-accent-300"
      @click="open = !open"
    >
      {{ open ? 'ย่อ' : 'ดูรายละเอียด & บทบาท' }}
      <Icon :name="open ? 'mdi:chevron-up' : 'mdi:chevron-down'" size="14" />
    </button>

    <div class="mt-4 flex flex-wrap gap-1.5 border-t border-white/8 pt-4">
      <span v-for="tech in visibleStack" :key="tech" class="chip">{{ tech }}</span>
      <span v-if="!open && hiddenCount > 0" class="chip text-slate-500">+{{ hiddenCount }}</span>
    </div>
  </article>
</template>
