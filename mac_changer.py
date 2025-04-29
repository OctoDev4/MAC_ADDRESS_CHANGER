import subprocess  # Importing the subprocess module to interact with system commands


import optparse  # Importing optparse to handle command-line options and arguments


import re  # Importing the re (regular expression) module for searching the MAC address


# ---


def get_arguments():
    # Creating an OptionParser object to handle command-line arguments
    parser = optparse.OptionParser()


    # ---


    # Adding an option to specify the network interface to change its MAC address
    parser.add_option("-i", "--interface", dest="interface", help="interface to change its mac address")


    # ---


    # Adding an option to specify the new MAC address that should be applied
    parser.add_option("-m", "--mac", dest="new_mac", help="new mac address")


    # ---


    # Parsing the command-line arguments
    (options, arguments) = parser.parse_args()


    # ---


    # If the interface is not specified, show an error and exit the script
    if not options.interface:
        parser.error("[-] please specify an interface, use --help for more info")


    # ---


    # If the MAC address is not specified, show an error and exit the script
    if not options.new_mac:
        parser.error("[-] please specify a mac address, use --help for more info")


    # ---


    # Returning the parsed options to be used later in the script
    return options


# ---


def change_mac(interface, new_mac):
    # Function to change the MAC address of the given network interface

    # Printing the current action of changing the MAC address
    print(f"[+] Changing MAC Address for {interface} to {new_mac}")


    # ---


    # Bringing the network interface down (disabling the interface)
    subprocess.run(["ifconfig", interface, "down"])


    # ---


    # Changing the MAC address of the interface using ifconfig
    subprocess.run(["ifconfig", interface, "hw", "ether", new_mac])


    # ---


    # Bringing the network interface up (enabling the interface again)
    subprocess.run(["ifconfig", interface, "up"])


    # ---


    # Displaying the current configuration of the network interface
    subprocess.run(["ifconfig", interface])


# ---


def get_current_mac(interface):
    # Function to fetch and return the current MAC address of the given network interface

    # Running the 'ifconfig' command to get the details of the interface
    ifconfig_result = subprocess.run(["ifconfig", interface], capture_output=True, text=True)


    # ---


    # Checking if the ifconfig command was successful by examining the return code
    if ifconfig_result.returncode != 0:
        # If the return code is not 0, it indicates an error (e.g., interface not found)
        print(f"[-] Error: interface '{interface}' not found or failed to fetch info.")
        return None  # Return None to indicate failure

    else:
        # If the ifconfig command was successful, search for the MAC address in the output
        mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result.stdout)

        # ---


        # If the MAC address is not found in the output, print an error message
        if not mac_address_search_result:
            print("[-] Could not read MAC address.")
            return None  # Return None to indicate failure

        else:
            # If a valid MAC address is found, return it as a string
            return mac_address_search_result.group(0)


# ---


# Main execution starts here


# Getting the command-line arguments for interface and new MAC address
options = get_arguments()


# Changing the MAC address of the specified interface to the new MAC address
change_mac(options.interface, options.new_mac)


# Fetching the current MAC address of the interface after the change
current_mac = get_current_mac(options.interface)

if current_mac == options.new_mac:
    print(f"the current mac is {current_mac}")
else:
    print("mac address did not get changed")

