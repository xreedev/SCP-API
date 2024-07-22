# SCP API

This is a simple Flask API that serves data from a text file (`test.txt`) as JSON.This was built as a 
simple project to better understand APIs

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/xreedev/SCP-API.git
    ```

2. Navigate to the project directory:

    ```bash
    cd SCP-API
    ```

3. Install the required dependencies:

    ```bash
    pip install Requirements.txt
    ```

## Usage

1. Run the Flask application:

    ```bash
    python app.py
    ```

2. Access the API in your web browser or using a tool like cURL:

    ```
    http://localhost:7775/
    ```

## File Structure

- `app.py`: Contains the Flask application code.
- `test.txt`: Input data file.
- `test3.json`: Output JSON file.
- `README.md`: Project documentation.

The apicall.py file can be sued to test run the api after updating the ipaddress value with your host address

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
