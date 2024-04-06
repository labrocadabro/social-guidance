export default defineEventHandler(async (event) => {
	try {
		const { query } = await readBody(event);

		const options = {
			method: "POST",
			headers: {
				accept: "application/json",
				"content-type": "application/json",
				authorization: `Bearer ${process.env.GRADIENT_ACCESS_TOKEN}`,
				"x-gradient-workspace-id": process.env.GRADIENT_WORKSPACE_ID,
			},
			body: JSON.stringify({
				autoTemplate: true,
				rag: { collectionId: process.env.GRADIENT_RAG_ID },
				query,
				maxGeneratedTokenCount: 200,
			}),
		};

		const res = await fetch(
			`https://api.gradient.ai/api/models/${process.env.GRADIENT_MODEL_ID}/complete`,
			options
		);
		const completion = await res.json();
		console.log(completion);

		const reply = completion.generatedOutput;
		console.log(reply);
		return { reply };
	} catch (e) {
		console.log(e);
	}
});
