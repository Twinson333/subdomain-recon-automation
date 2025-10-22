import subprocess
import os

def run_command(command, shell=True):
    try:
        subprocess.run(command, shell=shell, check=True)
    except subprocess.CalledProcessError:
        print(f"Error while running: {command}")
        exit(1)

def main():
    domain = input("Enter your domain name: ").strip()

    print("[+] Running subfinder...")
    run_command(f"subfinder -d {domain} -o subf.txt -silent")

    print("[+] Running haktrails...")
    run_command(f'echo "{domain}" | haktrails subdomains > haksubs.txt')

    print("[+] Running assetfinder...")
    run_command(f"assetfinder --subs-only {domain} > asset.txt")

    print("[+] Combining and sorting subdomains...")
    run_command("cat subf.txt haksubs.txt asset.txt | sort -u > subdomains.txt")

    print("[+] Probing active subdomains using httpx...")
    run_command("httpx -l subdomains.txt -o activesubs.txt -threads 200 -silent")

    # Cleanup temporary files
    for filename in ["subf.txt", "haksubs.txt", "asset.txt", "subdomains.txt"]:
        if os.path.exists(filename):
            os.remove(filename)

    print("\nAll the commands were executed successfully!")
    print("Output saved to: activesubs.txt")

if __name__ == "__main__":
    main()
