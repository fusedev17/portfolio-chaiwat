// v-reveal — เพิ่มคลาส .is-visible เมื่อ element เลื่อนเข้ามาในจอ
export default defineNuxtPlugin((nuxtApp) => {
  let observer: IntersectionObserver | null = null

  if (import.meta.client && typeof IntersectionObserver !== 'undefined') {
    observer = new IntersectionObserver(
      (entries) => {
        for (const entry of entries) {
          if (entry.isIntersecting) {
            entry.target.classList.add('is-visible')
            observer!.unobserve(entry.target)
          }
        }
      },
      { threshold: 0.12, rootMargin: '0px 0px -8% 0px' },
    )
  }

  const tracked = new Set<HTMLElement>()

  // failsafe: ถ้า observer ไม่ทำงาน (เช่น bot, prerender, จอสูง) ให้โชว์ทุกอย่างหลัง 2.5 วิ
  if (import.meta.client) {
    window.setTimeout(() => {
      tracked.forEach((el) => el.classList.add('is-visible'))
    }, 2500)
  }

  nuxtApp.vueApp.directive('reveal', {
    getSSRProps() {
      return {}
    },
    mounted(el: HTMLElement, binding) {
      el.classList.add('reveal')
      if (binding.value != null) {
        el.style.animationDelay = `${binding.value}ms`
      }
      if (observer) {
        tracked.add(el)
        observer.observe(el)
      } else {
        el.classList.add('is-visible')
      }
    },
    unmounted(el: HTMLElement) {
      tracked.delete(el)
      if (observer) observer.unobserve(el)
    },
  })
})
