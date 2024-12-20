import serial

def main():
    # Specify the serial port and baud rate
    serial_port = '/dev/ttyUSB0'  # Replace with your port
    baud_rate = 9600

    # Open the serial connection
    try:
        with serial.Serial(serial_port, baud_rate, timeout=1) as ser:
            print("Waiting for data...")

            while True:
                # Read up to 5 bytes of data from the serial port
                raw_data = ser.read(5)  # Adjust the number of bytes expected
                if raw_data:
                    # Convert raw bytes to a list of integers
                    values = list(raw_data)
                    print("Received Raw Values:", values)  # Print as integer values
                    print("Received Bytes:", raw_data)  # Print as raw byte object
    except serial.SerialException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
