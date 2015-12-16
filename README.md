# tweety-blink
Neat little script that will cause the RPi to blink whenever a tweet containing a word is published

## authentication
You must add your own twitter developer authentication credentials into an 'auth.json' file. A template is included in the project. 'c-key' stands for Client Key and 'a-token' stands for Access Token. These can all be obtained by creating a Twitter developer account and by registering an application.

## Schematic
Credit to "fritzing" for providing a schematic for the LED's
![alt text](https://raw.githubusercontent.com/geerlingguy/raspberry-pi-dramble/master/images/rgb-led-wiring.jpg "Schematic")

## Search terms
To change the search terms, modify the search_terms array in "tweety-blink.py" to fit whatever your heart desires

## TODO
- Pass search keywords through command line args
- Catch keyboard interrupts better
- Make classier