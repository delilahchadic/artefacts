import requests
import csv

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

class Production():
  
  def __init__(self, url):
    self.url = url
    response = requests.get(url)
    try:
      if response.status_code == 200:
          print()
          self.production = response.json()
    except requests.exceptions.RequestException as e:
      print(f"error occured")

  def get_artist(self):
    for item in self.production["referred_to_by"]:
      if item["_label"] == "Artist/Maker (Producer) Name":
        return item["content"]
    return ""

    

def main():
  
#    SELECT ?subject ?object1 ?object2
#    WHERE {
  #   ?subject crm:P129i_is_subject_of ?object1 .
  #   FILTER (CONTAINS(LCASE(str(?object1)), "iiif"))
  #   ?subject crm:P108i_was_produced_by ?object2 .
#     }

  test = Production("https://data.getty.edu/museum/collection/object/326eb488-8000-4132-beb8-7f00004370b8/production")
  print(test.get_artist())
  url = "http://localhost:8000/iiif/"  # Make sure your URL matches
  headers = {'Content-Type': 'application/json'}
  with open("/Users/damonchadic/art-proj/data.csv", 'r', newline='') as csv_data:
    reader = csv.reader(csv_data)
    count =0
    for row in reader:
      if count > 100:
        return
      artist = Production(row[2]).get_artist()
      payload = {'iiifUrl': row[1], 'artist' : artist}
      try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()  # Raise an exception for bad status codes
        print(f"Status Code: {response.status_code}")
        print(f"Response JSON: {response.json()}")
        count +=1
      except requests.exceptions.RequestException as e:
        print(f"Error: {e}")



#   test =  IIIFParser("https://media.getty.edu/iiif/manifest/8b117dd1-db5d-4317-9b8d-5adb122f550d")
#   # print("https://media.getty.edu/iiif/manifest/8b117dd1-db5d-4317-9b8d-5adb122f550d")
#   print(test.getArists())
#   url = "http://localhost:8000/iiif/"  # Make sure your URL matches
#   iiif_url_to_send = "https://media.getty.edu/iiif/manifest/8b117dd1-db5d-4317-9b8d-5adb122f550d"
#   headers = {'Content-Type': 'application/json'}
#   # payload = {'iiifUrl': iiif_url_to_send}

#   iiifs =[
# "https://media.getty.edu/iiif/manifest/61b06764-9b66-4740-b01f-d0fecfea6689",
# "https://media.getty.edu/iiif/manifest/2c35cff8-071d-4d6d-b8c4-744cb09e8f5b",
# "https://media.getty.edu/iiif/manifest/446f1bcb-6ca7-4949-ae0b-7eefc32628af",
# "https://media.getty.edu/iiif/manifest/a8e2ac5d-a568-4f74-9d06-b37e4078e1ca",
# "https://media.getty.edu/iiif/manifest/404ed872-3314-46ec-a422-a3e67f648063",
# "https://media.getty.edu/iiif/manifest/a32a0ad3-bd3b-4d6e-9ef2-d04fcfce73cd",
# "https://media.getty.edu/iiif/manifest/24457646-0907-41d8-98f8-88cb48391832",
# "https://media.getty.edu/iiif/manifest/853a3ff8-bb49-4062-b557-01db7ac0deda",
# "https://media.getty.edu/iiif/manifest/f39c3ab3-d636-4423-a3aa-a83eabf5ecdc",
# "https://media.getty.edu/iiif/manifest/634b493f-650c-4ff1-9625-ab7159de1a8e",
# "https://media.getty.edu/iiif/manifest/c5089f5f-4588-41a5-a1fa-cc6e6d74d023",
# "https://media.getty.edu/iiif/manifest/61f5cbb0-1bc8-48a2-8b98-84ef3f8eca27",
# "https://media.getty.edu/iiif/manifest/63998b4b-1faa-4a97-9d2a-5756eb8e673d",
# "https://media.getty.edu/iiif/manifest/638761e6-8613-4e18-bb6c-84ade6b3276a",
# "https://media.getty.edu/iiif/manifest/7bef3cc2-18bf-4cf1-af0b-645be7d945de",
# "https://media.getty.edu/iiif/manifest/c17c8fbd-b915-4d0b-8298-200ba8e3c5cc",
# "https://media.getty.edu/iiif/manifest/b45fde94-acf8-4d1c-bc67-5d8840fa1115",
# "https://media.getty.edu/iiif/manifest/0c4879de-17ef-475f-9336-262579a5b4c9",
# "https://media.getty.edu/iiif/manifest/26f0d45a-3ca5-401e-a904-c321c593be24",
# "https://media.getty.edu/iiif/manifest/fd1c36de-b278-4748-ab28-3bcf4b68182f",
# "https://media.getty.edu/iiif/manifest/dc5fa00d-53a8-4abc-ab61-22bc74c63d96",
# "https://media.getty.edu/iiif/manifest/ecaa4011-d1c5-4dbf-9b78-cbcb53d1acf2",
# "https://media.getty.edu/iiif/manifest/e54c5163-2a49-45c0-b591-a05c2ba0f06b",
# "https://media.getty.edu/iiif/manifest/4db6c63d-5754-4851-b62c-839eaaaa1865",
# "https://media.getty.edu/iiif/manifest/48fd2f61-9697-4be5-91fb-2463e0601e59",
# "https://media.getty.edu/iiif/manifest/74d208ec-13f4-4f74-8363-a98fe13c5fc0",
# "https://media.getty.edu/iiif/manifest/ad28221b-1d88-4da5-8e73-491c2f3c6b93",
# "https://media.getty.edu/iiif/manifest/439455ef-25d1-40c3-8da8-4589d7aa2726",
# "https://media.getty.edu/iiif/manifest/3bfe1c3f-eb31-4f41-9a8a-e1438adbf95d",
# "https://media.getty.edu/iiif/manifest/4f8eb4db-113e-4fb2-b5b8-e3e8a5b4dd52",
# "https://media.getty.edu/iiif/manifest/030fadcc-caa6-4472-bbde-5bbd4257c7ac",
# "https://media.getty.edu/iiif/manifest/bcad57b0-4adc-49b3-9776-8df076a3b808",
# "https://media.getty.edu/iiif/manifest/a3c5dfc6-af32-4384-9b82-01e73cba5177"]

#   for iiif in iiifs:
#     payload = {'iiifUrl': iiif}
#     try:
#         response = requests.post(url, json=payload, headers=headers)
#         response.raise_for_status()  # Raise an exception for bad status codes
#         print(f"Status Code: {response.status_code}")
#         print(f"Response JSON: {response.json()}")
#     except requests.exceptions.RequestException as e:
#         print(f"Error: {e}")

if __name__ == "__main__":
    main()