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
    imageUrl = jsonImage.value;
    fetchWikipediaFirstParagraphHTML(person.name)
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
        
        // const firstParagraph = tempDiv.querySelector('.mw-parser-output > p:not(.mw-empty-elt)');
        const images = tempDiv.querySelectorAll('img');
        // console.log(images)
        imageUrl = images[0].src;
        // const links = firstParagraph?.querySelectorAll('a');
        

        // links.forEach(link => {
        //   const href = link.getAttribute('href');
        //   if (href && href.startsWith('/wiki/')) {
        //     link.setAttribute('href', `https://en.wikipedia.org${href}`);
        //     link.setAttribute('target', '_blank'); // Optional: Open links in a new tab
        //     link.setAttribute('rel', 'noopener noreferrer'); // Recommended for security when using target="_blank"
        //   }
        // });
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

<a class="max-w-[20vw] p-4 m-4 shadow-md bg-white" href="/person/{person.id}">
  <h1 class="text-xs">{person.name}</h1>
  <img  class="" src={imageUrl}/>
</a>


