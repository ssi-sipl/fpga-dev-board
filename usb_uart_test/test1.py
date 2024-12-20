import serial
import time

# Set up the serial connection
serial_port = '/dev/ttyUSB0'  # Change this if your device is on a different port
baud_rate = 115200  # Make sure this matches the baud rate set on the ESP32-C3
timeout = 1  # Timeout for read operation

try:
    # Create a serial connection
    with serial.Serial(serial_port, baud_rate, timeout=timeout) as ser:
        print(f"Connected to {serial_port} at {baud_rate} baud rate.")

        # Allow some time for the connection to establish
        time.sleep(2)

        while True:
            # Read a line from the serial port
            if ser.in_waiting > 0:  # Check if data is available
                line = ser.readline().decode('utf-8').rstrip()  # Read and decode the line
                print(f"Received: {line}")  # Print the received line

except serial.SerialException as e:
    print(f"Error: {e}")
except KeyboardInterrupt:
    print("Exiting the program.")