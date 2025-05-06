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

<!-- <a class="max-w-[20vw] p-4 m-4 shadow-md" href="/person/{person.id}">
  <h1 class="text-xs">{person.first_name} {person.last_name}</h1>
  <img  class="" src={imageUrl}/>
</a> -->

<form>
  <label for="email">Email:</label><br>
  <input type="text" id="email" name="email"><br>
  <label class="mt-5" for="password">Password:</label><br>
  <input type="password" id="password" name="password"><br>
  <button class="rounded-md bg-black text-white p-2 mt-5" type="submit" value="Submit">Submit</button>
</form>