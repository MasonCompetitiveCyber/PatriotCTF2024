import requests

# Server IP
server_ip = 'http://167.99.12.253'


# Function to read binary strings from a file
def read_binary_strings(file_path):
    with open(file_path, 'r') as file:
        binary_strings = [line.strip() for line in file]
    return binary_strings


def binary_to_hex(binary_str):
    """Convert an 8-bit binary string to a two-digit hexadecimal string."""
    hex_str = hex(int(binary_str, 2))[2:].zfill(2)
    return hex_str


def send_post_requests(server_ip, binary_strings):
    for binary_str in binary_strings:
        # Convert binary string to hex
        hex_str = binary_to_hex(binary_str)

        # Construct the URL
        url = f"{server_ip}/{hex_str}"

        # Send the POST request
        requests.post(url, data=binary_str)


# Read binary strings from the file
file_path = 'testoutput.txt'  # Replace with your file path
binary_strings = read_binary_strings(file_path)

# Run the function
send_post_requests(server_ip, binary_strings)
