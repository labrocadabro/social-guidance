import api from "api";

export default defineEventHandler(async (event) => {
	try {
		const sdk = api("@preemo/v1.0#1r7781nlulnz4t2");
		const { query } = await readBody(event);
		sdk.auth(process.env.GRADIENT_ACCESS_TOKEN);
		sdk.server("https://api.gradient.ai/api");
		const completion = await sdk.completeModel(
			{
				autoTemplate: true,
				// guidance: { type: "choice" },
				rag: { collectionId: process.env.GRADIENT_RAG_ID },
				query,
				maxGeneratedTokenCount: 200,
			},
			{
				id: process.env.GRADIENT_MODEL_ID,
				"x-gradient-workspace-id": process.env.GRADIENT_WORKSPACE_ID,
			}
		);
		const reply = completion.data.generatedOutput;
		console.log(reply);
		return { reply };
	} catch (e) {
		console.log(e);
	}
});
