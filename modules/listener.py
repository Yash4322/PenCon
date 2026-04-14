import subprocess


def start_listener(port):
    print(f"[+] Starting listener on port {port}")
    subprocess.run(["nc", "-lvnp", port])
