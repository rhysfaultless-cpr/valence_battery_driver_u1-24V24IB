import can

def send_one():
    with can.Bus(interface='socketcan', channel='can0', bitrate=250000) as bus:
        msg = can.Message(
            arbitration_id=0x18920140, data=[0, 0, 0, 0, 0, 0, 0, 0], is_extended_id=True
        )
        
        try:
            bus.send(msg)
            print(f"Message sent on {bus.channel_info}")
        except can.CanError:
            print("Message NOT sent")

if __name__ == "__main__":
    send_one()
