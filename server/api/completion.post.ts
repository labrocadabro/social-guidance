import api from "api";

export default defineEventHandler(async (event) => {
	try {
		// const sdk = api("@preemo/v1.0#1r7781nlulnz4t2");
		// const { query } = await readBody(event);
		// sdk.auth(process.env.GRADIENT_ACCESS_TOKEN);
		// sdk.server("https://api.gradient.ai/api");
		// const completion = await sdk.completeModel(
		// 	{
		// 		autoTemplate: true,
		// 		// guidance: { type: "choice" },
		// 		rag: { collectionId: process.env.GRADIENT_RAG_ID },
		// 		query,
		// 		maxGeneratedTokenCount: 200,
		// 	},
		// 	{
		// 		id: process.env.GRADIENT_MODEL_ID,
		// 		"x-gradient-workspace-id": process.env.GRADIENT_WORKSPACE_ID,
		// 	}
		// );
		// const reply = completion.data.generatedOutput;
		// console.log(reply);
		function delay(ms: number) {
			return new Promise((resolve) => setTimeout(resolve, ms));
		}
		await delay(3000);
		const reply =
			"Being a good citizen involves doing little things for others and being considerate of those around you. You can start by helping your friends and classmates in small ways, such as tying their sash or helping them prepare for a lesson. It's also important to think ahead and be prepared, so you don't disturb others or cause trouble. During recess, you can play games that everyone can enjoy, and make sure to include others in your activities. Doing your job the best you can and taking pride in your work is also part of being a good citizen. Additionally, being careful and neat, and practicing good manners such as picking up after yourself and not holding up lines, are important habits to develop. As you grow older, these habits will become second nature and you will be seen as a considerate and responsible person.";
		return { reply };
	} catch (e) {
		console.log(e);
	}
});
