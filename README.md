
# README

## Project: Data Analysis and Visualization App

This project is a web-based application for uploading CSV files, analyzing data, and visualizing it using various chart types. It is built using Django for the backend and Chart.js for dynamic chart rendering on the frontend.

---

## Features

- **Upload CSV Files**: Users can upload CSV files to analyze the data.
- **Data Analysis**:
  - Display the first few rows of the dataset.
  - Generate summary statistics for numerical columns.
  - Highlight missing values in the dataset.
- **Dynamic Chart Generation**:
  - Visualize data using different chart types such as Line, Bar, Scatter, Pie, etc.
  - Choose x-axis and y-axis columns dynamically for visualization.
  - Support for chunk-based data processing for efficient rendering.
- **Error Handling**:
  - Handles invalid files gracefully.
  - Displays user-friendly error messages for invalid data or processing errors.

---

## Setup Instructions

### Prerequisites

- Python 3.11 or above
- Django 4.x or above
- Pip (Python package manager)

### Installation Steps

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Set Up a Virtual Environment**:
   ```bash
   python -m venv denv
   source denv/bin/activate  # On Windows: denv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Start the Development Server**:
   ```bash
   python manage.py runserver
   ```

6. **Access the Application**:
   Open your browser and navigate to server port.

---

## How to Use

1. Navigate to the application in your browser.
2. Upload a CSV file using the upload form.
3. Select a chunk size for data visualization (default is 100 rows).
4. View:
   - Data summary (first few rows, statistics, missing values).
   - Select columns for x-axis and y-axis.
   - Choose a chart type and click "Generate Chart" to visualize the data.
5. Interact with the chart dynamically on the frontend.

---

## File Structure

- **`data_analysis`**: Main Django app for data upload and processing.
- **`templates`**: Contains HTML templates for rendering views.
- **`static`**: Includes Chart.js and other static assets.
- **`forms.py`**: Handles the CSV upload form.
- **`views.py`**: Contains core logic for file handling, data analysis, and chart generation.
- **`file_handler.py`**: Manages file uploads and storage.

---

## Technical Details

### Backend:
- **Framework**: Django
- **Processing**: Pandas for data manipulation

### Frontend:
- **Framework**: Bootstrap for UI
- **Visualization**: Chart.js

### Additional Features:
- Efficient chunked processing for large datasets.
- Support for various chart types and dynamic column selection.

---

## Future Enhancements

- Add support for additional file formats (e.g., Excel).
- Enable user authentication for personalized data storage.
- Expand chart customization options (e.g., colors, labels).

---

## Contributing

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m "Add feature"`).
4. Push to the branch (`git push origin feature-name`).
5. Open a pull request.

--- 

Feel free to reach out for any questions or issues!
