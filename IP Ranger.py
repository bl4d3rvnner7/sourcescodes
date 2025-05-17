# A Function to make everything clean

def Ranger(ip: str) -> None:
    # We will use a try-except block to avoid any exceptions
    try:
        IpArray = ip.split('.')
        
        for i in range(256):  # IP Address Can only exceed upto 256
        
            # We will only range the last part of the ip , you can always increase or decrease it
            saveFileName.write(f"{IpArray[0]}.{IpArray[1]}.{IpArray[2]}.{i}\n") 
    

    except Exception:
        print(f"Invalid IP : {ip}")
            
            
            
fileName = input("[+] Your IP List :") # User will input the filename first


with open(fileName, errors="ignore", encoding="utf8") as baseFile:  # We use context manager

    IpList = list(dict.fromkeys(baseFile.readlines()))   # For removing duplicates
    
    saveFileName = open("IP Range.txt", "a") # We will create a new file Names IP Ranges to save those ranges
    
    # We will iterate through the list
    
    for ip in IpList:
        Ranger(ip)
        print(f"Completed : {ip}")  # Finally we will print the status as its completed