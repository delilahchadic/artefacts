<script>
  import { onMount } from "svelte";
  // import { state } from 'svelte/store';
  // import { apiData, drinkNames } from './store.js';
  let data = $state([]);

  onMount(async () => {
    const response = await fetch('http://localhost:8000/people/');
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      const jsonData = await response.json();
      data= jsonData;
    });
  </script>

<h1>Welcome to SvelteKit</h1>
{#each data as d}
  <h1>{d.first_name}</h1>
{/each}
<p class="bg-amber-700">Visit <a href="https://svelte.dev/docs/kit">svelte.dev/docs/kit</a> to read the documentation</p>
