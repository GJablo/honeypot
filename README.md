# Terminal-Based Honeypot

A Python-based honeypot that simulates a fake login prompt to detect and log unauthorized access attempts.

## Features
- Displays a fake login prompt in the terminal.
- Logs all inputs (username and password) along with:
  - Attacker's IP address.
  - Geolocation (city and country) derived from the IP.
  - Timestamp of the attempt.
  - User-Agent (simulated as "Terminal Honeypot").
- Responds with "Login failed: Invalid credentials" to encourage repeated attempts.
- Exits only if the attacker types "exit" as the username.
- Logs attempts to `honeypot_log.txt`.

## Requirements
- Python 3.x
- External libraries: `requests` (for IP and geolocation lookup)

## Installation
1. Clone or download the repository.
2. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the script:
```bash
python honeypot.py
```

## Output

Each log entry is saved in the following format

- `[YYYY-MM-DD HH:MM:SS] IP:<ip_address> | Location:<city, country> | User-Agent:<system info> | Username:<entered_username> | Password:<entered_password>
`

## Key Considerations

- Do not expose on production systems without proper safeguards

### How It Works
1. **Fake Login Prompt**: The script displays a fake username and password prompt in the terminal.
2. **IP Capture**: It fetches the public IP of the machine running the honeypot (or defaults to `127.0.0.1` if offline).
3. **Geolocation Lookup**: Uses `ipinfo.io` to derive the city and country from the IP.
4. **Logging**: All attempts are logged to `honeypot_log.txt` with timestamps, IP, location, and credentials.
5. **Behavior**: Responds with "Login failed" to encourage repeated attempts and exits only on the "exit" command.

### Caution

- This is a simulation tool for educational purposes only!
