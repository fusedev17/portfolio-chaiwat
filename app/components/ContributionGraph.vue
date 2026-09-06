<script setup lang="ts">
import { buildHeatmap } from '~/data/portfolio'

const { weeks, total, activeDays } = buildHeatmap()

const levelClass: Record<number, string> = {
  0: 'bg-white/5',
  1: 'bg-accent-600/30',
  2: 'bg-accent-600/55',
  3: 'bg-accent-500/80',
  4: 'bg-accent-400',
}

const monthLabels = computed(() => {
  const names = ['ม.ค.', 'ก.พ.', 'มี.ค.', 'เม.ย.', 'พ.ค.', 'มิ.ย.', 'ก.ค.', 'ส.ค.', 'ก.ย.', 'ต.ค.', 'พ.ย.', 'ธ.ค.']
  const out: { label: string; index: number }[] = []
  let last = -1
  weeks.forEach((week, i) => {
    const first = week[0]
    if (!first) return
    const m = new Date(first.date).getMonth()
    if (m !== last && new Date(first.date).getDate() <= 7) {
      out.push({ label: names[m]!, index: i })
      last = m
    }
  })
  return out
})

function tooltip(count: number, date: string) {
  const d = new Date(date)
  const s = d.toLocaleDateString('th-TH', { day: 'numeric', month: 'short', year: 'numeric' })
  return count > 0 ? `${count} commit · ${s}` : `ไม่มี commit · ${s}`
}
</script>

<template>
  <div class="card p-5">
    <div class="flex flex-wrap items-baseline justify-between gap-2">
      <p class="text-sm font-medium text-white">กิจกรรมการเขียนโค้ด</p>
      <p class="font-mono text-xs text-slate-500">
        {{ total.toLocaleString() }} commits · {{ activeDays }} วันในรอบปี
      </p>
    </div>

    <div class="mt-4 overflow-x-auto pb-1">
      <div class="min-w-[640px]">
        <div class="relative mb-1 ml-7 h-4">
          <span
            v-for="m in monthLabels"
            :key="m.index"
            class="absolute font-mono text-[10px] text-slate-500"
            :style="{ left: `${m.index * 14}px` }"
          >
            {{ m.label }}
          </span>
        </div>

        <div class="flex gap-[3px]">
          <div class="mr-1 flex flex-col gap-[3px] pt-[2px] font-mono text-[10px] text-slate-500">
            <span class="h-[11px]" />
            <span class="h-[11px] leading-[11px]">จ.</span>
            <span class="h-[11px]" />
            <span class="h-[11px] leading-[11px]">พ.</span>
            <span class="h-[11px]" />
            <span class="h-[11px] leading-[11px]">ศ.</span>
            <span class="h-[11px]" />
          </div>

          <div
            v-for="(week, wi) in weeks"
            :key="wi"
            class="flex flex-col gap-[3px]"
          >
            <span
              v-for="cell in week"
              :key="cell.date"
              class="h-[11px] w-[11px] rounded-[2px]"
              :class="levelClass[cell.level]"
              :title="tooltip(cell.count, cell.date)"
            />
          </div>
        </div>
      </div>
    </div>

    <div class="mt-4 flex items-center justify-end gap-1.5 font-mono text-[10px] text-slate-500">
      <span>น้อย</span>
      <span v-for="l in [0, 1, 2, 3, 4]" :key="l" class="h-[11px] w-[11px] rounded-[2px]" :class="levelClass[l]" />
      <span>มาก</span>
    </div>
  </div>
</template>
