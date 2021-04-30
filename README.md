# Build your own PC monitor backlight
A Python implementation to backlight your computer screen using a Raspberry Pi.

## How it works
The client code on the desktop PC constantly takes a screenshot of the current image output. 
This screenshot is then getting evaluated locally by evaluating the color values at the edges of the screenshot.
The color values are not immediately set to the new value, rather they approach fastly to the new value to create a smoother experience. 
The calculated color values are then transferred to the Raspberry Pi, which sets the leds with the new color values. 
This process is constantly repeated.

## Example
### Pictures
![Example2](img/example2.jpg)
![Example1](img/example1.jpg)

### Requirements
* PC to run the client script
* Raspberry Pi for running the server script
* Adafruit Neopixel LED strip
* Jumper Wires
* 5-12V power supply (5V GPIO on the Raspberry Pi is not recommend)

### How to use
* run the server script on you raspberry pi
* run the client script on your pc (set the ip address of your pi in the script before doing this)

### Known problems
* slight delay between the display and the backlight
* only tested on Windows

## Links
* Adafruit: https://www.adafruit.com/
* Wallpaper Source: https://www.pixelstalk.net/wp-content/uploads/2016/06/Color-Wallpapers-images-free-download-620x349.jpg

This idea has been developed within the Make2Learn and Innovate Workshop of the project Morphoa (Open Photonik Pro) 
sponsored by Federal Ministry of Education and Research of Germany (BMBF)
