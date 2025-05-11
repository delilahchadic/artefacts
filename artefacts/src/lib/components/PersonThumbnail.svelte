<script lang="ts">
  import { onMount } from "svelte";
  import type { PageProps } from './$types';

  let prop: PageProps = $props();
  let person = $state(prop.person);
  let imageUrl = $state("");
  // let data = $state([]);
  onMount(async () =>{
    const imageResponse = await fetch('http://localhost:8000/person/' + prop.person.id + '/image');
    const jsonImage = await imageResponse.json();
    // imageUrl = jsonImage.value;
    imageUrl = await getWikiImage(person.name);
  });

  async function getWikiImage(title: string): Promise<string> {
    const apiUrl = `https://en.wikipedia.org/w/api.php?action=parse&page=${encodeURIComponent(title)}&format=json&prop=text&origin=*`;
    
    try {
      const response = await fetch(apiUrl);
      const data = await response.json();

      if (data.parse && data.parse.text && data.parse.text['*']) {
        const htmlContent = data.parse.text['*'];
        const tempDiv = document.createElement('div');
        tempDiv.innerHTML = htmlContent;
        const images = tempDiv.querySelectorAll('img');
        let url = images[0]? images[0].src : "";
        return url;
      } else {
        return "";
      }
    } catch (error) {
      console.error("Error fetching from Wikipedia API:", error , title);
      return "";
    }
}
</script>

<a class="max-w-[20vw] p-4 m-4 shadow-md bg-white" href="/person/{person.id}">
  <h1 class="text-xs">{person.name}</h1>
  <img  class="" src={imageUrl}/>
</a>


