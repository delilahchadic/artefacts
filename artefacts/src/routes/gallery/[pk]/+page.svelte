<script lang="ts">
  import Gallery from '$lib/components/Gallery.svelte';
  import type { PageData } from './$types';
  export let data: PageData;
</script>
 <!-- {galleryName} -->
<Gallery gallery={data.gallery}></Gallery>



