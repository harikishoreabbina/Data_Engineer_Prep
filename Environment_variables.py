#ENVIRAONMENTAL VARIABLES
# they store the value outside the code
# it improves the security and flexibility

import os

def main():
    folder = os.getenv("DATA_FOLDER")
    print(folder)
    
if __name__ == "__main__":
    main()
    
# putting everthing in the main function will improve the :
# organized code,
# makes code more maintainable and reusable

# Settings like file path should be kept outside the code using environment variables
# SO we can change the path without editing the code, improves flexibility.