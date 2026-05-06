from gpiozero import DigitalOutputDevice, Button
import time as t 

#GPIO Pinout Reference
#{ top		row0: 26 }
#{			row1: 19 }
#{			row2: 13 }
#{ bot		row3: 06 }

#{ left		col0: 05 }
#{			col1: 00 }
#{			col2: 11 }
#{ right	col3: 09 }

# mapping GPIO pins to rows and columns
row_pins = [26, 19, 13, 6]
col_pins = [5, 0, 11, 9]

# keypad mapping
key_map = [
	["1", "2", "3", "A"],
	["4", "5", "6", "B"],
	["7", "8", "9", "C"],
	["*", "0", "#", "D"]
]

# holds a recently pressed key until it is passed to main via get_key()
RecentKey = None

## PUBLIC FUNCTIONS ##

# Initialize keypad with interrupts #
def keypadInit():
	# declare global list variables for keypad rows and columns
	global rows, cols
	# set up rows as outputs and columns as inputs (buttons)
	rows = [DigitalOutputDevice(pin) for pin in row_pins]
	cols = [Button(pin, pull_up=False) for pin in col_pins]
	set_rows_high()	# keypad becomes idle, waiting for press
	# assign interrupt callback for each column interrupt
	for col in cols:
		col.when_pressed = keyscan
	print("Keypad ready. Waiting for a press...")

# Returns most recently pressed key or 'None' if no recent keypresses
def get_key() -> str:
	global RecentKey
	temp_key = RecentKey
	RecentKey = None
	return temp_key

## END PUBLIC FUNCTIONS ##

## PRIVATE FUNCTIONS ##

# Interrupt callback triggered when any column goes high #
def keyscan():
	global RecentKey
	# disable interrupts on all columns to prevent duplicate presses
	for col in cols:
		col.when_pressed = None
	
	# reset pressed_key variable
	pressed_key = None
	
	# enter scanning algorithm to locate pressed key
	for i, row in enumerate(rows):	# set one row HIGH at a time
		for r in rows: r.off()		# set all rows LOW
		row.on()					# set a single row HIGH
		# check each column for pressed key
		for j, col in enumerate(cols):
			if col.is_pressed:
				# pressed key is found, save it
				pressed_key = key_map[i][j]
				break	# no need to check other columns
		# if pressed key is found, no need to check other rows either
		if pressed_key: break
			
	if pressed_key:
		print(f"Key Found: {pressed_key}")
		RecentKey = pressed_key
		# wait for release to prevent duplicate presses
		while any(c.is_pressed for c in cols):
			t.sleep(0.01)
	
	# reset keypad to idle
	set_rows_high()
	# reenable interrupt to wait for next press
	for col in cols:
		col.when_pressed = keyscan
	
def set_rows_high():
	for row in rows: row.on()        

## END PRIVATE FUNCTIONS ##
