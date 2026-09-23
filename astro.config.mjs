import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
import { fileURLToPath } from 'node:url';

export default defineConfig({
  site: 'https://belerofonte1973.github.io',
  base: '/curso-justica-grega',
  title: 'Justiça na Literatura Grega',
  description: 'Curso sobre o conceito de justiça e seus cognatos na literatura grega: poesia, tragédia, história e filosofia',
  logo: {
    src: '/logo.svg',
    alt: 'Justiça na Literatura Grega',
  },
  integrations: [
    starlight({
      title: 'Justiça na Literatura Grega',
      description: 'Díkē, Têmis, Aidôs, Nómos e Dikaiosýne na tradição grega',
      sidebar: [
        { label: 'Curso', autogenerate: { directory: 'docs' } },
        { label: 'Recursos', autogenerate: { directory: 'docs/recursos' } },
        { label: 'Sobre', autogenerate: { directory: 'docs/sobre' } },
      ],
    }),
  ],
  vite: {
    resolve: {
      alias: {
        '@': fileURLToPath(new URL('./src', import.meta.url)),
      },
    },
  },
});
