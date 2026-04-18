import sys
import time as t
from datetime import  datetime 

def main():
    current_time = datetime.now()
    print("385App Initialized!!!")

    #testing output continuously... print time every 5 seconds
    while True:
        print(f"current time in EST is: { current_time }")

        #output to logs for testing 
        sys.stdout.flush()

        t.sleep(5) 

if __name__ == "__main__":
    main()
