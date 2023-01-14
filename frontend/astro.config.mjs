import { defineConfig } from 'astro/config';

// https://astro.build/config
import svelte from "@astrojs/svelte";

// https://astro.build/config
import tailwind from "@astrojs/tailwind";

// https://astro.build/config
import deno from "@astrojs/deno";

// https://astro.build/config
export default defineConfig({
  integrations: [svelte(), tailwind()],
  output: "server",
  adapter: deno({
    port: 8000,
    hostname: 'localhost',
  })
});