import serial
i = raw_input("Enter the port no.")
port = serial.Serial("/dev/ttyUSB" + i, baudrate=9600, timeout=10.0)

line = []
print("connected to: " + port.portstr)

while True:
    try:
        rcv = port.read()
    except:
        rcv = ''
    line.append(rcv)

    if rcv == '\n':
        line = "".join(line)
        print line
        line = []