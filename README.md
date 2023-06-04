# Tren-chatbot

The Tren-Chatbot is a Rasa-based movie recommender chatbot created as part of a Bachelor Semester Project. The project aims to investigate the impact of recommendation length on the usability of a CRS (Content-based Recommender System). The chatbot utilizes a .csv dataset containing movie information to provide movie recommendations to users based on their preferences.

## Project Overview

This project focuses on evaluating the effect of recommendation length on user experience within a movie recommender system. It consists of two chatbots, with the other one available [here]<(https://github.com/saadshakeel1357/Tren2-chatbot)>.

## Features

- Simple movie recommendation based on user preferences
- Recommendation of movies based on genres
- Searching and filtering movies using a .csv dataset
- Integration with Rasa NLU and Rasa Core

## Prerequisites

- Python 3.8 
- Rasa 3.5
- check requirements.txt file for all packages

## Installation

1. Clone the repository:
    git clone <repository_url>
   
2. Set up a virtual environment (optional but recommended):
    python3 -m venv venv
    source venv/bin/activate

3. Install the required packages:
    pip install -r requirements.txt
    
## Usage

1. Train the RASA model:
    rasa train

2. Run the chatbot:
    rasa shell

For more details about running the chatbot, please refer to the BSP report.
