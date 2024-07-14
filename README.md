## Introduction

The Data Security Chrome Extension is designed to help users avoid accidentally sharing sensitive information such as personal data governed by GDPR/KVKK regulations. When a user pastes sensitive data into any input field on a webpage, the extension will display a warning message.

## Features

- Detects GDPR/KVKK sensitive data.
- Alerts the user when sensitive data is detected.
- Integrates with FastAPI for backend processing.
- Utilizes the OpenAI API for data analysis.

## Requirements

- Python 3.10 or higher
- Node.js and npm
- Google Chrome

## Installation

### Backend

1. Clone the repository:
    ```bash
    git clone https://github.com/merveealpay/data-security-chrome-extension.git
    cd data-security-chrome-extension/backend
    ```

2. Create a virtual environment and activate it:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Set your OpenAI API key in the `.env` file:
    ```plaintext
    OPENAI_API_KEY=your-openai-api-key
    ```

### Frontend (Chrome Extension)

1. Navigate to the `extension` directory:
    ```bash
    cd ../extension
    ```

2. No additional installation steps are required for the Chrome extension.

## Running the Backend

1. Navigate to the backend directory:
    ```bash
    cd ../backend/app
    ```

2. Start the FastAPI server:
    ```bash
    uvicorn main:app --reload
    ```

## Loading the Chrome Extension

1. Open Google Chrome and go to `chrome://extensions/`.
2. Enable "Developer mode" by toggling the switch in the top right corner.
3. Click "Load unpacked" and select the `extension` directory from this repository.

## Testing

1. Open any webpage in Google Chrome.
2. Paste the following example of sensitive data into any input field:
    ```plaintext
    John Doe, john.doe@example.com, +1-555-123-4567, 1234 Main St, Anytown, AT 12345, USA, Credit Card Number: 4111 1111 1111 1111, Social Security Number: 123-45-6789
    ```
3. The extension should display an alert warning you about sharing sensitive data.
