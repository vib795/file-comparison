
# File Comparison Tool

This application is a Flask-based web tool that allows users to perform side-by-side comparisons of two text files, highlighting differences with syntax highlighting, similar to functionality seen in tools like Notepad++ or GitHub's diff view.

## Features

- Side-by-Side Comparison: Visually compare two files side by side to easily identify added, removed, or unchanged lines.
- Syntax Highlighting: Enhances readability and comprehension by highlighting syntax for various programming languages.
- User-Friendly Interface: Simple and intuitive web interface for uploading or pasting file contents for comparison.
- Customizable: Open-source and easily modifiable to add more features or support for additional file types.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.6+
- Flask
- A modern web browser

### Installing

First, clone the repository to your local machine:

```bash
git clone https://github.com/vib795/file-comparison.git
cd file-comparison
```

Install the required Python packages:

```bash
pip install -r requirements.txt
```

### Running the Application

To start the Flask application, run:

```bash
flask run
```

Visit `http://localhost:5000` in your web browser to use the application.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
