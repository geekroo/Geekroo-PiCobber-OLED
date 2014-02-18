#!/usr/bin/python
from Raspi_MCP230xx import Raspi_MCP230XX
import time
import sys
import ssd1306
import time
import sys

# ============================================================================
# Example Code
# ============================================================================    

# ----------------------------------------------------------------------
mcp = Raspi_MCP230XX(address = 0x20, num_gpios = 8)
	
# Set pins 0, 1 and 2 to output (you can set pins 0..15 this way)

#SW1
mcp.config(0,mcp.INPUT)
#mcp.pullup(0, 1)
#SW2
mcp.config(1,mcp.INPUT)
#SW3
mcp.config(2,mcp.INPUT)
#SW4
mcp.config(3,mcp.INPUT)
#SW5
mcp.config(4,mcp.INPUT)
#SW6
mcp.config(5,mcp.INPUT)
#LED
mcp.config(6,mcp.OUTPUT)


mcp.output(6, 1)  # LED OUTPUT Low
# ----------------------------------------------------------------------
led = ssd1306.SSD1306()
led.begin()
led.clear_display()

offset = 0 # flips between 0 and 32 for double buffering
# ----------------------------------------------------------------------


while True:
    if(mcp.input(1) >> 1):  # Read input SW2 and SET LED
    	mcp.output(6, 1)  # LED OUTPUT Low
    else:
	mcp.output(6, 0)  # LED OUTPUT High	
	
    # write the current time to the display on every other cycle
    if offset == 0:
        text = time.strftime("%A")
        led.draw_text2(0,0,text,2)
        text = time.strftime("%e %b %Y")
        led.draw_text2(0,16,text,2)
        text = time.strftime("%X")
        led.draw_text2(0,32+4,text,3)
        led.display()
        time.sleep(0.2)
    else:
        time.sleep(0.5)
        
    # vertically scroll to switch between buffers
    for i in range(0,32):
        offset = (offset + 1) % 64
        led.command(led.SET_START_LINE | offset)
        time.sleep(0.01)
