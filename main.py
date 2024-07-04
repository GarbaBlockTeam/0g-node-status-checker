import requests

def check_0g_node_status(node_url):
    try:
        response = requests.get(node_url)
        response.raise_for_status()
        # Assuming the API returns JSON with a 'status' key
        status = response.json().get('status', 'Status not found')
        print(f"0g node status: {status}")
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")

# Replace 'your_0g_node_api_url' with the actual URL of your 0g node API
check_0g_node_status('your_0g_node_api_url')
