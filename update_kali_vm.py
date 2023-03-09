import os

from tkinter import messagebox

# Update and upgrade the packages
os.system("sudo apt-get update -y")
os.system("sudo apt-get upgrade -y")

# Clean up the packages
os.system("sudo apt-get autoremove -y")
os.system("sudo apt-get autoclean -y")

# Optimize the virtual machine
os.system("sudo fstrim /")

# Show a message to indicate that the update is complete
messagebox.showinfo("Update Complete", "Kali Linux VM has been updated and optimized.")
