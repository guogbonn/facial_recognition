This is a facial recognition project
Description:
This project is broken up into two parts.

Part 1 is a function (project_1_facial_recognition) that processes two images and acertains if the same face appears in both pictures and outputs a number representation of the certainty thereof onto the test image. See image below:

Part 2 is a web cam facial recognition fucnction (project_2_facial_recognition_attendance) which based on known faces stored in the face_2 directory can classify faces introduced in the web cam frame. see imgaes below:

    Limitations:
    Varying facial expressions and imgas with differing angles increase the inconsitency of results, also processing speed is slow with python, C++ would be better suited for intensive calculations

Goals
Further understanding of opencv techniques as well as get an introduction to computervision facial recognition algorithms

Further Applications:
Facial Recognition can be used in a variety of instances from security, to search and rescue, person tracking.

Background https://medium.com/@ageitgey/machine-learning-is-fun-part-4-modern-face-recognition-with-deep-learning-c3cffc121d78

Youtube tutorial:
https://www.youtube.com/watch?v=sz25xxF_AVE&list=PLMoSUbG1Q_r8jFS04rot-3NzidnV54Z2q&index=1
To Run:
pipenv run python basics.py

To Install:
clone the directory

**_ assuming pip env has not on system _**
refer to the following links for the installation of pipenv
https://packaging.python.org/tutorials/managing-dependencies/

    https://pipenv-fork.readthedocs.io/en/latest/basics.html

    pipenv install
    pipenv shell

You will also need to add vs code where to find your virtualenv

First, navigate to your Pipenv directory (where your Pipfile is located). Then run pipenv --venv, to get the full path to the Pipenv's virtualenv. This is probably something like /home/myuser/.local/share/virtualenvs/projectname, depending on which operating system you are on.

Next, press CTRL+Shift+P (Cmd in MacOS) and search for "Select Workspace Interpreter". Press enter, and select any of the suggested interpreters. Upon doing this, a .vscode directory will be created inside your project root, containing a settings.json. Open this file, and set python.pythonPath to the virtualenv path you found earlier, and add /bin/python at the end.

In other words, settings.json should look something like this:

{
"python.pythonPath": "/home/myuser/.local/share/virtualenvs/projectname/bin/python"
}

or

click in the bottom left area of the terminal as seen in the image

Save the settings file, and restart Visual Studio Code, for the changes to take effect.

Notes
To install a requiments.txt file run:
pipenv install -r path/to/requirements.txt

    To install new packages:
        (ex. specific version) pipenv install "numpy == 1.19.3"
        (ex. latest version) pipenv install numpy

    To save updated requirements run:
        pipenv lock
        pipenv run pip freeze > requirements.txt

    To deactivate shell run:
        deactivate

Extra: Readme Cheat sheet
https://levelup.gitconnected.com/github-readme-cheatsheet-617dff61fa23
