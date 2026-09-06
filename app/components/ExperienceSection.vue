<script setup lang="ts">
import { experience, projects } from '~/data/portfolio'

// นับปีที่มีผลงานเพื่อแสดง timeline ย่อ
const years = computed(() => {
  const set = new Set<string>()
  for (const p of projects) {
    for (const y of `${p.startDate}-${p.endDate}`.split('-')) {
      const n = Number(y)
      if (n >= 2000) set.add(String(n))
    }
  }
  return [...set].sort((a, b) => Number(b) - Number(a))
})
</script>

<template>
  <section id="experience" class="scroll-mt-20 py-20 sm:py-28">
    <div class="container-page">
      <SectionHeading
        v-reveal
        eyebrow="ประสบการณ์ทำงาน"
        title="เส้นทางการทำงาน"
        description="เริ่มงานสายพัฒนาเว็บตั้งแต่ปี 2565 กับทีมที่รับพัฒนาระบบให้ลูกค้าองค์กรหลากหลายอุตสาหกรรม"
      />

      <div class="mt-12 space-y-4">
        <div
          v-for="(job, i) in experience"
          :key="job.company"
          v-reveal="i * 80"
          class="card p-6"
        >
          <div class="flex flex-wrap items-start justify-between gap-3">
            <div>
              <h3 class="text-lg font-semibold text-white">{{ job.position }}</h3>
              <p class="mt-1 text-sm text-accent-400">{{ job.company }}</p>
            </div>
            <span class="chip">{{ job.startDate }} — {{ job.endDate }}</span>
          </div>
          <p class="mt-4 text-sm leading-relaxed text-slate-400">
            รับผิดชอบงาน Frontend เต็มรูปแบบ ทั้งพัฒนา UI จากดีไซน์ เชื่อมต่อ API วางระบบ state ด้วย Pinia
            และดูแลคุณภาพจนถึงขั้น UAT / ส่งมอบ ทำงานร่วมกับทีม Frontend, Backend และ AI ในหลายโปรเจกต์พร้อมกัน
          </p>

          <div class="mt-5 border-t border-white/8 pt-4">
            <p class="mb-3 font-mono text-[11px] uppercase tracking-wider text-slate-600">ปีที่มีผลงาน</p>
            <div class="flex flex-wrap gap-1.5">
              <span v-for="y in years" :key="y" class="chip">{{ y }}</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
