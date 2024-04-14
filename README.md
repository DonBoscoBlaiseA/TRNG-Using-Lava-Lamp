## True Random Number Generator(TRNG) using Lava Lamp

## Algorithm:
  1. Start.
  2. Import open cv(for computer vision) and hashlib(for encryption).
  3. Read a video of lava lamp using open cv.
  4. Convert the colourised video to grayscale using open cv.
  5. Convert each frame of the grayscale video into bytes object using PIL.
  6. Convert the bytes object into hash values using hashlib.
  7. Convert the hash values to Hexadecimal value.
  8. Using open cv display the colourised and grayscale videos on a window.
  9. Using a loop print the hexadecimal value for each frame of the video.
  10. Release the memory allocated to the video and destroy all windows.
  11. End.

## About TRNG:
```
True Random Number Generator is a method that generates random numbers based on
a physical process or phenomenon that is inherently unpredictable. Unlike
pseudorandom number generators (PRNGs), which use deterministic algorithms to
produce sequences of numbers that appear random, TRNGs produce numbers that are
truly random and not influenced by any external factors.

Why use lava lamps for encryption?
	Computers can only generate numbers that appear random, but are
actually generated using mathematical formulas. These are called
“pseudo-random” numbers.

Computers run on logic. A computer program is based on if-then statements:
If certain conditions are met, then perform this specified action.
The same input into a program results in the same output every time.

Computers are only useful because of their reliability and predictability.
However, that predictability is a liability when it comes to generating
secure encryption keys.

	This is a major deal breaker for encrypting data, since each
new key that the computer generates must be truly random, so that
hackers won't be able to figure out the key and decrypt the data.

	So, we are in need of a truly random source to generate truly
random encryption code. This is the reason we are using lava lamps,
since the lava inside the lava lamp doesn't take the same shape twice,
thus becoming a great source for randomness.
```
![image](https://github.com/DonBoscoBlaiseA/TRNG-Using-Lava-Lamp/assets/140850829/0f0ffae3-3f17-4a3f-b66f-e32d18cfccd2)
