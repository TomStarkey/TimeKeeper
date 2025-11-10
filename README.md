# TimeKeeper
## Introduction
Helps you keep track of your working hours. A simple GUI which includes a stopwatch and an entry for labelling your project.

## Installing dependencies
Before installing dependencies I would recommend creating a virtual environment. This can be done either with ***python -m virtualenv <environmentname>*** or with ***python -m venv <environmentname>***.

Third party dependencies for the project can be installed using the powershell command ***pip install -r requirements.txt*** (If this command has not worked then try adding "*python -m*" or "*py -m*" beforehand.)
This uses the *requirements.txt* file included in the repository to install the required dependencies.

## Using the programme
Run gui.py to begin the programme. 

## The Stopwatch
When it is open you will see a clock in the corner with the time and the date. Underneath that there are three buttons: *Start, Reset,* and *Stop*. When you click *Start* you will see a stop watch appear on the right. You can stop and start this with the *Stop* and *Start* buttons. Then when you are satisfied that you have completed a distinct section of work, you can simply click *Reset* and this will set the stop watch back to zero and output your time to an excel file in the same directory as the Python file. This will include four columns: *Date*, *Time*, *Time worked*, and *Label*.

## Labelling
On the UI (User Interface) you will also see an entry labelled *Label*. You can create new labels or use existing ones. 

### Creating new
New labels can be created by typing the label name into the entry and clicking *Add Project*. If there are no pre-existing labels, the program will create a text file entitled *"Projects.txt"* which will contain the names of your project labels. Once this is done the labels will appear underneath the entry.

### Using existing project labels.
These will appear beneath the entry with a tickbox to toggle off or on. Currently the tickbox defaults to on, but it is not actually selected until you toggle it off and back on again. This is still in devlopment.

## Further development
There are a few changes and additions to be made.
 - Buttons *Remove* and *Clear* need functionality added to them
 - The tick box for the project labels needs to be changed to default to untick so it does not lead the user to belief their project is selected when it is not.
 - An error message appears if the user has the spreadsheet open when the program tries to write to it. It should reset once the user has shut the file and tried again but it currently does not.
