import { defineConfig } from 'vitepress'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "R2Chef🧑‍🍳",
  lang: "zh-CN",
  description: "泰坦陨落2 模组开发文档",
  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    socialLinks: [
      { icon: 'github', link: 'https://github.com/HK560/R2Chef' },
      { icon: 'bilibili', link: 'https://space.bilibili.com/7342356' }
    ],
    i18nRouting: true,
  },
  locales: {
    root: {
      label: '简体中文',
      lang: 'zh-CN',
      themeConfig: {
        nav: [
          { text: '首页', link: '/' },
          { text: '文档教程', link: '/mainpage' }
        ],
        sidebar: [
          {
            text: 'MDL模组教程',
            link: '/tutorial/mdlmodding/index',
            items: [
              { text: '武器改模教程', link: '/tutorial/mdlmodding/weaponMod/index', 
                items: [
                  { text: '1.获取游戏资产文件', link: '/tutorial/mdlmodding/weaponMod/1' },
                  // { text: '获取游戏模型', link: '/tutorial/mdlmodding/weaponMod/2' },
                ]
              },
              { text: '人物改模教程', link: '/tutorial/mdlmodding/characterMod/index' },
            ]
          },
          {
            text: '文档',
            items: [
              { text: '修改武器动画', link: '/docs/weaponAnimMod' },
              { text: '动态皮肤(VTF)制作', link: '/docs/animTex' },
              { text: '注意事项', link: '/docs/tips' },
              { text: 'REPAK文档', link: '/docs/repak' },
              { text: '移植COD武器MOD', link: '/docs/modFromcod' },
            ]
          },
          {
            text: '杂项',
            items: [
              { text: '工具资源收集', link: '/misc/tools' }
            ]
          }
        ],
      }
    },
    en: {
      label: 'English',
      lang: 'en-US',
      themeConfig: {
        nav: [
          { text: 'Home', link: '/' },
          { text: 'Examples', link: '/en/markdown-examples' }
        ],
        sidebar: [
          {
            text: 'Modding',
            items: [
              { text: 'MDL Modding', link: '/en/mdlmodding/index' },
              { text: 'Runtime API Examples', link: '/en/api-examples' }
            ]
          }
        ]
      }
    }
  },
  markdown: {
    image:{
      lazyLoading: true,
    }
  }

})
