import type { Config } from "tailwindcss";

export default <Partial<Config>>{
	theme: {
		extend: {
			fontFamily: {
				header: ["Playfair Display", "serif"],
				body: ["Roboto Serif", "serif"],
				accent: ["Peralta", "serif"],
			},
			colors: {
				sepia: {
					100: "#f7f6e4",
					500: "#EAD9C0",
					800: "#4E2310",
				},
				accent: "#e45034",
			},
		},
	},
};
