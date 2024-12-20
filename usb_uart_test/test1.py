import serial

def main():
    # Specify the serial port and baud rate
    # Update '/dev/ttyUSB0' to the correct port if necessary
    serial_port = '/dev/ttyUSB0'  # Replace with your port
    baud_rate = 9600

    # Open the serial connection
    try:
        with serial.Serial(serial_port, baud_rate, timeout=1) as ser:
            print("Waiting for data...")

            while True:
                # Read data from the serial port
                data = ser.readline().decode('utf-8').strip()
                if data:
                    print(f"Received: {data}")
    except serial.SerialException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
