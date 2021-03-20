# TDD Full Course (Learn Test Driven Development with Python)

Follows the [youtube video](https://www.youtube.com/watch?v=eAPmXQ0dC7Q) tutorial.

## Three Rules of TDD

1. You are not allowed to write a line of product code without **writing a failing test first**.

1. You are not allowed to write more of a test than is required to fail. (**Write just enoough test to fail**)

1. You are not allowed to write more code than is to pass the failing test. (**Write just enough code to pass**)

## Setup

1. Create python virtual environment using:

    ```python3 -m venv /path/to/new/virtual/environment```

1. Install requirements using:

    ```pip install -r requirements.txt```

1. Download spacy small language model using:

    ```python -m spacy download en_core_web_sm```

1. Create directories using:

    ```mkdir static templates test```

    > static: Javascript and CSS

    > templates: Index.html flask template

    > test: Unit test and end test are located

1. After writing **Setup.py**, install it using:

    ```pip install -e .```
    > -e means editable, we won't have to install it again after making changes

1. Download and place the *Browser Web Driver* (I have used ChromeWebDriver) in known direcory and insert the path in file ``test_index_e2e.py``

## Next Step

Use GitLab CI/CD build, tests and deployment on this project.
