<script>
    import PersonThumbnail from "$lib/components/PersonThumbnail.svelte";
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

<h1 class ="text-2xl text-center">People: </h1>
<div class="grid grid-cols-5">
  {#each data as d}
  <PersonThumbnail person={d}></PersonThumbnail>
{/each}
</div>

