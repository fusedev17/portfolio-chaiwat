import tailwindcss from '@tailwindcss/vite'

// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2025-07-15',
  devtools: { enabled: true },

  modules: [
    '@nuxt/icon',
    '@nuxt/fonts',
    '@vueuse/nuxt',
  ],

  css: ['~/assets/css/main.css'],

  // เว็บเป็น static ล้วน (ข้อมูลมาจาก JSON ตอน build) — prerender ทุกหน้าให้เสิร์ฟเป็นไฟล์นิ่ง
  nitro: {
    prerender: {
      crawlLinks: true,
      routes: ['/', '/200.html', '/404.html'],
    },
  },
  routeRules: {
    '/**': { prerender: true },
  },

  vite: {
    plugins: [tailwindcss()],
  },

  fonts: {
    families: [
      { name: 'IBM Plex Sans Thai', provider: 'google', weights: [300, 400, 500, 600, 700] },
      { name: 'Space Grotesk', provider: 'google', weights: [400, 500, 600, 700] },
      { name: 'JetBrains Mono', provider: 'google', weights: [400, 500] },
    ],
  },

  app: {
    head: {
      htmlAttrs: { lang: 'th' },
      title: 'ชัยวัฒน์ สิงคิบุตร — Frontend Developer',
      meta: [
        { charset: 'utf-8' },
        { name: 'viewport', content: 'width=device-width, initial-scale=1' },
        {
          name: 'description',
          content:
            'พอร์ตโฟลิโอของ ชัยวัฒน์ สิงคิบุตร (ฟิวส์) — Frontend Developer ประสบการณ์ 4 ปี เชี่ยวชาญ Nuxt.js, Vue.js และการพัฒนาระบบองค์กร',
        },
        { property: 'og:title', content: 'ชัยวัฒน์ สิงคิบุตร — Frontend Developer' },
        {
          property: 'og:description',
          content: 'Frontend Developer ประสบการณ์ 4 ปี — Nuxt.js / Vue.js / TypeScript',
        },
        { property: 'og:type', content: 'website' },
        { name: 'theme-color', content: '#0a0a0f' },
      ],
    },
  },
})
