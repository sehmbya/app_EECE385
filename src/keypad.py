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

# holds a recently pressed key until it is read via get_key()
RecentKey = None
# stores the user's pin (changed with set_pin function)
UserPin = ["1", "1", "1", "1"]

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
	
# Returns true if next four key presses match user_pin, false otherwise
def enter_pin() -> bool:

	last4keys = []
	
	# record the start time for 20-second timeout
	start_t = t.time()
	
	# loop until 4 keys are received or 20 seconds pass
	while len(last4keys) < 4:
		# check if 20s have passed
		if t.time()-start_t > 20:
			print("\nTimeout reached during PIN entry.")
			return False
		
		key = get_key()
		
		if key is not None:
			last4keys.append(key)
			# print an asterisk for each keypress
			print("*", end="", flush=True)
			
	# move cursor to a new line once loop finishes
	print()
	
	# check for valid pin or not
	return last4keys == UserPin

# Overwrites user_pin with next four key presses
def set_pin() -> None:
	global UserPin
	
	newpin = []
	
	# record the start time for the 20-second timeout
	start_t = t.time()
	
	# loop until 4 keys are received or 20 seconds pass
	while len(newpin) < 4:
		# check if 20 seconds have passed
		if t.time() - start_t > 20:
			print("\nTimeout reached during PIN setup.")
			return
		
		key = get_key()
		
		if key is not None:
			newpin.append(key)
			# print an asterisk for each keypress
			print("*", end="", flush=True)
		
	# move cursor to a new line once loop finishes
	print()
	
	# save collected keys to the global variable
	UserPin = newpin


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
		#print(f"Key Found: {pressed_key}")
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
