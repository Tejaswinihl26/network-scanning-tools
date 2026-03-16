import subprocess
import re

def scan_arp():
    print("=== ARP Scanner ===")

    try:
        result = subprocess.run(
            ["arp", "-a"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        output = result.stdout

        pattern = r'(\d+\.\d+\.\d+\.\d+).*?(([0-9a-f]{2}:){5}[0-9a-f]{2})'

        matches = re.findall(pattern, output, re.I)

        print("\nIP Address\t\tMAC Address")
        print("-------------------------------------")

        count = 0

        for match in matches:
            print(match[0], "\t", match[1])
            count += 1

        print("\nTotal entries:", count)

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    scan_arp()
