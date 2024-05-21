import serial
import time

# Initialize the serial port
ser = serial.Serial(
    port='/dev/ttyUSB1',  # Your port name may vary
    baudrate=9600,
    parity=serial.PARITY_ODD,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.SEVENBITS,
    timeout=1
)

def send_command(command):
    """
    Send a command to the instrument and read the response if it is a query.
    """
    # Append carriage return and line feed as terminators
    terminators = '\r\n'
    full_command = command.upper() + terminators
    
    # Send command to instrument
    ser.write(full_command.encode())
    
    # If the command is a query, read the response
    if '?' in command:
        response = read_response()
        return response
    return None

def read_response():
    """
    Read the response from the instrument until terminators are encountered.
    """
    response = ''
    while True:
        char = ser.read().decode()
        response += char
        if response.endswith('\r\n'):
            break
    return response.strip()

def main():
    while True:
        command = input("Enter command (or type 'EXIT' to quit): ")
        if command.upper() == "EXIT":
            break
        response = send_command(command)
        if response is not None:
            print(f"Response: {response}")

if __name__ == "__main__":
    main()
