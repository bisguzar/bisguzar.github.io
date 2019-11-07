from requests import get

def request(target: str):
    return get(target)



from time import time

if __name__ == "__main__":
    started_time = time()
    counter = 0

    while (time() - started_time) < 30:
        response = request('https://google.com')
        if response:
            counter += 1

    print("Totally count: "+ str(counter))

