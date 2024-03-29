import importlib
import subprocess
import sys

def install_package(package_name):
    """
    Install a Python package if it's not already installed.

    Args:
        package_name (str): The name of the package to install.
    """
    try:
        
        importlib.import_module(package_name)
    except ImportError:
        print(f"Installing {package_name}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package_name], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    else:
        print(f"{package_name} is already installed.")

def uninstall_package(package_name):
    """
    Uninstall a Python package if it's installed.

    Args:
        package_name (str): The name of the package to uninstall.
    """
    try:
        importlib.import_module(package_name)
    except ImportError:
        print(f"{package_name} is not installed.")
    else:
        print(f"Uninstalling {package_name}...")
        subprocess.check_call([sys.executable, "-m", "pip", "uninstall", package_name, "-y"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"{package_name} has been uninstalled.")

if __name__ == "__main__":
    required_module = "public_ip"

    # Check if the required module is already imported
    if required_module not in sys.modules:
        install_package(required_module)

    # Now you can safely import and use the module
    import public_ip as ip
    public_ip_address = ip.get()
    print(f"Public IP Address: {public_ip_address}")

    if required_module in sys.modules:
        uninstall_package(required_module)
