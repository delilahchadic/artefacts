<script lang="ts">
  import { onMount } from "svelte";
  import type { PageProps } from './$types';
  import { IIIFParser } from "$lib/parse.js";

  let prop: PageProps = $props();
  let work = $state(prop.work);
  let imageUrl = $state("");
  // let collection = $state("");
  // let data = $state([]);
  onMount(async () =>{
    
    // const call = await fetch('http://localhost:8000/work/' + work.id + '/IIIF/');
    // const callJson = await call.json();

      const iiif_doc = new IIIFParser(work.documents[0]?.link);
      await iiif_doc.loadManifest();
      
      imageUrl = await iiif_doc.getThumbnailUrl();
      // collection = iiif_doc.getCollection();
      
  });
</script>

<a class="max-w-[20vw] p-4 m-4 shadow-md contain-content" href="/work/{work.id}">
  <h1 class="text-xs">{work.name}</h1>
  <img  class="justify-center" src={imageUrl}/>
  <!-- <p class="text-xs">{@html collection}</p> -->
</a>
