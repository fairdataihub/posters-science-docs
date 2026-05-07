import { defineConfig } from "vitepress";
import texmath from "markdown-it-texmath";
import katex from "katex";

export default defineConfig({
  lang: "en-US",
  title: "Posters.science",
  description: "Documentation for the Posters.science platform",
  titleTemplate: "Posters.science - %s",
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
      text: "Edit this page on GitHub",
    },

    socialLinks: [
      {
        icon: "github",
        link: "https://github.com/fairdataihub/posters-science",
      },
    ],

    nav: [
      {
        text: "User Guide",
        link: "/docs/intro",
      },
      {
        text: "Developer Guide",
        link: "https://dev.posters.science",
      },
      {
        text: "Contact Us",
        link: "https://tally.so/r/RG8Avd",
      },
    ],

    sidebar: {
      "/docs": sidebarGuide(),
    },

    footer: {
      message: "Released under the MIT License.",
      copyright: "Copyright 2025-present | FAIR Data Innovations Hub",
    },
  },
});

function sidebarGuide() {
  return [
    {
      text: "Getting Started",
      collapsible: true,
      items: [
        { text: "Introduction", link: "/docs/intro" },
        { text: "About Posters.science", link: "/docs/about" },
        { text: "Creating an Account", link: "/docs/account" },
      ],
    },
    {
      text: "Sharing Posters",
      collapsible: true,
      items: [
        { text: "Overview", link: "/docs/sharing" },
        { text: "Uploading Your Poster", link: "/docs/upload" },
        { text: "Reviewing Metadata", link: "/docs/metadata" },
        { text: "Publishing to a Repository", link: "/docs/publish" },
      ],
    },
    {
      text: "Discovering Posters",
      collapsible: true,
      items: [
        { text: "Searching the Registry", link: "/docs/search" },
        { text: "Overview Page", link: "/docs/overview-page" },
      ],
    },
    {
      text: "Behind the Scenes",
      collapsible: true,
      items: [
        { text: "The Poster Schema", link: "/docs/schema" },
        { text: "Metadata Extraction", link: "/docs/extraction" },
        { text: "Auto-Registration", link: "/docs/auto-registration" },
        { text: "FAIR Principles for Posters", link: "/docs/fair" },
      ],
    },
    {
      text: "Resources",
      collapsible: true,
      items: [
        { text: "FAQ", link: "/docs/faq" },
        { text: "Ecosystem", link: "/docs/ecosystem" },
        { text: "Citing Posters.science", link: "/docs/citing" },
        { text: "Contributing", link: "/docs/contributing" },
      ],
    },
  ];
}
