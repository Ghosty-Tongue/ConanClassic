# Conan Classic API GraphQL

This repository contains a Python script that sends a GraphQL query to the Conan Classic API endpoint to retrieve information about a specific episode/clip.

## Usage

1. Install the necessary dependencies:

```
pip install requests
```

2. Run the script:

```
python coco.py
```

## Important Note

- **Do Not Modify Payload or URL**: It's crucial not to alter the payload and URL provided in the script. Here's why:
  - **Payload**: The payload contains the GraphQL query specifying what data to request from the API. Changing it could result in the API not understanding the request or returning unexpected results.
  - **URL**: The URL points to the specific endpoint of the Conan Classic API. Changing it could lead to the request being sent to the wrong API endpoint or server, causing errors or failure to retrieve data.

- **Modifying the ID**: To retrieve information about a different episode/clip, follow these steps:
  1. Open the Python script (`coco.py`) in a text editor or an integrated development environment (IDE).
  2. Locate the `payload` dictionary within the script.
  3. Find the `"variables"` key within the `payload` dictionary.
  4. Replace the current value with the desired ID of the episode/clip you want to retrieve information about.
  5. Save the changes to the script.
  6. Run the script again using the command `coco.py`
 
# Response Structure
The response from the Conan Classic API contains important information about the requested record. Here are the key components and keys included

`Title`: Provides the title of the record, giving a brief description of its content.

`Teaser`: Offers a short summary or description of the content associated with the record.Duration: Indicates the duration of the associated video.

`Thumbnail`: Contains information about the thumbnail image associated with the record, including its URL.

`Video Source`: Provides metadata about the video associated with the record, including the URL(s) for streaming.

## Script Explanation

- The script sends a POST request to the API endpoint with the GraphQL query and retrieves the response.

## Dependencies

- [requests](https://pypi.org/project/requests/): HTTP library for sending requests easily.

## License

This project is licensed under the [MIT License](LICENSE).
