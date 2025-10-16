# Python TCP Port Scanner

A lightweight TCP port scanner that identifies open ports on target hosts and logs results with timestamps and performance metrics.

## Features

- Scans TCP ports 1-1025 on any target host
- Real-time console display of open ports
- Automatic hostname to IP resolution
- logging to `Port-Scanner.txt`
- Performance tracking with start time, end time, and total duration
- Fast scanning with 0.001s timeout per port
- Error handling for invalid hostnames and connection issues

## Requirements

- Python 3.x
- Standard library only (socket, sys, datetime)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/jamesoleary203/Python-Port-Scanner.git
cd Python-Port-Scanner
```

2. No additional dependencies required

## Usage

Run the scanner:
```bash
python port_scanner.py
```

Enter target when prompted (accepts hostname or IP address):
```
Please enter host to scan: example.com
```

## How It Works

1. Resolves hostname to IP address using DNS lookup
2. Creates TCP socket connections (IPv4, `AF_INET`)
3. Tests each port in range 1-1025 with 0.001s timeout
4. Logs open ports and timing data to `Port-Scanner.txt`
5. Handles connection errors gracefully

## Output

### Console Output
```
Please enter host to scan: scanme.nmap.org
Finding Open Ports @scanme.nmap.org...
Start Time: 2025-10-16 14:30:25.123456
Port 22 Open
Port 80 Open
End Time: 2025-10-16 14:31:10.654321
Total Time: 0:00:45.530865
```

### File Output (`Port-Scanner.txt`)
```
Scanning Host: 45.33.32.156
Start Time: 2025-10-16 14:30:25.123456
Port 22 Open
Port 80 Open
End Time: 2025-10-16 14:31:10.654321
Total Time: 0:00:45.530865
```

## Technical Details

- **Protocol**: TCP (SOCK_STREAM)
- **Address Family**: IPv4 (AF_INET)
- **Port Range**: 1-1025 (well-known and registered ports)
- **Timeout**: 0.001 seconds per port for fast scanning
- **Connection Method**: `connect_ex()` returns 0 for successful connections

## Error Handling

- **Invalid Hostname**: Catches `socket.gaierror` and exits gracefully
- **Connection Errors**: Catches `socket.error` for server connectivity issues
- Provides clear error messages for troubleshooting

## Disclaimer

⚠️ **For Educational Purposes Only**

This tool is designed for learning network security concepts and ethical penetration testing. 

**Legal Notice:**
- Only scan systems you own or have explicit written permission to test
- Unauthorized port scanning may violate computer fraud laws
- Always obtain proper authorization before scanning networks
- Respect network policies and local regulations

## Future Enhancements

- [ ] Add UDP scanning support
- [ ] Implement multi-threading for faster scans
- [ ] Add service detection for open ports
- [ ] Support custom port ranges
- [ ] Add verbose/quiet mode options

## License

MIT License

## Author
James O'Leary
Cybersecurity Student | Systems Analyst
