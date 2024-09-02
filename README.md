# VartaStorageServer
A simple Flask server for displaying VartaStorage data via Modbus using the VartaStorage python module

## Features

- Fetches and displays data from Varta Storage devices
- Uses Modbus protocol for communication
- Built with Flask for a lightweight web interface that displays data in json format

## Requirements

- Python 3.x
- Flask
- VartaStorage pip module

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/vartastorage-server.git
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Setup

Before running the server, make sure to update the IP address, username, and password in the script. 

## Usage

1. Start the Flask server:

    ```bash
    python app.py
    ```

2. Open a web browser and navigate to `http://localhost:5000` to view the VartaStorage data.

## Notes

- Ensure that the VartaStorage device is connected and accessible via the provided IP address.
- Modify the Flask route handlers as needed to customize data display.

## Credits

- **VartaStorage Python module**: This project uses the `VartaStorage` Python module created by Vip0r. You can find the module and its documentation on [GitHub](https://github.com/Vip0r/vartastorage).

- **Flask Framework**: This server is built using the [Flask](https://github.com/pallets/flask) framework for Python.

- **Modbus Protocol**: Communication with the VartaStorage devices is handled using the Modbus protocol.

## License

This project is licensed under MIT License


