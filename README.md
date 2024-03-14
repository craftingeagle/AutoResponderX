# AutoResponderX - Automated WhatsApp Business Autoresponder

AutoResponderX is a Termux tool designed to automate responses to messages received on WhatsApp Business. It integrates with the WhatsApp Business API to analyze incoming messages and send predefined responses based on keywords or patterns. This tool aims to enhance customer service efficiency by promptly addressing frequently asked questions and providing immediate assistance to users.

## Setup
  
### 1. Prerequisites
- An Android device with Termux installed
- Access to the WhatsApp Business API

### 2. Installation

1. Clone this repository to your Termux environment:
   ```bash
   git clone https://github.com/craftingeagle/AutoResponderX.git
   ```

2. Navigate to the AutoResponderX directory:
   ```bash
   cd AutoResponderX
   ```
3. Install the required dependencies:
   ```bash
   pkg install python
   ```

### 3. Configuration
1. Open the `config.py` file in the `src` directory.
2. Update the `API_KEY` variable with your WhatsApp Business API key.
3. Optionally, configure other variables such as database settings.

### 4. Database Setup
1. The tool uses SQLite by default for simplicity.
2. No additional setup is required as SQLite is included with Python.
3. The database will be created automatically when the tool is executed for the first time.

## Usage

### Running the Tool
1. Navigate to the `src` directory:
   ```bash
   cd src
   ```
2. Execute the main script:
   ```bash
   python3 main.py
   ```

### Functionality
- The tool continuously listens for incoming messages from the WhatsApp Business API.
- When a message is received, it extracts keywords, searches for predefined responses, and sends an appropriate response.
- Messages and responses are recorded in the database for future reference and analysis.

### Examples
- **Incoming Message**: "Hello, do you have this product in stock?"
- **Response**: "Yes, we currently have the product in stock. You can place an order through our website."
- **Incoming Message**: "What are your business hours?"
- **Response**: "Our business hours are Monday to Friday, 9 am to 5 pm. We are closed on weekends and holidays."

## Contribution
Contributions to the AutoResponderX project are welcome! If you encounter any bugs or have suggestions for improvements, please open an issue or submit a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
