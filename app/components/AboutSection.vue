<script setup lang="ts">
import { personal, education } from '~/data/portfolio'

const highlights = [
  {
    icon: 'mdi:rocket-launch-outline',
    title: 'พัฒนาตั้งแต่ศูนย์',
    body: 'ร่วมวางโครงสร้างโปรเจกต์ Nuxt ใหม่ตั้งแต่เริ่มต้น กำหนด pattern การทำงานร่วมกับทีม',
  },
  {
    icon: 'mdi:swap-horizontal',
    title: 'เชื่อมต่อระบบองค์กร',
    body: 'ทำงานกับ API หลายระดับ ทั้ง SAP, LINE LIFF, LiveKit และ workflow อนุมัติหลายขั้น',
  },
  {
    icon: 'mdi:wrench-outline',
    title: 'เข้าไปแก้ของเดิมได้',
    body: 'รับช่วงต่อโค้ดเดิม แก้ defect ช่วง UAT และรีดีไซน์ UI ของระบบที่รันอยู่แล้ว',
  },
]
</script>

<template>
  <section id="about" class="scroll-mt-20 py-20 sm:py-28">
    <div class="container-page">
      <SectionHeading
        v-reveal
        eyebrow="เกี่ยวกับผม"
        title="พัฒนา Frontend ให้ระบบธุรกิจที่ต้องใช้งานจริงทุกวัน"
        description="ผมทำงานกับระบบองค์กรเป็นหลัก ทั้งงานสร้างใหม่และงานดูแลต่อ ตั้งแต่ระบบขาย เชื่อม SAP, แชทรวมศูนย์, วิดีโอคอนเฟอเรนซ์ผสาน AI ไปจนถึง Backoffice หลายตัว"
      />

      <div class="mt-12 grid gap-6 lg:grid-cols-[1.1fr_0.9fr]">
        <div class="min-w-0 space-y-6">
          <div v-reveal class="grid gap-4 sm:grid-cols-3">
            <div v-for="h in highlights" :key="h.title" class="card card-hover p-4">
              <Icon :name="h.icon" size="22" class="text-accent-400" />
              <p class="mt-3 text-sm font-semibold text-white">{{ h.title }}</p>
              <p class="mt-1.5 text-xs leading-relaxed text-slate-400">{{ h.body }}</p>
            </div>
          </div>

          <div v-reveal="80" class="card p-5">
            <p class="section-eyebrow"><Icon name="mdi:school-outline" size="14" /> การศึกษา</p>
            <div v-for="edu in education" :key="edu.school" class="mt-3">
              <p class="text-sm font-semibold text-white">{{ edu.school }}</p>
              <p class="mt-1 text-xs text-slate-400">{{ edu.degree }} · {{ edu.field }}</p>
              <p class="mt-1 font-mono text-[11px] text-slate-600">{{ edu.startDate }} – {{ edu.endDate }}</p>
            </div>
          </div>

          <dl v-reveal="120" class="card grid grid-cols-1 gap-4 p-5 sm:grid-cols-2">
            <div class="flex items-start gap-3">
              <Icon name="mdi:map-marker-outline" size="18" class="mt-0.5 shrink-0 text-accent-400" />
              <div class="min-w-0">
                <dt class="text-[11px] uppercase tracking-wide text-slate-600">ที่อยู่</dt>
                <dd class="text-xs leading-relaxed text-slate-300">{{ personal.location }}</dd>
              </div>
            </div>
            <div class="flex items-start gap-3">
              <Icon name="mdi:email-outline" size="18" class="mt-0.5 shrink-0 text-accent-400" />
              <div class="min-w-0">
                <dt class="text-[11px] uppercase tracking-wide text-slate-600">อีเมล</dt>
                <dd class="font-mono text-xs text-slate-300">
                  <a v-for="m in personal.email" :key="m" :href="`mailto:${m}`" class="block break-all hover:text-accent-400">{{ m }}</a>
                </dd>
              </div>
            </div>
          </dl>
        </div>

        <div v-reveal="60" class="min-w-0">
          <ContributionGraph />
          <p class="mt-3 px-1 text-[11px] leading-relaxed text-slate-600">
            * สรุปจากประวัติ commit ในรอบ 12 เดือนล่าสุด
          </p>
        </div>
      </div>
    </div>
  </section>
</template>
