<script setup lang="ts">
import questions from "../data/questions";
const query = ref("");
const reply = ref("");
const loading = ref(false);
const error = ref(false);
const showForm = computed(() => {
	return !loading.value && reply.value.length === 0;
});
async function getReply() {
	try {
		loading.value = true;
		error.value = false;
		const data = await $fetch("/api/completion", {
			method: "POST",
			headers: {
				"Content-Type": "application/json",
			},
			body: { query: query.value },
		});
		loading.value = false;
		if (data) {
			reply.value = data.reply;
		}
	} catch {
		error.value = true;
		loading.value = false;
	}
}

function reset() {
	reply.value = "";
	query.value = "";
}
function randomQuestion() {
	const randomQ = questions[Math.floor(Math.random() * questions.length)];
	query.value = randomQ;
}
</script>

<template>
	<img src="~/assets/man-sepia.png" class="h-screen absolute left-10" />
	<img src="~/assets/woman-sepia.png" class="h-screen absolute right-10" />
	<div class="pt-10 mx-auto w-1/2 text-center">
		<h1 class="mb-4">Etiquette advice from the 1950s</h1>
		<h2 class="mb-2">As taught in social guidance films</h2>
		<NuxtLink to="/about" class="block">What is social guidance?</NuxtLink>
		<div v-show="loading" class="mt-20">
			<clock-spinner class="mx-auto" />
		</div>
		<form
			@submit.prevent="getReply"
			class="mx-auto w-96 text-left pt-10"
			v-show="showForm"
		>
			<div v-show="error" class="text-red-500 font-bold mb-2">
				Something went wrong, please try again.
			</div>
			<div class="relative">
				<textarea
					name="query"
					id="query"
					rows="5"
					v-model="query"
					class="block w-full rounded-lg py-5 px-12 bg-sepia-100 focus:outline focus:outline-2 focus:outline-sepia-800"
				/>
				<label for="query" class="font-accent text-sepia-100 z-20 absolute"
					>Ask for advice</label
				>
				<div class="arrow-top"></div>
				<div class="arrow-left"></div>
				<div class="arrow-bottom"></div>
				<div class="arrow-head"></div>
				<button class="font-accent text-sepia-100 text-2xl z-20 absolute">
					Submit
				</button>
			</div>
			<button
				class="again block mx-auto bg-accent text-sepia-100 font-accent font-2xl px-5 py-3 rounded-lg mt-20"
				@click.prevent="randomQuestion"
			>
				Random Question
			</button>
		</form>
		<div v-show="reply" class="-mt-10 mx-auto text-left pt-10 reply">
			<p class="text-lg max-h-[60vh] overflow-scroll no-scrollbar">
				{{ reply }}
			</p>
			<button
				class="again block mx-auto bg-accent text-sepia-100 font-accent font-2xl px-5 py-3 rounded-lg mt-4"
				@click="reset"
			>
				Ask again
			</button>
		</div>
	</div>
</template>

<style>
textarea {
	transform: perspective(25px) rotateX(1deg);
}
label {
	top: -25px;
	left: 40px;
}
form button {
	right: 85px;
	bottom: -37px;
}
.arrow-bottom,
.arrow-head,
.arrow-left,
.arrow-top {
	@apply rounded z-10 absolute;
}
.arrow-bottom,
.arrow-left,
.arrow-top {
	@apply bg-accent;
}
.arrow-top {
	width: 220px;
	height: 40px;
	top: -30px;
	left: 10px;
}
.arrow-left {
	width: 40px;
	height: 250px;
	bottom: -40px;
	left: -10px;
	transform: skew(-5deg);
}
.arrow-bottom {
	width: 330px;
	height: 40px;
	bottom: -40px;
	left: 8px;
}
.arrow-head {
	width: 100px;
	height: 80px;
	bottom: -60px;
	right: -20px;
	border-top: 40px solid transparent;
	border-bottom: 40px solid transparent;
	border-left: 100px solid #e45034;
}
.reply {
	width: calc(100vw - 135vh);
}
.again {
	transform: perspective(25px) rotateX(1deg);
}
</style>
