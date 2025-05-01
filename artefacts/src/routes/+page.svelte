<script>
  import { onMount } from "svelte";
  // import { state } from 'svelte/store';
  // import { apiData, drinkNames } from './store.js';
  import PersonThumbnail from "$lib/components/PersonThumbnail.svelte";
  import WorkThumbnail from "$lib/components/WorkThumbnail.svelte";

  let data = $state([]);
  let work_data = $state([]);
  onMount(async () => {
    const response = await fetch('http://localhost:8000/people/');
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      
      const jsonData = await response.json();
      data= jsonData;

      const workResponse = await fetch('http://localhost:8000/works/');
      if (!workResponse.ok) {
        throw new Error(`HTTP error! status: ${workResponse.status}`);
      }
      
      const workJsonData = await workResponse.json();
      work_data= workJsonData;
    });
    

      
  
  </script>



<div class="flex flex-row text-center">
    <div class="flex-1">
      <div class="">
        <h1 class="text-2xl">People:</h1>
        <div class="grid grid-cols-5">
          {#each data as d}
          <PersonThumbnail person={d}></PersonThumbnail>
        {/each}
        </div>
        
      </div>

    <div class="">
      <h1 class="text-2xl">Works:</h1>
      <div class="grid grid-cols-5">
        {#each work_data as d}
        <WorkThumbnail work={d}></WorkThumbnail>
      {/each}
      </div>
    </div>
  </div>
  
</div>

