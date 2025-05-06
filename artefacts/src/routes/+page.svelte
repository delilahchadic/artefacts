<script>
  import { onMount } from "svelte";
  // import { state } from 'svelte/store';
  // import { apiData, drinkNames } from './store.js';
  import PersonThumbnail from "$lib/components/PersonThumbnail.svelte";
  import WorkThumbnail from "$lib/components/WorkThumbnail.svelte";
    import { IIIFParser } from "$lib/parse.js";
  
  let data = $state([]);
  let work_data = $state([]);
  let welcome_image = $state('');
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

      const welcomResponse = await fetch('http://localhost:8000/work/4/IIIF/');
      const welcomeJson = await welcomResponse.json();
      const welcome_ifff = new IIIFParser(welcomeJson.link);
      await welcome_ifff.loadManifest();
      welcome_image = welcome_ifff.getAllImageUrls()[0];

    });
    

      
  
  </script>
<div class="grid grid-cols-4 p-4">
  <div class ="text-center" > <a href="/person/">People</a></div>
  <div class ="text-center" > <a href="/work/">Works</a></div>
  <div class ="text-center" > <a href="/gallery/1">Galleries </a></div>
  <div class ="text-center" > <a href="">about </a></div>
</div>
<div class="grid grid-cols-8 h-[100vh]">
  <div class="col-span-2">
    <h1 class="text-zinc-400 text-4xl  pt-45 pl-15">Welcome Artefacts</h1>
  </div>
  <div class="col-span-6">
    <a href="/work/4">
      <img src={welcome_image} href="/work/4"/>
    </a>
    
  </div>
  
</div>

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

