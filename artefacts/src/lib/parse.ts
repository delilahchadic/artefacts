class IIIFParser{
  manifestUrl: string;
  manifestData: any;

  constructor(manifestUrl: string){
    this.manifestUrl=manifestUrl;
    this.manifestData= null;
  }

  async loadManifest(): Promise<void>{
    try{
      const response = await fetch(this.manifestUrl);
      if(!response.ok){
        throw new Error('Failed to fetch manifest');
      }
      this.manifestData = await response.json();
    }
    catch(error){
      throw error;
    }
  }

  getLabel(): string {
    if (!this.manifestData) return "";
    if(this.manifestData.label['en']){
      return this.manifestData.label['en'];
    }   
    return this.manifestData.label; // Let the consumer handle language maps
  }

  getMetadata(): {label: string; value: string}[] {
    if(!this.manifestData || !this.manifestData.metadata){
      return [];
    }
    return this.manifestData.metadata.map((item: any) => ({
      label: item.label['en']? item.label['en'] : item.label,
      value: item.value['en']? item.value['en'] : item.value,
    }))
  } 

  getAllImageUrls(): string[] {
    const imageUrls: string[] = [];

    if (this.manifestData?.items ) {
      (this.manifestData?.items || [])
        .filter(item => item?.type === 'Canvas')
        .forEach(canvas => {
          (canvas?.items || [])
            .forEach(annotationPage => {
              (annotationPage?.items || [])
                .filter(annotation => annotation?.body?.type === 'Image' && annotation?.body?.id)
                .forEach(annotation => {
                  imageUrls.push(annotation.body.id);
                });
            });
        });
    } else {
      (this.manifestData?.sequences || [])
        .forEach(sequence => {
          (sequence?.canvases || [])
            .forEach(canvas => {
              (canvas?.images || [])
                .forEach(image => {
                  if (image?.resource?.['@id']) {
                    imageUrls.push(image.resource['@id']);
                  }
                });
            });
        });
    }

    return imageUrls;
  }

  getThumbnailUrl(): string | undefined {
    // ... (thumbnail logic - can be refined further for v3) ...
    if (this.manifestData?.thumbnail?.['@id']) {
      return this.manifestData.thumbnail['@id'];
    } else if (this.manifestData?.thumbnail?.length > 0 && this.manifestData.thumbnail[0]?.['@id']) {
      return this.manifestData.thumbnail[0]['@id'];
    } else if (this.manifestData?.items?.[0]?.thumbnail?.length > 0 && this.manifestData.items[0].thumbnail[0]?.id) {
      return this.manifestData.items[0].thumbnail[0].id;
    } else {
      return this.getAllImageUrls()[0];
    }
  }

  getCollection(): string{
    
    let collectionAliases = ["Collection", "Institution"];
    let item;

    for(const alias of collectionAliases){
      const v2Check = this.manifestData?.metadata?.find(item => item.label=== alias )?.value;
      if(v2Check){
        return v2Check;
      }

      const v3Check = this.manifestData?.metadata?.find(item => item.label && item.label.en &&  item.label.en[0] === alias);
      if(v3Check){
        return v3Check.value.en[0];
      }
    }

    return "";
   
  }
}

export { IIIFParser };
