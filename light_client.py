import socket
import pyautogui

screen = None


def clamp(n, m, value):
    return min(m, max(value, n))


def get_rgb_as_string(rgb_color):
    rgb_as_string = ""
    rgb_as_string += "%03d" % rgb_color[0]
    rgb_as_string += "%03d" % rgb_color[1]
    rgb_as_string += "%03d" % rgb_color[2]
    return rgb_as_string


def get_pixel_colour(x, y, w, h, steps):
    """
    defines a rectangle
    x,y:mid of rectangle
    w,h:size
    """
    global screen
    rgb_average = [0, 0, 0]
    # loops trough the rectangle while checking pixel rgb values
    for current_x in range(0, w, steps):
        for current_y in range(0, h, steps):
            pixel_rgb = screen.getpixel((x + current_x, y + current_y))
            rgb_average[0] += pixel_rgb[0]
            rgb_average[1] += pixel_rgb[1]
            rgb_average[2] += pixel_rgb[2]
    rgb_average[0] = round(rgb_average[0] / (w * h) * steps * steps)
    rgb_average[1] = round(rgb_average[1] / (w * h) * steps * steps)
    rgb_average[2] = round(rgb_average[2] / (w * h) * steps * steps)
    return rgb_average


def client_program():
    global screen
    # 192.0.2.0
    host = "192.168.2.120"
    port = 5000  # socket server port number
    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    screen_width = 1920
    screen_height = 1080

    led_left = 5
    led_top = 10
    led_right = 5

    led_current_colour = []
    led_target_colour = []

    for i in range(20):
        led_current_colour.append([0, 0, 0])
        led_target_colour.append((0, 0, 0))

    while True:
        screen = pyautogui.screenshot()  # take a screenshot of the screen
        led_string = ""

        # left led's
        # gets the rgb values for all led's on the left side
        current_led_y = screen_height
        left_spacing = round(screen_height / led_left)
        for n in range(led_left):
            current_led_y -= left_spacing
            led_target_colour[n] = get_pixel_colour(screen_width - 100, current_led_y, 100, left_spacing, 5)

        # top led's
        # gets the rgb values for all led's on the top side
        current_led_x = screen_width - (screen_width / led_left) / 2
        for n in range(led_left, led_left + led_top):
            led_target_colour[n] = get_pixel_colour(current_led_x, 100, 20, 20, 5)
            current_led_x -= screen_width / led_top

        # right led's
        # gets the rgb values for all led's on the right side
        current_led_y = 0
        right_spacing = round(screen_height / led_right)
        for n in range(led_left + led_top, led_left + led_top + led_right):
            led_target_colour[n] = get_pixel_colour(0, current_led_y, 100, right_spacing, 5)
            current_led_y += right_spacing

        for n in range(20):
            # slowly fades light to the target color
            led_current_colour[n][0] += round((led_target_colour[n][0] - led_current_colour[n][0]) / 3)
            led_current_colour[n][1] += round((led_target_colour[n][1] - led_current_colour[n][1]) / 3)
            led_current_colour[n][2] += round((led_target_colour[n][2] - led_current_colour[n][2]) / 3)

            # clamps the color values in a range of 0-255
            led_current_colour[n][0] = clamp(0, 255, led_current_colour[n][0])
            led_current_colour[n][1] = clamp(0, 255, led_current_colour[n][1])
            led_current_colour[n][2] = clamp(0, 255, led_current_colour[n][2])

            led_string += get_rgb_as_string(led_current_colour[n])

        client_socket.send(led_string.encode())  # send message


if __name__ == '__main__':
    client_program()
