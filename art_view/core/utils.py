import requests
class IIIFParser():
  # iiifUrl = ""
  # iiifManfiest ={}

  def __init__(self, url):
    self.iiifUrl = url
    try:
      response = requests.get(url)
      response.raise_for_status()

      if response.status_code == 200:
        print()
        self.iiifManifest = response.json()
    except requests.exceptions.RequestException as e:
      print(f"error occured")

  def getMetadata(self):
    if(self.iiifManifest["metadata"]):
      return self.iiifManifest["metadata"]
    return {} 
  
  def getArists(self):
    metadata = self.getMetadata()
    artists = []
    for item in metadata:
      if item["label"] == "Artist/Maker":
        for value in item["value"]:
          artists.append(value.split("(",1)[0].strip())
        
    return artists
  

  def getTitle(self):
    metadata = self.getMetadata()
    # artists = []
    for item in metadata:
      if item["label"] == "Title":
        return item["value"]
        
    return ""

    

def main():
  test =  IIIFParser("https://media.getty.edu/iiif/manifest/8b117dd1-db5d-4317-9b8d-5adb122f550d")
  # print("https://media.getty.edu/iiif/manifest/8b117dd1-db5d-4317-9b8d-5adb122f550d")
  print(test.getArists())
  url = "http://localhost:8000/iiif/"  # Make sure your URL matches
  iiif_url_to_send = "https://media.getty.edu/iiif/manifest/8b117dd1-db5d-4317-9b8d-5adb122f550d"
  headers = {'Content-Type': 'application/json'}
  payload = {'iiifUrl': iiif_url_to_send}

  try:
      response = requests.post(url, json=payload, headers=headers)
      response.raise_for_status()  # Raise an exception for bad status codes
      print(f"Status Code: {response.status_code}")
      print(f"Response JSON: {response.json()}")
  except requests.exceptions.RequestException as e:
      print(f"Error: {e}")

if __name__ == "__main__":
    main()