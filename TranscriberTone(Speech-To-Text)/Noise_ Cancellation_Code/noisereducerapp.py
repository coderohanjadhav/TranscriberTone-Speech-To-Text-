# Importing Libraries
import os
from pedalboard.io import AudioFile
from pedalboard import *
import noisereduce as nr
from flask import Flask, request, jsonify

app = Flask(__name__)

# Define the sample rate
sr = 44100

# Output folder path
output_folder = "c:\\Users\\Rohan.Jadhav\\Stationary_Audio_output"

# Create the output folder if it doesn't exist
try:
  if not os.path.exists(output_folder):
    os.makedirs(output_folder)
except OSError as e:
  print(f"Error creating output folder: {e}")

def process_audio(input_file_path, output_file_path):
  try:
    with AudioFile(input_file_path).resampled_to(sr) as f:
      audio = f.read(f.frames)

    # Apply Stationary noise reduction
    reduced_noise = nr.reduce_noise(y=audio, sr=sr, stationary=True, prop_decrease=0.75)

    # Apply non-stationary noise reduction
    reduced_noise = nr.reduce_noise(y=audio, sr=sr, thresh_n_mult_nonstationary=2, stationary=False)

    # Set up audio processing chain (modify as needed)
    board = Pedalboard([
      NoiseGate(threshold_db=-30, ratio=1.5, release_ms=250),
      Compressor(threshold_db=-16, ratio=2.5),
      LowShelfFilter(cutoff_frequency_hz=400, gain_db=10, q=1),
      Gain(gain_db=10)
    ])

    # Apply the audio processing chain to the reduced noise
    effected = board(reduced_noise, sr)

    # Write the processed audio to the output file
    with AudioFile(output_file_path, 'w', sr, effected.shape[0]) as f:
      f.write(effected)

    print(f"Processed audio saved to {output_file_path}")
  except Exception as e:
    print(f"Error processing audio: {e}")

@app.route('/process_audio', methods=['POST'])
def process_audio_route():
  try:
    if 'file' not in request.files:
      return jsonify({'error': 'No file provided'})

    input_file = request.files['file']
    input_filename = input_file.filename
    input_file_path = os.path.join(output_folder, input_filename)
    output_file_path = os.path.join(output_folder, input_filename)

    input_file.save(input_file_path)
    process_audio(input_file_path, output_file_path)

    return jsonify({'message': 'Audio input speech converted to Text'})
  except Exception as e:
    return jsonify({'error': f'Error in audio processing: {e}'})

if __name__ == '__main__':
  try:
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)
  except Exception as e:
    print(f"Error starting the Flask app: {e}")