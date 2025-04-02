# Stock Price Prediction Web Application

This project is a web application for stock price prediction, developed using Django for the backend and HTML for the frontend. It allows users to input stock data and receive predictions based on implemented models.

## Features

- **User Interface**: Interactive web pages to input stock data and view predictions.
- **Prediction Models**: Backend algorithms to analyze stock data and generate predictions.
- **Data Visualization**: Graphical representation of stock trends and prediction results.

## Technologies Used

- **Backend**: Django (Python)
- **Frontend**: HTML
- **Database**: SQLite (default for Django projects)

## Setup Instructions

### Clone the Repository

```bash
git clone https://github.com/ThePunisher30/Stock-Price-Prediction-UI.git
```

### Navigate to the Project Directory

```bash
cd Stock-Price-Prediction-UI
```

### Create a Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'
```

### Install Required Packages

```bash
pip install django
```

### Apply Migrations

```bash
python manage.py migrate
```

### Run the Development Server

```bash
python manage.py runserver
```

### Access the Application

Open a web browser and navigate to `http://127.0.0.1:8000/` to use the application.

## Project Structure

- **StockPrice/**: Main Django application directory containing settings and configurations.
- **dashboard/**: Contains the web interface templates and static files.
- **db.sqlite3**: SQLite database file.
- **manage.py**: Django's command-line utility for administrative tasks.
- **mysite.log**: Log file for the project.

## Contributing

Contributions are welcome! If you have suggestions or improvements, please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License.

---

*Note: This README is based on the available information from the repository and may require additional details for complete setup and usage instructions.*
