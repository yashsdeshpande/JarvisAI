
# Jarvis AI Assistant

This project is a personal AI assistant named **Jarvis** that can perform various tasks based on voice commands. Jarvis can interact with the user to provide weather updates, play music, open websites, launch applications, fetch news, and generate AI-based text using Google's Gemini model.

## Features

1. **Weather Updates**: Get live weather information for any city.
2. **News Retrieval**: Fetch and read out the latest news articles from various categories.
3. **Application Launching**: Open applications like VS Code, Chrome, etc.
4. **Website Access**: Open commonly used websites via voice commands.
5. **Music Playback**: Play specific music tracks stored locally.
6. **Time Retrieval**: Get the current time on command.
7. **AI Text Generation**: Generate responses or essays using Google's Gemini AI model.

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/jarvis-ai-assistant.git
   cd jarvis-ai-assistant
   ```

2. **Install Dependencies**
   Ensure you have Python installed. Then, install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **API Keys**
   - Create a `config.py` file in the root directory.
   - Add your API keys and necessary configurations:
     ```python
     WEATHER_API_KEY = 'your_openweathermap_api_key'
     NEWS_API_KEY = 'your_newsapi_api_key'
     gemini_api_key = 'your_google_gemini_api_key'
     ```

4. **Running the Assistant**
   ```bash
   python main.py
   ```

## Usage

### Voice Commands
- **Weather**: Say `"weather in [city name]"` to get the weather update for any city.
- **News**: Say `"news"`, and then specify the category of news you are interested in (e.g., `"technology"`).
- **Open Applications**: Say `"open [application name]"` to launch an application. Supported applications include VS Code, Chrome, Brave, Notepad, Calculator, and Edge.
- **Open Websites**: Say `"open [website name] site"` to open a website.
- **Play Music**: Say `"play [song name]"` to play a music file stored locally.
- **Get Time**: Say `"time"` to get the current time.
- **AI Response Generation**: Say `"using artificial intelligence"` followed by your prompt to get AI-generated text.

### Example Usage
- **"weather in Delhi"**: Provides the current weather in Delhi.
- **"news" > "technology"**: Fetches the latest technology news.
- **"play titanium"**: Plays the song "Titanium" from your local music directory.

## Requirements

- Python 3.x
- Libraries: `win32com.client`, `speech_recognition`, `requests`, `webbrowser`, `google.generativeai`

Install these libraries via `pip`:
```bash
pip install pywin32 SpeechRecognition requests google-generativeai
```

## Contributing

Feel free to fork this repository, create a branch, and submit a pull request with your changes. Contributions are always welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- **OpenWeatherMap**: For providing weather data.
- **NewsAPI**: For fetching the latest news articles.
- **Google Gemini**: For AI text generation.
