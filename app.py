from flask import Flask, render_template, request
import difflib

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
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

        # Generate a diff
        diff = difflib.ndiff(file1_lines, file2_lines)

        # Process diff for side-by-side comparison
        diff_left, diff_right = [], []
        for line in diff:
            if line.startswith('-'):
                diff_left.append((line[2:], 'del'))
                diff_right.append(('', 'none'))
            elif line.startswith('+'):
                diff_left.append(('', 'none'))
                diff_right.append((line[2:], 'add'))
            elif line.startswith(' '):
                diff_left.append((line[2:], 'none'))
                diff_right.append((line[2:], 'none'))

        # Render the comparison results
        return render_template('results.html', diff_left=diff_left, diff_right=diff_right)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
