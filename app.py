from flask import Flask, render_template, request
import difflib

app = Flask(__name__)

# Make `zip` available in Jinja2 templates
app.jinja_env.globals.update(zip=zip)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file1_lines = request.form['file1'].splitlines()
        file2_lines = request.form['file2'].splitlines()

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

        # Pass the zipped result to the template
        diff_pairs = zip(diff_left, diff_right)
        
        return render_template('results.html', diff_pairs=diff_pairs)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
