---
layout: page
---
<script setup>
import {
  VPTeamPage,
  VPTeamPageTitle,
  VPTeamMembers
} from 'vitepress/theme'

const members = [
  {
    avatar: 'https://avatars.githubusercontent.com/u/59009530',
    name: 'HK560',
    title: 'R2Chef创建者',
    links: [
      { icon: 'github', link: 'https://github.com/HK560' },
      { icon: 'twitter', link: 'https://x.com/_HK560_' },
      { icon: 'bilibili', link: 'https://space.bilibili.com/7342356' }
    ]
  },
]
</script>

<VPTeamPage>
  <VPTeamPageTitle>
    <template #title>
      文档贡献者
    </template>
    <template #lead>
    </template>
  </VPTeamPageTitle>
  <VPTeamMembers :members />
</VPTeamPage>