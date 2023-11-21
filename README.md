# Fitness Coaching Chatbot

Welcome to the Fitness Coaching Chatbot repository! This chatbot is designed to provide virtual fitness coaching and answer questions related to fitness and health. The chatbot is implemented in Python using the PyTorch library for natural language processing and deep learning.

## Table of Contents

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Model Training](#model-training)
- [Chat Interface](#chat-interface)
- [Credits](#credits)
- [License](#license)

## Overview

This virtual fitness coaching chatbot uses a natural language processing (NLP) model to understand and respond to user input. The NLP model is trained on a dataset of intents related to fitness coaching. The chatbot provides informative responses based on the trained model.

## Prerequisites

- Python 3.x
- PyTorch
- NLTK (Natural Language Toolkit)
- Tkinter (for the graphical user interface)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Dhanush0R/chatbot-v.git
   cd chatbot-v
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

To use the fitness coaching chatbot, run the `app.py` script:

```bash
python app.py
```

This will launch a graphical user interface where you can interact with the chatbot.

## Model Training

If you want to retrain the NLP model or modify the intents, follow these steps:

1. Edit the `intents.json` file to customize the intents and responses.

2. Run the `train.py` script to train the NLP model:

   ```bash
   python train.py
   ```

   The trained model will be saved to a file named `data.pth`.

## Chat Interface

The chat interface is implemented using Tkinter. You can type messages in the entry box at the bottom, press Enter to send a message, and receive responses from the chatbot in the main text area.

## Credits

The NLP model architecture and training process are adapted from [NLTK](https://www.nltk.org/).

## License

This project is licensed under the [MIT License](LICENSE).
