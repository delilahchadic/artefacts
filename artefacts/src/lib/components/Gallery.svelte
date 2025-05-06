<script lang="ts">
  import { onMount } from "svelte";
  import type { PageProps } from './$types';
  import { IIIFParser } from "$lib/parse.js";
    import GalleryItem from "./GalleryItem.svelte";

  let prop: PageProps = $props();
  let gallery = $state(prop.gallery);
  let imageUrl = $state("");
  let collection = $state("");
  
  onMount(async () =>{
      // gallery = prop.gallery;
  });
  console.log($inspect(gallery)); 
</script>
<h1>{gallery.name}</h1>
<p>{gallery.description}</p>
<div class="grid grid-cols-4">
  {#each gallery.gallery_items as gi}
  <GalleryItem work={gi.work}></GalleryItem>
{/each}
</div>

