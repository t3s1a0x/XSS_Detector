### Advanced XSS Detector Tool

This is an advanced tool designed to test websites for potential Cross-Site Scripting (XSS) vulnerabilities. The tool supports multi-threaded payload testing and includes advanced features like progress bars, colored outputs, and graceful interruption handling.

### Features

Multi-threaded Execution: Fast payload testing using multiple threads.

Dynamic Progress Bar: Visual representation of testing progress.

Colored Output: Clearly distinguishes between various messages (errors, successes, info).

Graceful Interruption: Handles Ctrl+C to exit the program cleanly.

Detailed Reports: Outputs detailed information on detected vulnerabilities.

### Installation

Clone the repository:

git clone https://github.com/e5t3hb4r47/XXS_Detector.git
- cd XXS_Detector

### Install the required Python libraries:

pip install -r requirements.txt

### Usage

Basic Syntax

python xss_detector.py -u <URL> -p <PAYLOAD_FILE>

Arguments

-u, --url : The base URL to test. Example: https://example.com/search?q=

-p, --payload : The file containing XSS payloads to test.

Example

python xss_detector.py -u "https://example.com/search?q=" -p payloads.txt

Output Example

When running the tool, the following output is displayed:

[#] @e5t3hb4r47 [#]
[*] Loaded 50 payloads from payloads.txt
[*] Starting XSS tests...

Testing Payloads:  30%|███████▏            | 15/50 [00:01<00:03, 10.87 payload/s]

[!] XSS Vulnerability Detected!
    [+] Payload: <script>alert(1)</script>
    [+] Affected URL: https://example.com/search?q=%3Cscript%3Ealert(1)%3C%2Fscript%3E
    [+] HTTP Status Code: 200
    [+] Response Length: 14859 bytes

[!] Stopping further testing as vulnerability was detected.

### Requirements

Python 3.6+

Libraries:

requests

tqdm

colorama

Install dependencies with:

pip install -r requirements.txt

### Notes

The tool tests payloads by appending them to the base URL provided.

Make sure you have proper authorization before testing any website for vulnerabilities.

Designed for ethical security testing only.

### Disclaimer

This tool is intended for authorized security testing purposes only. Misuse of this tool can result in legal consequences. Ensure you have explicit permission to test the target website.

