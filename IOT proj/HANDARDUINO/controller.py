import pyfirmata2

# Define the serial port and initialize the board
comport = 'COM4'
board = pyfirmata2.Arduino(comport)

# Define the pins for the servos
st = board.get_pin('d:3:s')  # Example pin for servo 1
si = board.get_pin('d:5:s')  # Example pin for servo 2
sm = board.get_pin('d:6:s')  # Example pin for servo 3
sr = board.get_pin('d:7:s')  # Example pin for servo 4
sp = board.get_pin('d:9:s')  # Example pin for servo 5

def led(fingerUp):
    # Control each servo based on the fingerUp input
    if fingerUp[0] == 1:
        st.write(180)  # Move servo 1 to 180 degrees
    else:
        st.write(0)    # Move servo 1 to 0 degrees

    if fingerUp[1] == 1:
        si.write(180)  # Move servo 2 to 180 degrees
    else:
        si.write(0)    # Move servo 2 to 0 degrees

    if fingerUp[2] == 1:
        sm.write(180)  # Move servo 3 to 180 degrees
    else:
        sm.write(0)    # Move servo 3 to 0 degrees

    if fingerUp[3] == 1:
        sr.write(180)  # Move servo 4 to 180 degrees
    else:
        sr.write(0)    # Move servo 4 to 0 degrees

    if fingerUp[4] == 1:
        sp.write(180)  # Move servo 5 to 180 degrees
    else:
        sp.write(0)    # Move servo 5 to 0 degrees
