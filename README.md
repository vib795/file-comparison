
# File Comparison Tool

This application is a Flask-based web tool that allows users to perform side-by-side comparisons of two text files, highlighting differences with syntax highlighting, similar to functionality seen in tools like Notepad++ or GitHub's diff view.

## Features

- **Side-by-Side Comparison:** Visually compare two files side by side to easily identify added, removed, or unchanged lines.
- **Syntax Highlighting:** Enhances readability and comprehension by highlighting syntax for various programming languages.
- **User-Friendly Interface:** Simple and intuitive web interface for uploading or pasting file contents for comparison.
- **Customizable:** Open-source and easily modifiable to add more features or support for additional file types.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.11.7
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

## Running it using Docker
- Make sure you have [**Docker**](https://www.docker.com/products/docker-desktop/) installed. 

- Run 
    ```bash
    cd file-comparison
    ```
- Run 
    ```bash
    docker compose up --build
    ```
    and then to destroy the container run
    ```bash
    docker compose down
    ```
    OR <br/>
    You can download and run a pre built image from the public repository [utkarshsingh/file-comparison](https://hub.docker.com/r/utkarshsingh/file-comparison) by running the command:
    ```bash
    docker run -p 5000:5000 --name file-comparison \
            utkarshsingh/file-comparison
    ```
    and then to detroy the container run:
    ```bash
    docker stop file-comparison
    docker rm file-comparison
    ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
