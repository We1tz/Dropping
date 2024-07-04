import uvicorn
import signal
import sys


def run_server():
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)


def signal_handler(sig, frame):
    print("Server is shutting down...")
    sys.exit(0)


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    run_server()
