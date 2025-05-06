import type { PageLoad } from './$types';

export const load: PageLoad = async ({ fetch, params }) => {
  const { pk } = params;
  const response = await fetch(`http://localhost:8000/gallery/${pk}`);
  if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
  const jsonData = await response.json();
  return { gallery: jsonData.gallery };
};