<template>
  <!-- [frame heading start] -->
  <img class='absolute -z-10 w-full' :src=frameHeading alt='Frame heading' />
  <!-- [frame heading end] -->

  <!-- [header start] -->
  <header class="flex flex-wrap sm:justify-start sm:flex-nowrap z-[999] w-full bg-white text-sm py-[20px]">
    <nav class="max-w-[90em] 2xl:max-w-[100em] w-full mx-auto px-4 sm:flex sm:items-center sm:justify-between" aria-label="Global">
      <div class="flex items-center justify-between">
        <a class="flex-none" href="#home">
          <img class='2xl:w-10 h-auto' src="emblem.png" alt="Brand">
        </a>
        <div class="sm:hidden">
          <button type="button"
            class="hs-collapse-toggle p-2 inline-flex justify-center items-center gap-2 rounded-md border font-medium bg-white text-gray-700 shadow-sm align-middle hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-offset-white focus:ring-primary-600 transition-all text-sm"
            data-hs-collapse="#navigation" aria-controls="navigation" aria-label="Toggle navigation">
            <svg class="hs-collapse-open:hidden w-4 h-4" width="16" height="16" fill="currentColor" viewBox="0 0 16 16">
              <path fill-rule="evenodd"
                d="M2.5 12a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5zm0-4a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5zm0-4a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5z" />
            </svg>
            <svg class="hs-collapse-open:block hidden w-4 h-4" width="16" height="16" fill="currentColor" viewBox="0 0 16 16">
              <path
                d="M4.646 4.646a.5.5 0 0 1 .708 0L8 7.293l2.646-2.647a.5.5 0 0 1 .708.708L8.707 8l2.647 2.646a.5.5 0 0 1-.708.708L8 8.707l-2.646 2.647a.5.5 0 0 1-.708-.708L7.293 8 4.646 5.354a.5.5 0 0 1 0-.708z" />
            </svg>
          </button>
        </div>
      </div>
      <div id="navigation" class="hs-collapse hidden overflow-hidden transition-all duration-300 basis-full grow sm:block">
        <div data-hs-scrollspy="#scrollspy"
          class="flex flex-col 2xl:text-base 2xl:font-medium font-normal [--scrollspy-offset:0] text-[22px] gap-5 mt-5 sm:flex-row sm:items-center sm:justify-end sm:mt-0 sm:pl-5">
          <a class="text-primary hs-scrollspy-active:border-b-[2px] leading-7 border-secondary" :href="`#${l.path}`" :aria-current="`${l.path}`" v-for="l in navs"
            :key="l.path">
            {{ l.label }}
          </a>
        </div>
      </div>
    </nav>
  </header>
  <!-- [header end] -->

  <!-- [main start] -->
  <main id='scrollspy' role='main'>

    <!-- banner start -->
    <section class="py-20 2xl:h-[calc(100vh-88px)] 2xl:-z-0 2xl:py-0 2xl:flex 2xl:items-center 2xl:justify-center" id='home' role="banner">

      <!-- hero start -->
      <div class="2xl:max-w-[90em] max-w-[82em] w-full mx-auto px-4 sm:px-6 lg:px-8">

        <!-- grid start -->
        <div class="flex lg:gap-x-8 xl:gap-x-12 flex-wrap lg:flex-nowrap place-items-center justify-between items-center">

          <!-- col start -->
          <div class="lg:basis-2/3">
            <div class='space-y-[25px]'>
              <p class="mt-3 text-lg font-semibold text-[15.59] text-blue-600 dark:text-gray-400">Improve your worklife</p>
              <h1 class="block text-3xl leading-[60px] font-bold text-gray-800 text-[50.68px] sm:text-4xl md:text-5xl lg:text-6xl dark:text-white">Remote work
                made easy with
                better tools.</h1>
            </div>
            <div class="mt-3 lg:mt-6 flex flex-col items-center gap-2 sm:flex-row sm:gap-3">
              <div class="w-full sm:w-auto flex gap-16">
                <div class='flex items-center gap-4' v-for='c in checks' :key='c.label'>
                  <img :src="checkIcon" alt='Check' />
                  <p class='font-semibold text-lg'>{{ c.label }}</p>
                </div>
              </div>
            </div>
            <div class="mt-6 lg:mt-12">
              <p class='text-[#060F51] text-2xl'>Lorem ipsum dolor sit amet consectetur. At elementum enim et aliquam donec dis accumsan. Integer feugiat
                convallis nisl odio cursus aliquet metus
                lobortis eget.</p>
            </div>
            <div class="mt-6 lg:mt-12">
              <a class='bg-primary text-white rounded-full w-full lg:w-max py-3 font-semibold px-14 text-center' href='#'>Заказать</a>
            </div>
          </div>
          <!-- col end -->

          <!-- col start -->
          <div class="lg:basis-1/3 mt-10 lg:mt-0">
            <img class='w-full h-auto lg:w-auto' :src=heading alt="Heading" />
          </div>
          <!-- col end -->

        </div>
        <!-- grid end -->

      </div>
      <!-- hero end -->

    </section>
    <!-- banner end -->

    <!-- about start -->
    <section class="bg-[url('../../assets/images/team.png')] 2xl:bg-bottom min-h-[820px] bg-no-repeat bg-center 2xl:bg-cover mb-20" id='about'>
      <div class="2xl:max-w-[90em] max-w-[82em] px-4 py-10 sm:px-6 lg:px-8 lg:py-14 mx-auto">
        <div class="max-w-2xl mx-auto text-center mb-10 lg:mb-14">
          <h2 class="2xl:text-3xl font-bold text-6xl md:leading-tight dark:text-white">Our company</h2>
          <p class="mt-4 text-base text-gray-600 mx-auto max-w-md">Clarity gives you the blocks & components you need to create a truly professional website,
            landing page or admin panel for your SaaS.</p>
        </div>
      </div>
      <div>
        <div
          class='absolute shadow-md rounded-xl px-4 py-2 z-30 text-center 2xl:left-[890px] left-[200px] 2xl:top-[1240px] top-[1500px] bg-[rgba(255, 255, 255, 0.85)] backdrop-blur-md rotate-[2.18deg]'>
          <p class='text-[#090914] font-semibold text-[14px]'>Jenny Wilson</p>
          <p class='text-gray-600 text-[12px]'>Co-Founder, CEO</p>
        </div>
        <div class="inline-block absolute rotate-[3.82deg] z-40 overflow-hidden 2xl:left-[940px] left-[260px] top-[1555px] 2xl:top-[1295px]">
          <div class="h-[17px] w-[32px] origin-top-left -rotate-45 drop-shadow-md transform rounded-lg bg-white"></div>
        </div>
      </div>
    </section>
    <!-- about end -->

    <!-- portofilo start -->
    <section class="z-10 relative bg-[url('../../assets/images/portfolio.png')] 2xl:h-screen bg-center bg-no-repeat bg-cover" id='projects'>
      <div class="2xl:max-w-[90em] max-w-[82em] w-full mx-auto px-4 sm:px-6 lg:px-8">
        <div class='flex flex-col py-[160px] pb-[320px] max-w-2xl'>
          <div class='space-y-[60px]'>
            <div class='space-y-[30px]'>
              <h2 class='text-white font-bold text-5xl'>Portfolio</h2>
              <p class='text-[24px] text-white'>Lorem ipsum dolor sit amet, consectetur adipiscing elit. In nunc nisl eu consectetur. Mi massa elementum odio eu
                viverra amet.</p>
            </div>
            <div class='flex items-center gap-[30px]'>
              <a class='text-black font-semibold py-3 px-6 rounded-md text-center block text-sm bg-white'>Show more</a>
              <a class='2xl:text-white font-semibold py-3 px-6 text-center block text-sm text-white'>Open galery</a>
            </div>
          </div>
        </div>
      </div>
    </section>
    <!-- portfolio end -->

    <!-- services start -->
    <section class='relative -top-[140px] z-0' id='services'>
      <div class='w-full bg-[#F9F5FF]'>
        <div class='max-w-md mx-auto text-center space-y-4 py-32'>
          <h2 class='text-[#42307D] text-5xl font-semibold'>Service</h2>
          <p class='text-[#6941C6] text-lg'>All services what we do</p>
        </div>
      </div>
      <div class="bg-[url('../../assets/images/services.png')] relative -top-[30px] bg-cover bg-center bg-no-repeat h-[420px]">
        <div class="2xl:max-w-[90em] max-w-[82em] w-full mx-auto px-4 sm:px-6 lg:px-8 py-10">
          <div class='grid lg:grid-cols-3 grid-cols-1 gap-[32px]'>
            <div class="flex flex-col bg-white border border-[#EAECF0] rounded-xl shadow-lg" v-for='s in services' :key='s.label'>
              <div class="p-[32px] 2xl:p-10">
                <div class='flex flex-col items-center'>
                  <img class='mb-[20px]' :src='s.icon' alt='Icon' />
                  <h3 class="text-lg mb-[8px] font-semibold text-[#6941C6]">
                    {{ s.label }}
                  </h3>
                  <p class="text-gray-600">
                    {{ s.sublabel }}
                  </p>
                </div>
                <div class='mt-[32px] flex flex-col gap-[16px]'>
                  <div class='flex items-center gap-[12px]' v-for='i in s.items' :key='i.label'>
                    <img :src='checkIconPrimary' alt='Icon' />
                    <p class='text-gray-600 text-base'>{{ i.label }}</p>
                  </div>
                </div>
              </div>
              <div class="bg-gray-100 border-t rounded-b-xl p-[32px]">
                <a class='block w-full bg-[#7F56D9] text-white text-center py-[12px] rounded-md text-lg'>Заказать</a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
    <!-- services end -->

    <!-- guaranties start -->
    <section class='py-20' id='why'>
      <div class="2xl:max-w-[90em] max-w-[82em] px-4 py-10 sm:px-6 lg:px-8 lg:py-14 mx-auto">
        <div class="max-w-2xl mx-auto text-center mb-10 lg:mb-14">
          <h2 class="2xl:text-3xl font-bold text-6xl md:leading-tight text-[#42307D]">Our guaranties</h2>
          <p class="mt-4 text-base text-gray-600 mx-auto max-w-md">Lorem ipsum dolor sit amet, consectetur adipis elit</p>
        </div>
        <div class='mt-[54px] grid 2xl:grid-cols-3 gap-[100px] justify-between place-items-center grid-cols-1'>
          <div class='flex flex-col items-center text-center gap-[22px]' v-for='g in guaranties' :key='g.label'>
            <div class='space-y-[45px]'>
              <img :src='g.icon' alt='Icon' />
              <p class='text-[21px] font-semibold'>{{ g.label }}</p>
            </div>
            <p class='text-gray-600'>{{ g.description }} </p>
          </div>
        </div>
      </div>
    </section>
    <!-- guaranties end -->

    <!-- trust start -->
    <section id='trust'>
      <div class="xl:max-w-[90em] max-w-[82em] px-4 py-10 sm:px-6 lg:px-8 lg:py-14 mx-auto">
        <div class="sm:w-1/2 xl:w-1/3 mx-auto text-center mb-6">
          <h2 class="text-[20px] text-[#667085] md:leading-tight dark:text-gray-200">Trusted by 4,000+ companies</h2>
        </div>
        <div class="my-8 md:my-16 grid grid-cols-3 sm:flex sm:justify-center gap-6 sm:gap-x-12 lg:gap-x-20">
          <a class="flex-shrink-0 transition hover:-translate-y-1" href="#" v-for='c in companies' :key='c.logo'>
            <img :src='c.logo' alt='Brand' />
          </a>
        </div>
      </div>
    </section>
    <!-- trust end -->

    <!-- record start -->
    <section class='bg-[#0F172A] relative w-full z-40'>
      <div class="2xl:max-w-[90em] max-w-[82em] w-full mx-auto px-4 sm:px-6 lg:px-8">
        <div class='flex items-center 2xl:flex-row flex-col place-items-center justify-between'>
          <img class='2xl:h-[700px] 2xl:w-auto 2xl:absolute -top-[60px] w-full z-50' :src='note' alt='Note' />
          <div class='2xl:relative left-[calc(140px+50%)] max-w-min 2xl:py-20 py-8 w-full 2xl:w-auto text-white'>
            <div class='space-y-[16px]'>
              <h3 class='text-[36px] font-semibold'>Проконсультироваться</h3>
              <p class='text-[#94A3B8]'>Clarity gives you the blocks and components you need to create a truly professional website.</p>
            </div>
            <form class='mt-[40px]' @submit.prevent='handleSubmitRecord'>
              <div class='mb-[20px]'>
                <label for="name" class="block text-sm mb-2 dark:text-[#E4E4E7]">Имя</label>
                <input type="text" id="name" v-model='data.name'
                  class="py-3 px-4 block w-full rounded-full border-[#334155] bg-transparent border text-sm focus:border-blue-500 focus:ring-blue-500 dark:bg-slate-900 dark:border-gray-700 dark:text-gray-400"
                  placeholder="Введите ваше имя">
              </div>
              <div class='mb-[37px]'>
                <label for="tel" class="block text-sm mb-2 dark:text-[#E4E4E7]">Телефон</label>
                <input type="tel" id="tel" v-model='data.tel'
                  class="py-3 px-4 block w-full rounded-full border-[#334155] bg-transparent border text-sm focus:border-blue-500 focus:ring-blue-500 dark:bg-slate-900 dark:border-gray-700 dark:text-gray-400"
                  placeholder="Введите ваше имя">
              </div>
              <button class='block bg-blue-600 text-white rounded-full py-[12px] px-[54px] font-semibold text-sm ' type='submit'>Записаться</button>
            </form>
          </div>
        </div>
      </div>
    </section>
    <!-- record end -->

  </main>
  <!-- [main end] -->

  <!-- [footer start] -->
  <footer class='bg-[#F3F5F6] py-[64px]' id='contacts'>
    <div class="2xl:max-w-[90em] max-w-[82em] w-full mx-auto px-4 sm:px-6 lg:px-8">
      <div class='flex flex-col items-center text-center justify-center gap-[48px]'>
        <h3 class='font-bold text-[48px] text-transparent bg-clip-text bg-gradient-to-r from-[#6072B2] to-[#3B095F]'>Contact us</h3>
        <p class='text-black text-2xl'>Lorem ipsum dolor sit amet, consectetur</p>
        <div class='text-[#3C3C43]/85 mb-[28px]'>
          <p>Phone: +998 (99) 999-99-99</p>
          <p>E-mail: forexample@gmail.com</p>
        </div>
        <div class='flex items-center gap-[20px]'>
          <a :href='s.path' v-for='s in socials' :key='s.path'>
            <img :src='s.icon' alt='Social' />
          </a>
        </div>
      </div>
    </div>
  </footer>
  <!-- [footer end] -->
