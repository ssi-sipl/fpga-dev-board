import serial
import time

# Configure the serial connection
ser = serial.Serial(
    port='/dev/ttyUSB0',  # USB-UART port
    baudrate=115200,      # Match the baudrate of your device
    bytesize=serial.EIGHTBITS,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    timeout=1             # Read timeout in seconds
)

try:
    while True:
        # Check if data is available
        if ser.in_waiting > 0:
            # Read the data
            data = ser.readline().decode('utf-8').strip()
            
            # Print the received data
            print(f"Received: {data}")
        
        # Small delay to prevent high CPU usage
        time.sleep(0.1)

except KeyboardInterrupt:
    print("Serial reading stopped by user")

finally:
    # Close the serial connection
    ser.close()
    print("Serial port closed")
