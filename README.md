# TranscriberTone-Speech-To-Text-
TranscriberTone, an innovative speech-to-text conversion project, delivers seamless and precise transcription of User Separated spoken words into written text.   Our audio processing algorithms capture the  human speech, providing an efficient and accurate solution for diverse applications.

### About Noise Cancellation Code:-

##### Importing Libraries:

os: Used for file system operations
multiprocessing: For parallel processing
AudioFile: For reading and writing audio files
pedalboard: For applying audio effects
noisereduce: For noise reduction
Flask: For creating a web API

##### Defining Global Variables:

sr: Sample rate of audio files (44100 Hz)
output_folder: Path to store processed audio files
Creating the Output Folder:

##### Checks if the output folder exists
Creates the output folder if it doesn't exist

##### Audio Processing Function:

Reads the audio file and resamples it to the specified sample rate
Applies stationary and non-stationary noise reduction using noisereduce
Creates an audio processing chain using pedalboard
Applies the audio processing chain to the reduced noise
Writes the processed audio to the output file

##### Flask Application:

Creates a Flask app instance
Defines a route /process_audio to handle POST requests
Checks if an audio file is provided in the request
Saves the uploaded audio file to the input folder
Processes the audio using the process_audio function
Returns a JSON response indicating success or error
Runs the Flask app on port 5000

##### Main Block:

Runs the Flask app in debug mode
Runs the Flask app on port 5000 and binds to all interfaces (0.0.0.0)

##### Error Handling:

Error Handling in Output Folder Creation:

Encloses the output folder creation code within a try-except block
Catches any OSError exceptions during folder creation
Prints an error message containing the specific exception details
Error Handling in Audio Processing:

Encloses the entire audio processing block within a try-except block
Catches any exceptions that might occur during audio processing
Prints an error message containing the specific exception details if an error occurs
Error Handling in Flask Application:

Encloses the entire Flask application code, including route handling and app execution, within a try-except block
Catches any exceptions that might occur during Flask app operation
Prints an error message containing the specific exception details if an error occurs
Improved Response Handling:

In the /process_audio route handler:

Checks for the presence of an audio file in the request
If no file is found, returns a JSON response with an error message
If a file is provided:
Saves the uploaded file to the input folder
Processes the audio using the process_audio function
Returns a JSON response indicating successful audio processing
In the if __name__ == '__main__': block:

Tries to run the Flask app in debug mode
If any exception occurs, prints an error message and exits the program
