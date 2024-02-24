import zmq
import time
from decoder.gomspace import NanoComAX100

# TODO: make length calc dynamic using pmt (not working currently bc of a bug)
# https://github.com/gnuradio/gnuradio/issues/6967

def main():
    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    socket.connect("tcp://127.0.0.1:5555")
    socket.setsockopt(zmq.SUBSCRIBE, b'')
    
    print("Started ZMQ")

    while True:
        if socket.poll(10) != 0:
            data = socket.recv()[10:]
            csp = NanoComAX100.decode_frame(data)
            print(csp)
        else:
            time.sleep(0.1)

if __name__ == "__main__":
    main()

