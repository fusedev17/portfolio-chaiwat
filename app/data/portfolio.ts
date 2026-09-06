import profile from '~~/profile.json'
import commitHeatmap from '~~/commit_heatmap.json'

export interface ProjectItem {
  name: string
  startDate: string
  endDate: string
  type: string
  description: string
  role: string
  stack: string[]
}

export const personal = profile.personal
export const experience = profile.experience
export const education = profile.education
export const projects = profile.projects as ProjectItem[]

/** ลิงก์โซเชียล / ช่องทางติดต่อ */
export const socials = [
  { label: 'GitHub', icon: 'mdi:github', href: 'https://github.com/fusedev17' },
  { label: 'Email', icon: 'mdi:email-outline', href: `mailto:${personal.email[1]}` },
  { label: 'โทรศัพท์', icon: 'mdi:phone-outline', href: `tel:${personal.phone}` },
]

/** สรุปทักษะแยกหมวด — เรียงจากที่ใช้บ่อยที่สุด */
export const skillGroups = [
  {
    title: 'Core',
    icon: 'mdi:hexagon-multiple-outline',
    items: ['Nuxt.js', 'Vue.js', 'Nuxt.js 4', 'Vue 3', 'JavaScript', 'TypeScript', 'HTML5', 'CSS3'],
  },
  {
    title: 'State & Data',
    icon: 'mdi:database-outline',
    items: ['Pinia', 'pinia-plugin-persistedstate', 'Vue Router', 'Axios', 'REST API', 'Socket.IO', 'JWT'],
  },
  {
    title: 'Styling & UI',
    icon: 'mdi:palette-outline',
    items: ['Tailwind CSS', 'daisyUI', 'Vuetify', 'Bootstrap Vue', 'Element Plus', 'Sass', 'VueUse Motion'],
  },
  {
    title: 'Tooling & Platform',
    icon: 'mdi:tools',
    items: ['Vite', 'Git', 'Docker', 'Nuxt Image', 'Chart.js', 'dayjs / date-fns', 'SweetAlert2'],
  },
  {
    title: 'Integrations',
    icon: 'mdi:transit-connection-variant',
    items: ['SAP', 'LINE LIFF', 'LiveKit', 'Google Maps', 'PDFMake / jsPDF', 'xlsx'],
  },
  {
    title: 'Also worked with',
    icon: 'mdi:dots-horizontal',
    items: ['Next.js', 'React', 'Redux Toolkit', 'Ant Design', 'NestJS', 'Prisma', 'Python'],
  },
]

/** ตัวเลขสรุปหน้าแรก */
export const stats = [
  { value: `${personal.yearsOfExperience}+`, label: 'ปีประสบการณ์' },
  { value: `${projects.length}`, label: 'โปรเจกต์ที่ร่วมพัฒนา' },
  { value: '15+', label: 'ระบบองค์กร / Backoffice' },
  { value: '6+', label: 'ระบบเชื่อมต่อ SAP / LINE' },
]

// ---------- Commit heatmap ----------

export interface HeatCell {
  date: string
  count: number
  level: 0 | 1 | 2 | 3 | 4
}

function levelFor(count: number): HeatCell['level'] {
  if (count <= 0) return 0
  if (count <= 1) return 1
  if (count <= 3) return 2
  if (count <= 5) return 3
  return 4
}

/**
 * สร้างตารางแบบ GitHub contribution graph สำหรับ 12 เดือนล่าสุด
 * คืนค่าเป็น array ของสัปดาห์ (คอลัมน์) โดยแต่ละสัปดาห์มี 7 วัน (อา.-ส.)
 */
export function buildHeatmap(now = new Date()) {
  const map = commitHeatmap as Record<string, number>

  const end = new Date(now)
  end.setHours(0, 0, 0, 0)
  // ถอยไปให้ถึงวันเสาร์ที่ปิดสัปดาห์
  end.setDate(end.getDate() + (6 - end.getDay()))

  const start = new Date(end)
  start.setDate(start.getDate() - 52 * 7 - 6)

  const weeks: HeatCell[][] = []
  let total = 0
  const cursor = new Date(start)

  while (cursor <= end) {
    const week: HeatCell[] = []
    for (let d = 0; d < 7; d++) {
      const key = cursor.toISOString().slice(0, 10)
      const count = map[key] ?? 0
      total += count
      week.push({ date: key, count, level: levelFor(count) })
      cursor.setDate(cursor.getDate() + 1)
    }
    weeks.push(week)
  }

  const activeDays = Object.keys(map).filter((k) => {
    const t = new Date(k).getTime()
    return t >= start.getTime() && t <= end.getTime()
  }).length

  return { weeks, total, activeDays }
}
