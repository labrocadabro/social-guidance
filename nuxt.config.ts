// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
	devtools: { enabled: true },
	modules: ["@nuxtjs/tailwindcss", "@nuxtjs/google-fonts"],
	googleFonts: {
		families: {
			Yesteryear: true,
			Peralta: true,
			"Roboto Serif": [400],
			"Playfair Display": [600],
		},
	},
	nitro: {
		preset: 'node-server',
	},
	app: {
		baseURL: '/',
		buildAssetsDir: '/_nuxt/',
	},
});