</template>

<script setup>
  import axios from 'axios'
  import { reactive } from 'vue'

  import { default as frameHeading } from './assets/images/frames/frame_heading.png'

  import { default as note } from './assets/images/go_record.png'
  import { default as heading } from './assets/images/heading.png'

  import { default as company2 } from './assets/images/companies/Company logo-1.png'
  import { default as company3 } from './assets/images/companies/Company logo-2.png'
  import { default as company4 } from './assets/images/companies/Company logo-3.png'
  import { default as company5 } from './assets/images/companies/Company logo-4.png'
  import { default as company6 } from './assets/images/companies/Company logo-5.png'
  import { default as company1 } from './assets/images/companies/Company logo.png'

  import { default as checkIcon } from './assets/images/icons/check_circle.png'
  import { default as checkIconPrimary } from './assets/images/icons/check_circle_primary.png'
  import { default as featuredIconFirst } from './assets/images/icons/featured_1.png'
  import { default as featuredIconSecond } from './assets/images/icons/featured_2.png'
  import { default as featuredIconThird } from './assets/images/icons/featured_3.png'
  import { default as productIcon } from './assets/images/icons/product.png'
  import { default as salesIcon } from './assets/images/icons/sales.png'
  import { default as supportIcon } from './assets/images/icons/support.png'

  import { default as socialTwitter } from './assets/images/socials/Social-1.png'
  import { default as socialTelegram } from './assets/images/socials/Social-2.png'
  import { default as socialFacebook } from './assets/images/socials/Social.png'

  import { BASE_URL } from './config'

  const navs = [
    { label: 'Главная', path: 'home' },
    { label: 'О нас', path: 'about' },
    { label: 'Наши проекты', path: 'projects' },
    { label: 'Об услугах', path: 'services' },
    { label: 'Почему мы', path: 'we' },
    { label: 'Нам доверяют', path: 'trust' },
    { label: 'Контакты', path: 'contacts' }
  ]

  const checks = [
    { label: 'SMM' },
    { label: 'Consulting' },
    { label: 'Develope' },
  ]

  const services = [
    {
      label: 'Consulting', sublabel: 'Billed annualy.', icon: featuredIconFirst, items: [
        { label: 'Access to all basic features' },
        { label: 'Access to all basic features' },
        { label: 'Access to all basic features' },
        { label: 'Access to all basic features' },
        { label: 'Access to all basic features' }
      ]
    },
    {
      label: 'Consulting', sublabel: 'Billed annualy.', icon: featuredIconSecond, items: [
        { label: 'Access to all basic features' },
        { label: 'Access to all basic features' },
        { label: 'Access to all basic features' },
        { label: 'Access to all basic features' },
        { label: 'Access to all basic features' }
      ]
    },
    {
      label: 'Consulting', sublabel: 'Billed annualy.', icon: featuredIconThird, items: [
        { label: 'Access to all basic features' },
        { label: 'Access to all basic features' },
        { label: 'Access to all basic features' },
        { label: 'Access to all basic features' },
        { label: 'Access to all basic features' }
      ]
    }
  ]

  const guaranties = [
    { label: 'Support', icon: supportIcon, description: 'Lorem ipsum dolor sit amet, consectetur adipis elit. Sit enim nec, proin faucibus nibh et sagittis a. Lacinia purus ac amet.' },
    { label: 'Product', icon: productIcon, description: 'Lorem ipsum dolor sit amet, consectetur adipis elit. Sit enim nec, proin faucibus nibh et sagittis a. Lacinia purus ac amet.' },
    { label: 'Sales', icon: salesIcon, description: 'Lorem ipsum dolor sit amet, consectetur adipis elit. Sit enim nec, proin faucibus nibh et sagittis a. Lacinia purus ac amet.' },
  ]

  const companies = [
    { logo: company1, path: '' },
    { logo: company2, path: '' },
    { logo: company3, path: '' },
    { logo: company4, path: '' },
    { logo: company5, path: '' },
    { logo: company6, path: '' },
  ]

  const socials = [
    { icon: socialFacebook, path: '' },
    { icon: socialTwitter, path: '' },
    { icon: socialTelegram, path: '' },
  ]

  const data = reactive({
    name: '',
    tel: ''
  })

  const handleSubmitRecord = () => {
    axios.post(BASE_URL, {
      name: data.name,
      tel: data.tel
    }).then((res) => {
      alert('Success')
      console.log(res)
    }).catch((e) => console.log(e))
  }
</script>