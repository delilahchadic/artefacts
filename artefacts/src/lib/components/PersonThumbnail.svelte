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
  });
</script>

<a class="max-w-[20vw] p-4 m-4 shadow-md bg-white" href="/person/{person.id}">
  <h1 class="text-xs">{person.name}</h1>
  <img  class="" src={imageUrl}/>
</a>


