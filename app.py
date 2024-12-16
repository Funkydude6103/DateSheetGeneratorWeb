from flask import Flask, render_template, request, jsonify
import pandas as pd
import os


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

uploaded_data = None


def load_datesheet(file_path):
    sheet_data = pd.read_excel(file_path, sheet_name='Complete')
    cleaned_data = sheet_data.iloc[2:, [0, 1, 2, 3, 4, 5]]
    cleaned_data.columns = ['Day', 'Date', 'Code 1', 'Course Name 1', 'Code 2', 'Course Name 2']

    morning_data = cleaned_data[['Day', 'Date', 'Code 1', 'Course Name 1']].rename(
        columns={'Code 1': 'Code', 'Course Name 1': 'Course Name'}
    )
    morning_data['Time'] = '09:00 - 12:00'

    afternoon_data = cleaned_data[['Day', 'Date', 'Code 2', 'Course Name 2']].rename(
        columns={'Code 2': 'Code', 'Course Name 2': 'Course Name'}
    )
    afternoon_data['Time'] = '1:00 - 4:00'

    combined_data = pd.concat([morning_data, afternoon_data], ignore_index=True)
    combined_data = combined_data.dropna(subset=['Code', 'Course Name'])

    return combined_data


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    global uploaded_data
    file = request.files.get('file')
    if file:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        uploaded_data = load_datesheet(file_path)
        courses = uploaded_data[['Code', 'Course Name']].drop_duplicates().to_dict(orient='records')
        return jsonify({'courses': courses})
    return jsonify({'error': 'No file uploaded'}), 400


@app.route('/generate', methods=['POST'])
def generate_datesheet():
    global uploaded_data
    if uploaded_data is None:
        return jsonify({'error': 'No data available. Please upload a file first.'}), 400

    selected_courses = request.json.get('selected_courses')
    if not selected_courses:
        return jsonify({'error': 'No courses selected'}), 400

    selected_data = uploaded_data[uploaded_data['Code'].isin([course.split(' - ')[0] for course in selected_courses])]
    sorted_data = selected_data.sort_values(by='Date', key=lambda col: pd.to_datetime(col, format='%d-%b-%Y'))

    return jsonify({'data': sorted_data.to_dict(orient='records')})


if __name__ == '__main__':
    app.run(debug=True)
