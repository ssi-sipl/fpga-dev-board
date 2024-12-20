import serial

def main():
    # Specify the serial port and baud rate
    serial_port = '/dev/ttyUSB0'  # Replace with your port
    baud_rate = 115200

    # Open the serial connection
    try:
        with serial.Serial(serial_port, baud_rate, timeout=1) as ser:
            print("Waiting for data...")

            while True:
                # Read a line of text from the serial port
                line = ser.readline().decode('utf-8').strip()  # Decode and remove trailing whitespace
                if line:
                    print(f"Received: {line}")
    except serial.SerialException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
