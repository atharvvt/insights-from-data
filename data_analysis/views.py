from django.shortcuts import render
from .forms import UploadFileForm
from .file_handler import handle_uploaded_file
from celery import shared_task
import pandas as pd
import numpy as np
import os
import json

TEMP_DIR = "file_uploads"
os.makedirs(TEMP_DIR, exist_ok=True)

# Data processing handler
# Modify the data processing handler to handle both x and y axes
from django.shortcuts import render
import pandas as pd
import json

# Assuming 'handle_uploaded_file' is the function that processes the uploaded CSV file
def process_data(file_path, chunk_size):
    df = pd.read_csv(file_path)

    # Drop ID columns if present
    id_columns = [col for col in df.columns if col.lower() == 'id']
    df.drop(columns=id_columns, inplace=True, errors='ignore')

    # Results dictionary to pass data to the template
    results = {}

    # Columns available for visualization (only numerical columns for charts)
    numerical_columns = df.select_dtypes(include=['number']).columns
    results['columns'] = numerical_columns.tolist()

    # First few rows
    results['head'] = df.head().to_html(classes='table table-striped')

    # Summary statistics for numerical columns
    summary_stats = df[numerical_columns].describe().transpose()
    results['summary'] = summary_stats.to_html(classes='table table-bordered')

    # Missing values
    missing_values = df.isnull().sum()
    results['missing'] = missing_values.to_frame('Missing Values').to_html(classes='table table-hover')

    # Prepare charts data
    charts_data = generate_charts_data(df, numerical_columns, chunk_size)
    results['charts_data'] = json.dumps(charts_data)

    return results


def generate_charts_data(df, columns, chunk_size=100):
    charts_data = []

    # Data for charts (we'll use the first few rows as the chunk)
    chunk = df.iloc[0:chunk_size]

    for column in columns:
        # Ensure columns are numeric or compatible
        x_data = chunk.index.tolist()  # Default x-axis: DataFrame index
        y_data = chunk[column].dropna().tolist()  # Y-axis: Column values

        chart = {
            'label': column,
            'x_data': x_data,  # Pass x_data explicitly
            'y_data': y_data   # Pass y_data explicitly
        }
        charts_data.append(chart)

    return charts_data




def upload_file(request):
    results = None  # Initialize results to avoid NameError
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                # Handle file upload
                file_path = handle_uploaded_file(request.FILES['file'])
                chunksize = int(request.POST.get('chunksize', 100))
                results = process_data(file_path, chunksize)
            except Exception as e:
                results = {'error': f"An error occurred: {str(e)}"}
    else:
        form = UploadFileForm()

    return render(request, 'data_analysis_app/upload.html', {'form': form, 'results': results})




