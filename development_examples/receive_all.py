import can
from can.bus import BusState

def receive_all():
    with can.Bus(interface='socketcan', channel='can0', bitrate=250000) as bus:
        try:
            bus.state = BusState.PASSIVE
        except NotImplementedError:
            pass

        try:
            while True:
                msg = bus.recv(1)
                if msg is not None:
                    print(msg)

        except KeyboardInterrupt:
            pass  # exit normally

if __name__ == "__main__":
    receive_all()
