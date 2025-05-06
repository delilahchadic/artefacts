<script lang="ts">
  import { onMount } from "svelte";
  // import { state } from 'svelte/store';
  // import { apiData, drinkNames } from './store.js';
  import PersonThumbnail from "$lib/components/PersonThumbnail.svelte";
  import WorkThumbnail from "$lib/components/WorkThumbnail.svelte";
    import { IIIFParser } from "$lib/parse.js";
  
  // let data = $state([]);
  let work_data = $state([]);
  // let welcome_image = $state('');
  onMount(async () => {
    const workResponse = await fetch('http://localhost:8000/works/');
    if (!workResponse.ok) {
      throw new Error(`HTTP error! status: ${workResponse.status}`);
    }
    
    const workJsonData = await workResponse.json();
    work_data= workJsonData;

      const welcomResponse = await fetch('http://localhost:8000/work/4/IIIF/');
      const welcomeJson = await welcomResponse.json();
    });
</script>

<div class="">
  <h1 class="text-2xl">Works:</h1>
  <div class="grid grid-cols-5">
    {#each work_data as d}
    <WorkThumbnail work={d}></WorkThumbnail>
  {/each}
  </div>
</div>