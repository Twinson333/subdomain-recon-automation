#  Tamarin Sub-Recon

A simple Python-based automation script to discover and probe active subdomains for any target domain.  
It uses tools like **subfinder**, **haktrails**, **assetfinder**, and **httpx** to gather, merge, filter, and identify live subdomains.

> ⚠️ **Disclaimer:** This tool is intended for educational and authorized security testing only. Do **not** use it on domains you don't own or have permission to test.

---

##  Features

-  Collects subdomains from multiple sources  
-  Removes duplicates and sorts results  
-  Probes for live subdomains using `httpx`  
-  Cleans temporary files after execution  
-  Saves results to `activesubs.txt`  

---

##  Requirements

Ensure the following tools are installed and available in your terminal (`$PATH`):

| Tool         | Purpose                      |
|--------------|------------------------------|
| `subfinder`  | Subdomain enumeration        |
| `haktrails`  | Subdomain gathering via APIs |
| `assetfinder`| Asset discovery              |
| `httpx`      | Probe for live subdomains    |
| `python3`    | To run the script            |

You can install them using:
```
# Example (Go-based tools)
go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
go install -v github.com/hakluke/haktrails@latest
go install -v github.com/tomnomnom/assetfinder@latest
go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest
```
## Usage

Run the script using: ```python3 subrecon.py```     
Then enter your target domain when prompted: ```Enter your domain name:``` `example.com`    

## Output:

- `activesubs.txt` — contains all active/live subdomains

- Temporary files (`subf.txt`, `haksubs.txt`, `asset.txt`, `subdomains.txt`) are automatically deleted

## What the Script Does

1. Runs subfinder → saves results to subf.txt
2. Runs haktrails → saves results to haksubs.txt
3. Runs assetfinder → saves results to asset.txt
4. Merges & removes duplicates → subdomains.txt
5. Probes with httpx → live subdomains saved to activesubs.txt
6. Deletes all intermediate files
