import shlex
import subprocess  # nosec B404

def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError("Tidak boleh bagi nol")
    return a / b

def run_command(cmd):
    # Perbaikan: tanpa shell=True, perintah dipecah jadi list argumen
    args = shlex.split(cmd)
    result = subprocess.run(  # nosec B603
        args, shell=False, capture_output=True, text=True
    )
    return result.stdout