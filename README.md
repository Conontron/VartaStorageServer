# VartaStorageServer
A simple Flask server for displaying VartaStorage data via Modbus using the VartaStorage python module
# VartaStorage Data Display Server

A simple Flask server that displays data from VartaStorage devices. It connects via Modbus and processes the data using the `vartastorage` Python module.

## Features

- Fetches and displays data from Varta Storage devices
- Uses Modbus protocol for communication
- Built with Flask for a lightweight web interface

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

## Credits Python module
VartaStorage python module by Vip0r [https://github.com/Vip0r/vartastorage]


