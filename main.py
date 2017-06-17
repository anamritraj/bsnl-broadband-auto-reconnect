try:
    import httplib
except:
    import http.client as httplib

import time
from subprocess import Popen

# Time interval to check connection
CHECKING_INTERVAL = 5

def have_internet():
    """
    Checks if the computer has a connection to the internet.
    :return: True if there is a successful connection to google servers, False otherwise.
    """
    conn = httplib.HTTPConnection("www.google.com", timeout=5)
    try:
        conn.request("HEAD", "/")
        conn.close()
        return True
    except:
        conn.close()
        return False


def main():
    while True:
        if have_internet():
            # We have internet connection
            print("Connected!")
        else:
            p = Popen("autodial.bat")
            stdout, stderr = p.communicate()
            print(stdout)
            print(stderr)
        time.sleep(5)

if __name__ == '__main__':
    main()