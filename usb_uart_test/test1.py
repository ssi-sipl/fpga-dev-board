import serial
import time
import logging

# Configure logging
logging.basicConfig(
    filename='serial_read.log',  # Log file name
    level=logging.INFO,           # Log level
    format='%(asctime)s - %(levelname)s - %(message)s'  # Log format
)

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
    logging.info("Serial reading started.")
    
    while True:
        # Check if data is available
        if ser.in_waiting > 0:
            # Read the data
            data = ser.readline().decode('utf-8').strip()
            
            # Log the received data
            logging.info(f"Received: {data}")
        
        # Small delay to prevent high CPU usage
        time.sleep(0.1)

except KeyboardInterrupt:
    logging.info("Serial reading stopped by user")

except Exception as e:
    logging.error(f"An error occurred: {e}")

finally:
    # Close the serial connection
    ser.close()
    logging.info("Serial port closed")
