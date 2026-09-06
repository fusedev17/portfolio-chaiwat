<script setup lang="ts">
import { personal, socials } from '~/data/portfolio'

const copied = ref(false)
async function copyEmail() {
  try {
    await navigator.clipboard.writeText(personal.email[1] as string)
    copied.value = true
    setTimeout(() => (copied.value = false), 1800)
  } catch {
    /* ignore */
  }
}
</script>

<template>
  <section id="contact" class="scroll-mt-20 py-20 sm:py-28">
    <div class="container-page">
      <div v-reveal class="card overflow-hidden">
        <div class="grid gap-8 p-8 sm:p-12 lg:grid-cols-[1.2fr_1fr]">
          <div>
            <span class="section-eyebrow"><span class="h-px w-6 bg-accent-400/60" /> ติดต่อ</span>
            <h2 class="mt-3 text-2xl font-semibold sm:text-3xl">ช่องทางการติดต่อ</h2>
            

            <div class="mt-6 flex flex-wrap gap-3">
              <button
                type="button"
                class="inline-flex items-center gap-2 rounded-lg bg-accent-500 px-5 py-2.5 text-sm font-semibold text-ink-950 transition-colors hover:bg-accent-400"
                @click="copyEmail"
              >
                <Icon :name="copied ? 'mdi:check' : 'mdi:content-copy'" size="16" />
                {{ copied ? 'คัดลอกแล้ว' : 'คัดลอกอีเมล' }}
              </button>
              <a
                :href="`tel:${personal.phone}`"
                class="inline-flex items-center gap-2 rounded-lg border border-white/12 px-5 py-2.5 text-sm font-semibold text-white transition-colors hover:border-accent-500/40"
              >
                <Icon name="mdi:phone-outline" size="16" />
                {{ personal.phone }}
              </a>
            </div>
          </div>

          <ul class="flex flex-col justify-center gap-2 border-white/8 lg:border-l lg:pl-8">
            <li v-for="s in socials" :key="s.label">
              <a
                :href="s.href"
                target="_blank"
                rel="noopener"
                class="flex items-center gap-3 rounded-lg px-3 py-2.5 text-sm text-slate-300 transition-colors hover:bg-white/5 hover:text-white"
              >
                <Icon :name="s.icon" size="18" class="text-accent-400" />
                {{ s.label }}
                <Icon name="mdi:arrow-top-right" size="14" class="ml-auto text-slate-600" />
              </a>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </section>
</template>
