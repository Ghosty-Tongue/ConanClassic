import requests

url = "https://conanclassic.com/api/legacy/graphql"
headers = {"Content-Type": "application/json"}
payload = {
    "query": "query findRecord($ID: ID!){findRecord(id: $ID){id title teaser publishOn version masterSite airDate isLive videoType duration thumb {id found name path mime url title timestamp description status preview version type flags data token storageUri alt}} findRecordVideoMetadata(id: $ID) {src videoType}}",
    "variables": {"ID": "74709"}
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
