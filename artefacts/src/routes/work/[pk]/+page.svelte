<script lang="ts">
  import { onMount } from "svelte";
  import type { PageProps } from './$types';
  import {IIIFParser} from "$lib/parse.js";
 

  let lightbox =$state(false);

	let prop: PageProps = $props();
  let iiif = $state(null);
  let creators = $state([]);
  let label = $state("");
  let metadata = $state<{label: string; value: string}[]>([]);
  let imageurl = $state("");
  let images = $state([]);
  let iiif_link = $state("");
  let description = $state("");
  let activeImage = $state("");
  interface Work {
    id: number;
    name: string;
  }

  interface IIIFResponse {
    link: string;
  }
  let test = $state<IIIFParser |null>(null);
  onMount(async () => {
    const call = await fetch('http://localhost:8000/work/' + prop.data.pk + '/IIIF/');
    const callJson = await call.json();
    
    creators = callJson.creators;
    iiif_link = callJson.link;
    test = new IIIFParser(callJson.link);
    await test.loadManifest();
    console.log(test);
    label = callJson.work.name;
    metadata = test.getMetadata();
    imageurl = test.getAllImageUrls()[0];
    images = test.getAllImageUrls();
    const manifestCall = await fetch(callJson.link);
    const manifestJson = await manifestCall.json()

    iiif = manifestJson
    description = test.getDescription();
  });

  function clickImage(imageUrl){
    lightbox = true;
    setActiveImage(images[0]);
  }

  function setActiveImage(imageUrl){
    activeImage=imageUrl;
    console.log(imageUrl);
  }
  </script>

{#if lightbox}
<div class="h-[100vh] w-[100vh]">
  <div class="relative max-h-[80%] flex  content-center">
    
    <img class="max-h-[70vh] mx-auto" src={activeImage}/>
    <button class="absolute top-0 right-2 bg-gray-200 hover:bg-gray-700 text-white font-bold py-2 px-4 rounded button" onclick="{() => lightbox=false}">X</button>
</div>
<div class="grid grid-cols-6 max-h-[10%]">
{#each images as image}
  <img class="p-4" src={image} onclick="{() => setActiveImage(image)}"/>
{/each}
</div>
</div>
  
{/if}
<div class="">
  <h1 class="text-3xl text-center mb-10">{label}</h1>
  <div class="flex flex-row gap-10" >

    <div class="mr-4 max-w-[30vw] w-fit flex-shrink-0 justify-self-center">
      <div class="w-fit"><img class= "pb-10 h-auto max-h-[70vh] w-auto object-contain ml-5" src={imageurl} onclick="{() =>clickImage(imageurl)}"/></div>
      
      <div class="break-words max-w-[20vw]" >
      {#each metadata as data }
      {#if data.label !== 'Rights Statement'}
        <p class="ml-2 text-[8px] ">{data.label} : {@html data.value}</p> 
        
      {/if}
      {/each}
    </div>
    </div>
    <div id="wiki" class=" text-center">
      <p class="text-sm mr-40">{@html description}</p>
      <a  class="block" href={iiif_link}>{iiif_link}</a>
      {#each creators as creator}
        <a href='/person/{creator.id}/'> more by {creator.name}</a>
      {/each}
    </div>
  </div>

  <h1 class="text-2x">All Images:</h1>
  <div class="grid max-h-[20vh] grid-cols-5">
    {#each images as image}
    <div class=" p-5 m-5 shadow-2xl">
      <img src={image} onclick="{() =>clickImage(image)}"/>
    </div>
    
    {/each}
  </div>
  
</div>
 

