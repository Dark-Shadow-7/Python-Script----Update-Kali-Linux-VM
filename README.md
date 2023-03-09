# Python-Script----Update-Kali-Linux-VM
  * A simple Python script that updates and optimizes the Kali Linux VM upon startup.

  1.  Open your Kali Linux Virtual Machine terminal.
  2.  Create a new Python script using the following command:
  
      <b>'nano update_kali-linux_vm.py'</b>
        
  3.  Add the following code to the script:
  
      ![image](https://user-images.githubusercontent.com/63378147/223884325-402b414f-865e-4c87-be1f-3f85f5203995.png)

  4.  Save the script by pressing <b>'Ctrl+X'</b>, then <b>'Y'</b>, and finally <b>'Enter'</b>.
  
  5.  Make the script executable using the following command:
  
      <b>'sudo chmod +x update_kali-linux_vm.py'</b>
        
  6.  Add the script to your startup programs by following these steps: (Example is using VMWare. Other VM managers may differ.)
  
      Click on the Kali blue button, type <b>'startup'</b> in the search bar and select <b>'Sessions and Startup'</b>
      
      ![image](https://user-images.githubusercontent.com/63378147/223885201-4ed60037-45d7-4228-8851-388f94efea08.png)
      
      Click on <b>'Application Autostart'</b> and then <b>'+Add'</b>
      
      ![image](https://user-images.githubusercontent.com/63378147/223885363-48660a54-1c91-47d6-a854-17e5fc9ee758.png)
      
      After you click <b>+Add</b>, a popup box will appear to fill out the information for the startup process.
        * Name: Here you will name your startup process
        * Description: Optional but you can describe your process here briefly
        * Command: python3 <PATH TO YOUR SCRIPT .py FILE> (I placed mine in my /usr/bin directory)
        * Trigger: on login
        * Click <b>'OK'</b> and then <b>'Close'</b>
        
        ![image](https://user-images.githubusercontent.com/63378147/223887055-bc444aba-0bce-417c-951f-868106247911.png)

  7.  Restart your virtual machine to see if the script is executed successfully at startup. If successful, you will see your customized message popup appear.
  
       *  ![image](https://user-images.githubusercontent.com/63378147/223887550-54d65467-41f6-4d5d-8483-3572980a763e.png)

Description
  * The above script will update and upgrade the packages, clean up unnecessary packages and optimize the virtual machine by using the <b>'fstrim'</b> command. To add a message to the script to pop up and notify you that the machine has been updated, we have imported the <b>'messagebox</b> module from the <b>'tkinter'</b> library, which provides a simple way to create message boxes. The <b>'showinfo'<b/> function from this module is used to create a message box with the title "Update Complete", "Kali Linux VM has been updated and optimized." The message box will pop up after the update and optimization process is complete.
  
  * Note that you may need to install the <b>'tkinter'</b> library if it is not already installed on your system. You can do this by running the following command:

    <b>'sudo apt-get install python3-tk'</b>.
    
Finally, you can modify the script according to your needs.
