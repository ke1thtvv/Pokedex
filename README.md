# Pokedex - AI-Based Pokemon Recognition

![pokedex0](https://github.com/user-attachments/assets/bc54b5bc-da67-439d-9855-66d82bda8330)
![pokedex2](https://github.com/user-attachments/assets/7cb563a1-fc6e-40d6-abc0-4a97590b5c42)
![pokedex1](https://github.com/user-attachments/assets/5427101a-2991-40f5-a5f0-14fc03a965c5)

## Overview

Pokedex is an AI-powered application that allows users to recognize and analyze Pokemon from images or by selecting them from a list. It integrates **machine learning**, **computer vision**, and an interactive **GUI** built with PyQt5. The project demonstrates expertise in **deep learning, Python application development, and UI design**, making it an impressive portfolio piece for aspiring software engineers.

## Features
- **AI-Powered Pokemon Recognition**: Uses a trained deep learning model to classify Pokemon from images.
- **Manual Selection**: Choose a Pokemon from a predefined list for quick lookup.
- **Interactive GUI**: Built with PyQt5 for a seamless and user-friendly experience.
- **Data Analysis**: Reads and processes Pokemon statistics using Pandas.
- **Two Input Methods**:
  - Drag-and-Drop Image Input: Analyze images by dragging and dropping them into the app.
  - Manual Selection: Pick a Pokemon from a searchable list.
- **Real-Time Feedback**: Displays predicted Pokemon name and confidence score.
- **Background Music & Animations**: Enhances user experience with sound effects and visual elements.

## Technologies Used
- **Python** (Core application logic)
- **PyQt5** (Graphical User Interface)
- **FastAI** (Deep learning model for Pokemon classification)
- **Pandas** (Data analysis for Pokemon statistics)
- **NumPy** (Efficient numerical computations)
- **OpenCV** (Image processing for inference)
- **Pygame** (Music and sound effects)

## Installation & Setup
### Prerequisites
Ensure you have Python 3.8+ installed, along with the required dependencies.

### Installation Steps
1. Clone this repository:
   ```sh
   git clone https://github.com/yourusername/pokedex.git
   cd pokedex
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Download the trained model from Google Colab:
   - Open the provided Google Colab notebook [HERE PLACE LINK].
   - Run the download script to get `export.pkl`.
   - Move `export.pkl` to the `train/` directory.
4. Run the application:
   ```sh
   python main.py
   ```

## Usage
1. Launch the application.
2. Choose one of the two recognition methods:
   - **Drag and drop** a Pokemon image into the designated area.
   - **Manually select** a Pokemon from the list.
3. The AI model predicts the Pokemon and displays its stats (if using image input).
4. Explore more details about the Pokemon in the interactive UI.

## Project Structure
```
Pokedex/
├── models/            # Pre-trained ML model (downloaded separately)
├── gui/               # PyQt5 UI components
├── data/              # CSV files with Pokemon stats
├── assets/            # Images, icons, and audio
├── main.py            # Entry point for the application
├── inference.py       # AI model inference logic
├── menu.py            # GUI menu handling
├── info.py            # Detailed Pokemon information UI
└── requirements.txt   # Project dependencies
```

## Contributing
Contributions are welcome! Feel free to submit a pull request or report issues.

