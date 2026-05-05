import { defineConfig } from "vitepress";
import texmath from "markdown-it-texmath";
import katex from "katex";

// https://vitepress.dev/reference/site-config

export default defineConfig({
  lang: "en-US",
  title: "Posters.science",
  description: "Documentation for posters.science",
  titleTemplate: "Posters.science Documentation - %s",
  appearance: true,
  lastUpdated: true,
  ignoreDeadLinks: false,
  markdown: {
    config: (md) => {
      md.use(texmath, {
        engine: katex,
        delimiters: "dollars",
      });
    },
  },
  head: [
    [
      "link",
      {
        rel: "stylesheet",
        href: "https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css",
      },
    ],
    [
      "link",
      {
        rel: "stylesheet",
        href: "https://cdn.jsdelivr.net/npm/markdown-it-texmath/css/texmath.min.css",
      },
    ],
    ["link", { rel: "icon", href: "favicon.ico" }],
    ["link", { rel: "manifest", href: "site.webmanifest" }],
    ["meta", { name: "theme-color", content: "#ffffff" }],
  ],

  themeConfig: {
    editLink: {
      pattern:
        "https://github.com/fairdataihub/posters-science-docs/edit/main/docs/:path",
    },
    socialLinks: [
      {
        icon: "github",
        link: "https://github.com/fairdataihub/posters-science",
      },
    ],
    nav: [{ text: "Documentation", link: "/docs/getting-started" }],
    sidebar: {
      "/docs": [
        {
          text: "Getting Started",
          collapsible: true,
          items: [{ text: "Introduction", link: "/docs/getting-started" }],
        },
      ],
    },
    footer: {
      copyright: "© 2026 FAIR Data Innovations Hub. All rights reserved.",
    },
  },
});
