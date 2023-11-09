import requests
# URL of your Flask API
url = "http://127.0.0.1:5000/process_audio"  # Replace with the correct URL
# Replace with the actual path to your audio file
file_path = "C:\\Users\\Rohan.Jadhav\\Audio_InputFile\\sp02_car_sn5.wav"
# Send the POST request with the audio file
files = {'file': open(file_path, 'rb')}
response = requests.post(url, files=files)
# Print the response from the API
print(response.json())