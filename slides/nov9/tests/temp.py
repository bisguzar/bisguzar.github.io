from http.client import HTTPSConnection
from threading import Thread

def do_request(target: str):
    session = HTTPSConnection(target)
    session.request('GET', '/')
    print('ok')
    return session.getresponse()

if __name__ == "__main__":
    while True:
        thread = Thread(
            target=do_request, 
            args=('google.com',)
            )

        thread.start()
