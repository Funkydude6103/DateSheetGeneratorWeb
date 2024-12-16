# Date Sheet Generator

A web application built with Flask that allows users to upload an Excel file containing course schedules, select specific courses, and generate a date sheet dynamically. The app renders the date sheet on the webpage and provides an option to save it as an image.

---
## Live Demo
The app is live at: https://funkydude6103.pythonanywhere.com/

## Features

- **Upload Excel File**: Upload an Excel file containing the schedule data.
- **Search and Select Courses**: Use a search bar to quickly find and select courses from a scrollable list.
- **Dynamic Date Sheet Generation**: Generate a date sheet dynamically based on selected courses.
- **Save as Image**: Save the generated date sheet as an image using a simple button click.
- **Responsive Design**: Optimized for both desktop and mobile devices using Bootstrap.

---

## Technologies Used

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS (Bootstrap), JavaScript (jQuery, html2canvas)
- **Excel Processing**: Pandas
- **Environment**: PythonAnywhere (or any WSGI-compatible hosting platform)

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/date-sheet-generator.git
   cd date-sheet-generator
   ```

2. **Set Up a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the App**:
   ```bash
   python app.py
   ```

5. **Access the App**:
   Open your browser and go to `http://127.0.0.1:5000`.

---

## How to Use

1. **Upload File**:
   - Upload an Excel file containing the schedule. Ensure the file follows the required format:
     - Sheet name: `Complete`
     - Columns: `Day`, `Date`, `Code 1`, `Course Name 1`, `Code 2`, `Course Name 2`

2. **Search and Select Courses**:
   - Use the search bar to find courses by name or code.
   - Select courses from the list.

3. **Generate Date Sheet**:
   - Click the "Generate Date Sheet" button to dynamically render the date sheet below the button.

4. **Save as Image**:
   - Click the "Save as Image" button to download the date sheet as a PNG file.

---

## Deployment

### Deploy on PythonAnywhere
1. **Upload the Code**:
   - Upload your project files to PythonAnywhere using the file manager or via Git.

2. **Configure WSGI File**:
   - Ensure the WSGI file points to your Flask app.

3. **Install Dependencies**:
   - Install the required packages in your PythonAnywhere virtual environment:
     ```bash
     pip install -r requirements.txt
     ```

4. **Reload the App**:
   - Reload the web app from the PythonAnywhere dashboard.

---

## Dependencies

- Flask
- Pandas
- html2canvas (JavaScript library)
- Bootstrap (CSS framework)

Install Python dependencies with:
```bash
pip install -r requirements.txt
```

---

## Contributing

Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Make your changes and commit them:
   ```bash
   git commit -m "Description of changes"
   ```
4. Push to your forked repository:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request on the main repository.

---

## Demo
<div style="display: flex; justify-content: center; align-items: center;">
    <video class="as" src="https://github.com/user-attachments/assets/91aa5c37-2742-40d8-ac22-4c1ba695a689" controls="controls" style="max-width: 100%;">
        Your browser does not support the video tag.
    </video>
</div>
