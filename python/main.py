from camera import Camera
import threading
import time

def main():
    camera = Camera()
    threads = []
    try:
        for _ in range(10):
            t = threading.Thread(target=camera.TakePhoto)
            threads.append(t)
            t.start()
            time.sleep(1) 

        for t in threads:
            t.join()
    finally:
        camera.cleanup()

if __name__ == "__main__":
    main()