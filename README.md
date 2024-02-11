# Conan Classic API GraphQL

This repository contains a Python script that sends a GraphQL query to the Conan Classic API endpoint to retrieve information about a specific record.

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

- **Modifying the ID**: To retrieve information about a different record, follow these steps:
  1. Open the Python script (`coco.py`) in a text editor or an integrated development environment (IDE).
  2. Locate the `payload` dictionary within the script.
  3. Find the `"variables"` key within the `payload` dictionary.
  4. Replace the current value with the desired ID of the record you want to retrieve information about.
  5. Save the changes to the script.
  6. Run the script again using the command `coco.py`.

## Script Explanation

- The script sends a POST request to the API endpoint with the GraphQL query and retrieves the response.

## Dependencies

- [requests](https://pypi.org/project/requests/): HTTP library for sending requests easily.

## License

This project is licensed under the [MIT License](LICENSE).
