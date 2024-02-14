"""
A Flask web application to compare the content of two files or text inputs. This module utilizes 
the Flask framework to create a simple web interface where users can upload two files or input text
into two separate forms. The application then compares the contents of these two inputs, using the 
`difflib` module, to generate a detailed, side-by-side comparison of the differences. The 
comparison highlights additions, deletions, and unchanged lines between the two inputs. The results
are displayed in a user-friendly format, allowing for easy visualization of differences.
The application supports both GET and POST requests, rendering an initial form for input on a GET
request, and processing the submitted content on a POST request to display the comparison results.
Dependencies:
    - Flask: A micro web framework for Python, used for handling web requests 
    and rendering templates.
    - difflib: A module in the Python standard library, used to compare sequences,
    in this case, lines of text from the input files or texts.
"""

import difflib
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    """
    The main view function that handles requests to the root URL ('/').
    On a GET request, this function renders an initial HTML form allowing the user to either upload
    two files or enter text into two separate input fields for comparison.
    On a POST request, the function processes the uploaded files or entered text, compares the 
    content using the `difflib.ndiff` method, and generates a list of differences. These 
    differences are processed to support side-by-side comparison, distinguishing between added 
    lines, deleted lines, and unchanged lines.
    The comparison results are then rendered and displayed to the user in a 'results.html' 
    template, providing a visual representation of differences between the two inputs.
    Parameters:
    - None explicitly; uses `request` context from Flask to access submitted data.
    Returns:
    - A rendered template: 'index.html' for a GET request, or 'results.html' with comparison 
    results for a POST request.
    """
    if request.method == 'POST':
        # Initialize variables to store file or text content
        file1_content, file2_content = None, None

        # Handle file upload for file1
        file1 = request.files['file1']
        if file1 and file1.filename != '':
            file1_content = file1.read().decode('utf-8')
        else:
            file1_content = request.form['content1']

        # Handle file upload for file2
        file2 = request.files['file2']
        if file2 and file2.filename != '':
            file2_content = file2.read().decode('utf-8')
        else:
            file2_content = request.form['content2']

        # Split the contents into lines for comparison
        file1_lines = file1_content.splitlines()
        file2_lines = file2_content.splitlines()

        # Generate unified diff
        unified_diff = list(difflib.unified_diff(file1_lines, file2_lines, fromfile='file1', \
                                                 tofile='file2', lineterm=''))
        # Generate split diff
        diff = list(difflib.ndiff(file1_lines, file2_lines))

        # Process unified diff
        unified_diff_processed = [(line, 'none') if line.startswith(' ') else (line, 'add')\
                                  if line.startswith('+') else (line, 'del')\
                                    for line in unified_diff]

        # Process split diff for side-by-side comparison
        split_diff_left, split_diff_right = [], []
        for line in diff:
            if line.startswith('-'):
                split_diff_left.append((line[2:], 'del'))
                split_diff_right.append(('', 'none'))
            elif line.startswith('+'):
                split_diff_left.append(('', 'none'))
                split_diff_right.append((line[2:], 'add'))
            elif line.startswith(' '):
                split_diff_left.append((line[2:], 'none'))
                split_diff_right.append((line[2:], 'none'))

        # Render the comparison results
        return render_template('results.html', unified_diff=unified_diff_processed,\
                               split_diff_left=split_diff_left, split_diff_right=split_diff_right,\
                                view_mode="split")

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
