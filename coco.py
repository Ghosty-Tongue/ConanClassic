import requests
import json

url = "https://conanclassic.com/api/legacy/graphql"
headers = {"Content-Type": "application/json"}
payload = {
    "query": "query findRecord($ID: ID!){findRecord(id: $ID){id title teaser publishOn version masterSite airDate isLive videoType duration thumb {id found name path mime url title timestamp description status preview version type flags data token storageUri alt}} findRecordVideoMetadata(id: $ID) {src videoType}}",
    "variables": {"ID": "74709"}
}

response = requests.post(url, json=payload, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Parse JSON response
    response_data = response.json()
    # Pretty print the response
    print(json.dumps(response_data, indent=3))
else:
    print("Error:", response.status_code)
