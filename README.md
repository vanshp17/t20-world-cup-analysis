# T20 World Cup Analysis

![WhatsApp Image 2024-08-01 at 17 37 39_e445f009](https://github.com/user-attachments/assets/35cc2ee1-4baf-4156-bad9-4b54d0661226)

This repository contains the code for analyzing and predicting scores in T20 World Cup matches using machine learning techniques. The project includes data collection, data extraction, feature extraction, and a Streamlit application for interactive predictions.

## Project Structure

- `app.py`: Streamlit application for predicting T20 scores.
- `data-collection _T20 score prediction.ipynb`: Notebook for downloading and organizing the dataset.
- `data_extraction.ipynb`: Notebook for extracting and preprocessing match data.
- `feature_extraction.ipynb`: Notebook for creating features for the prediction model.
- `style.css`: CSS file for styling the Streamlit app.
- `t20_pipe.pkl`: Trained machine learning model.
- `requirements.txt`: List of dependencies.

## Setup Instructions

1. **Clone the repository**:
    ```bash
    git clone https://github.com/vanshp17/t20-world-cup-analysis.git
    cd t20-world-cup-analysis
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Streamlit app**:
    ```bash
    streamlit run app.py
    ```

## Usage

1. **Data Collection**:
    - Download the dataset from Kaggle and organize it in the specified directory.

2. **Data Extraction**:
    - Extract and preprocess match data to create a clean dataset.

3. **Feature Extraction**:
    - Generate features required for the machine learning model.

4. **Streamlit Application**:
    - Use the Streamlit app to predict the scores of T20 matches by selecting the batting team, bowling team, city, current score, overs, wickets, and runs scored in the last 5 overs.

## Predicting Scores

The Streamlit app provides an interactive interface to predict the final score of a T20 match. Select the relevant inputs and click the 'Predict Score' button to get the predicted score.

## Contributing

Feel free to fork this repository and contribute by submitting pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License.
