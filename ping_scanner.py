import subprocess
import platform
import re

def ping_host(host):
    os_type = platform.system().lower()

    if os_type == "windows":
        param = "-n"
    else:
        param = "-c"

    try:
        result = subprocess.run(
            ["ping", param, "4", host],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=10
        )

        output = result.stdout

        if result.returncode == 0:
            print(f"\nHost {host} is Reachable")

            match = re.search(r'avg[/=](\d+\.?\d*)', output)
            if match:
                print("Average Time:", match.group(1), "ms")
        else:
            print(f"\nHost {host} is Unreachable")

    except subprocess.TimeoutExpired:
        print("Ping request timed out")


if __name__ == "__main__":
    print("=== Ping Scanner ===")
    host = input("Enter IP or hostname: ")
    ping_host(host)
