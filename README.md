# portfolio-chaiwat

พอร์ตโฟลิโอส่วนตัวของ **ชัยวัฒน์ สิงคิบุตร (ฟิวส์)** — Frontend Developer
สร้างด้วย **Nuxt 4** + **Tailwind CSS v4**

## Stack

| ส่วน | เทคโนโลยี |
| --- | --- |
| Framework | Nuxt 4 (Vue 3, Nitro, Vite) |
| Styling | Tailwind CSS v4 (`@tailwindcss/vite`) |
| Fonts | `@nuxt/fonts` — IBM Plex Sans Thai / Space Grotesk / JetBrains Mono |
| Icons | `@nuxt/icon` + `@iconify-json/mdi` (bundle แบบ local) |
| Utils | `@vueuse/nuxt` |

## โครงสร้าง

```
app/
  app.vue                  หน้าเดียว ประกอบ section ทั้งหมด
  assets/css/main.css       Tailwind theme + utility คลาสส่วนกลาง
  data/portfolio.ts         โหลด/แปลงข้อมูลจาก profile.json + commit_heatmap.json
  plugins/reveal.ts         directive v-reveal (scroll-in animation + failsafe)
  components/
    AppHeader / AppFooter
    HeroSection / AboutSection / ExperienceSection
    SkillsSection / ProjectsSection / ProjectCard
    ContributionGraph       heatmap สไตล์ GitHub จากประวัติ commit
    ContactSection / SectionHeading
profile.json                แหล่งข้อมูลหลัก (ประวัติ + โปรเจกต์)
commit_heatmap.json         ข้อมูล commit รายวันสำหรับ heatmap
```

แก้ข้อมูลในพอร์ตได้ที่ `profile.json` — หน้าเว็บอ่านจากไฟล์นี้โดยตรง

## คำสั่ง

```bash
npm install
npm run dev        # http://localhost:3000
npm run build      # build โปรดักชัน (SSR)
npm run generate   # export เป็น static site
npm run preview
```
