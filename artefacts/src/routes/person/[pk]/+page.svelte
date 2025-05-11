<script lang="ts">
  import { onMount } from "svelte";
  import type { PageProps } from './$types';
  import {IIIFParser} from "$lib/parse.js";
  import WorkThumbnail from "$lib/components/WorkThumbnail.svelte";
	
  let prop: PageProps = $props();
  let imageUrl = $state("");
  let data = $state([]);
  let works = $state([]);
  let iiif_images = $state<{[key:number]: any}>({});
  let iiif = $state<{ [key: number]: any | undefined }>({}); 
  let wikiSummary = $state("");
  interface Work {
    id: number;
    name: string;
  }

  interface IIIFResponse {
    link: string;
  }

  onMount(async () => {
    const response = await fetch('http://localhost:8000/person/' + prop.data.pk);
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    const jsonData = await response.json();
    data = jsonData;

    wikiSummary = await fetchWikipediaFirstParagraphHTML(data.name);

    const workResponse = await fetch('http://localhost:8000/person/works/' + prop.data.pk + "");
    const jsonWorkData = await workResponse.json();
    works = jsonWorkData;

    for(let i = 0;i < works.length;i++ ){
      let work = works[i];
      const call = await fetch('http://localhost:8000/work/' + work.id + '/IIIF/');
      const callJson = await call.json();
      const manifestCall = await fetch(callJson.link);
      const manifestJson = await manifestCall.json()
      const iiif_doc = new IIIFParser(callJson.link);
      await iiif_doc.loadManifest();
      iiif_images[work.id] = iiif_doc.getThumbnailUrl();
      iiif[work.id] = manifestJson
    }

  });

  async function fetchWikipediaFirstParagraphHTML(title: string): Promise<string> {
  const apiUrl = `https://en.wikipedia.org/w/api.php?action=parse&page=${encodeURIComponent(title)}&format=json&prop=text&origin=*`;

  try {
    const response = await fetch(apiUrl);
    const data = await response.json();

    if (data.parse && data.parse.text && data.parse.text['*']) {
      const htmlContent = data.parse.text['*'];
      const tempDiv = document.createElement('div');
      tempDiv.innerHTML = htmlContent;
      
      const firstParagraph = tempDiv.querySelector('.mw-parser-output > p:not(.mw-empty-elt)');
      const images = tempDiv.querySelectorAll('img');
      console.log(images)
      imageUrl = images[0].src;
      const links = firstParagraph?.querySelectorAll('a');
      

      links.forEach(link => {
        const href = link.getAttribute('href');
        if (href && href.startsWith('/wiki/')) {
          link.setAttribute('href', `https://en.wikipedia.org${href}`);
          link.setAttribute('target', '_blank'); // Optional: Open links in a new tab
          link.setAttribute('rel', 'noopener noreferrer'); // Recommended for security when using target="_blank"
        }
      });
      return firstParagraph ? firstParagraph.outerHTML : "";
    } else {
      console.error("Could not extract HTML from Wikipedia API response.");
      return "";
    }
  } catch (error) {
    console.error("Error fetching from Wikipedia API:", error);
    return "";
  }
}

</script>

<h1 class="text-4xl m-3">{data.name}</h1>
<div class="flex">
  <div >
    <img  class="max-w-[20vw] m-5" src={imageUrl}/>
  </div>
  <div id="wiki">
    <p class="m-5 a:text-blue-500">{@html wikiSummary}</p>
    <p class=" m-5 text-[8px]">from Wikipedia</p>
  </div>
  
  </div>
  <div>
    <div class="grid grid-cols-5">
      {#each works as d}
        <WorkThumbnail work={d}></WorkThumbnail>     
      {/each}
    </div>
</div>





