import subprocess
import shutil

def check_nmap():
    if shutil.which("nmap"):
        print("Nmap is installed")
        return True
    else:
        print("Nmap is not installed")
        return False

def run_scan(target, option):

    if option == "1":
        cmd = ["nmap", "-sn", target]

    elif option == "2":
        cmd = ["nmap", target]

    elif option == "3":
        cmd = ["nmap", "-sV", target]

    else:
        print("Invalid choice")
        return

    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        print("\nScan Results:\n")
        print(result.stdout)

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":

    print("=== Nmap Scanner ===")

    if check_nmap():

        target = input("Enter target IP: ")

        print("\nSelect scan type")
        print("1. Host Discovery")
        print("2. Port Scan")
        print("3. Service Version Detection")

        choice = input("Enter choice: ")

        run_scan(target, choice)
