import socket
import board
import neopixel

led_count = 20
brightness = 0.5
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
board_gpio = board.D18

# defines board with led's
pixels = neopixel.NeoPixel(board_gpio, led_count, brightness=brightness)


def server_program():
    # get the hostname
    host = ""
    port = 5000  # initiate port no above 1024

    server_socket = socket.socket()  # get instance
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        if not data:
            # if data is not received break
            break

        led_array = []
        current_string_pos = 3
        for i in range(20):
            led = []
            for n in range(3):
                # reads a rgb value for a led
                led.append(int(data[current_string_pos - 3:current_string_pos]))
                current_string_pos += 3
            led_array.append(led)
        for i in range(20):
            # sets rgb values of led's
            pixels[i] = led_array[19 - i]
    conn.close()  # close the connection
    # sets all led's to off
    pixels.fill((0, 0, 0))


if __name__ == '__main__':
    server_program()
