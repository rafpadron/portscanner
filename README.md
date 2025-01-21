# Simple Port Scanner

This is a simple port scanner written in Python that allows you to scan a range of ports on a specific IP address. It also includes an option to scan only common ports and retrieve banners from services running on open ports.

## Requirements

- Python 3.x

## Installation

1. Clone this repository or download the `main.py` file.
2. Ensure you have Python 3.x installed on your system.

## Usage

To run the port scanner, open a terminal and navigate to the directory where `main.py` is located. Then, execute the following command:

```sh
python main.py <IP_ADDRESS> [OPTIONS]

Arguments
<IP_ADDRESS>: The IP address you want to scan.
Options
-p, --ports: Range of ports to scan (default is 1-65535). Example: -p 1-1024.
-t, --threads: Number of threads to use (default is 100). Example: -t 50.
-c, --common: Scan only common ports.
