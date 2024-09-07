# Tkinter CRUD Application

This project is a simple CRUD (Create, Read, Update, Delete) application built using Python's Tkinter library for the graphical user interface and SQLite for the database. The application allows users to input, view, update, and delete records in a local database.

## Features

- **Add New Records**: Input data into the form fields and save it to the database.
- **View Records**: Display a list of all records saved in the database.
- **Update Records**: Select a record by ID, edit the data, and update the changes in the database.
- **Delete Records**: Remove records from the database by ID.

## Prerequisites

- Python 3.x
- SQLite3 (included with Python)
- Tkinter (included with Python)
- PIL (Python Imaging Library) - for handling images in Tkinter.

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/tkinter-crud-application.git
   cd tkinter-crud-application
   ```

2. **Install Required Libraries:**
   Make sure you have `Pillow` installed for handling images:
   ```bash
   pip install Pillow
   ```

## How to Run

1. Navigate to the project directory:
   ```bash
   cd tkinter-crud-application
   ```

2. Run the application:
   ```bash
   python app.py
   ```

   Replace `app.py` with the actual name of your Python file if it differs.

## Usage

1. **Submit Record:**
   - Fill in the form fields: First Name, Last Name, Address, City, State, and Zip Code.
   - Click the "Submit" button to save the record to the database.
   - All fields are mandatory, and the ZIP code must be a number.

2. **View Records:**
   - Click the "View Records" button to display all records in the database.
   - Records are shown with their ID, Name, and City.

3. **Update Record:**
   - Enter the ID of the record you wish to update in the "Select ID" field.
   - Click the "Update Record" button.
   - A new window will open with the current details of the record. Edit the fields as needed and click "Save" to update the record.

4. **Delete Record:**
   - Enter the ID of the record you wish to delete in the "Select ID" field.
   - Click the "Delete Record" button to remove the record from the database.

## Validation

- The application includes basic validation:
  - All fields are required when submitting or updating a record.
  - The ZIP code must be numeric.
  - The ID for updating or deleting must be numeric.

## Troubleshooting

- **Common Issues:**
  - Ensure the database path is correct and accessible.
  - Make sure Python and required libraries are installed correctly.

- **Error Messages:**
  - If you see validation error messages (e.g., "All fields are required" or "ID must be a number"), ensure that the input meets the specified criteria.

## Screenshots

Include screenshots of the application interface, demonstrating the various features.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Tkinter for GUI
- SQLite for database management
- Python Imaging Library (PIL) for handling images
