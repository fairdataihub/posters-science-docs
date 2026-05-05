import { defineConfig } from 'vitepress';
import { withMermaid } from 'vitepress-plugin-mermaid';

export default withMermaid(
  defineConfig({
    lang: 'en-US',
    title: 'posters.science',
    description: 'Documentation for posters.science',
    titleTemplate: 'posters.science',
    port: 3000,

    appearance: true,
    lastUpdated: true,
    ignoreDeadLinks: false,

    markdown: {
      lineNumbers: true,
    },

    mermaid: {},

    head: [
      ['link', { rel: 'icon', href: 'favicon.ico' }],
      ['link', { rel: 'manifest', href: 'site.webmanifest' }],
      ['meta', { name: 'theme-color', content: '#ffffff' }],
    ],

    themeConfig: {
      editLink: {
        pattern:
          'https://github.com/fairdataihub/docs.posters.science/edit/main/docs/:path',
        text: 'Edit this page on GitHub',
      },

      socialLinks: [
        {
          icon: 'github',
          link: 'https://github.com/fairdataihub/docs.posters.science',
        },
      ],

      nav: [{ text: 'Documentation', link: '/docs/getting-started' }],

      sidebar: {
        '/docs': [
          {
            text: 'Getting Started',
            collapsible: true,
            items: [{ text: 'Introduction', link: '/docs/getting-started' }],
          },
        ],
      },

      footer: {
        message: 'Released under the MIT License.',
        copyright: 'Copyright © present | fairdataihub',
      },
    },
  }),
);
