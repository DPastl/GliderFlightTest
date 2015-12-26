# GliderFlightTest
A python exam generator to aid in studying for Canadian Glider Pilots Exams.  Two interfaces are available: the standard
command line interface or a simple python GUI.  The GUI was designed with Tkinter and requires no external packages to
run.  Both interfaces work the same and will create the same tests.

## Usage
### Unix and Linux Systems
The exam generator can be easily be run by simply running the main.py script:
```
python main.py
```

### Windows
Currently, to run in windows you must first install python.  Navigate to https://www.python.org/downloads/ and download
python, then click the installer and install python.  Download the repository files for this project by clicking
"Download zip" above.  The main.py file can then be run by double clicking the file.  
A Compiled Windows executable is planned but not yet implemented (the developers don't actually have windows computers).

## Example
Below is an example of the command line exam interface.

```
Question Number 1
An airplane flying at 10,000 feet ASL in the Altimeter Setting Region should have its altimeter set to
1) the altimeter setting of th aerodrome of the departure
2) the altimeter setting of the aerodrome of intended landing
3) 29.92 inches of mercury
4) the altimeter setting of the nearest aerodrome
Answer: 
```

## Databases
The databases are based on questions from sample examinations for glider examinations and from private powered license
practice exams.  The databases contain references to where each question came from.