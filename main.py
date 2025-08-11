import logging

logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

def version() -> None :
    try:
        with open("VERSION", "r") as version_file:
            print(f"Current Version : {version_file.read()}")
    except FileNotFoundError as e:
        logger.error(f" File Not Found : {str(e)}")
    except PermissionError as e:
        logger.error(f" Permission Denied : {str(e)}")
        
def main():
    version()
    
    
if __name__ == "__main__":
    main()