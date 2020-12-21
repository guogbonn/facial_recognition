This is a facial recognition project
Description:
Background https://medium.com/@ageitgey/machine-learning-is-fun-part-4-modern-face-recognition-with-deep-learning-c3cffc121d78

Youtube tutorial:
https://www.youtube.com/watch?v=sz25xxF_AVE&list=PLMoSUbG1Q_r8jFS04rot-3NzidnV54Z2q&index=1
To Run:
pipenv run python basics.py

To Install:
**_ assuming pip env has not on system _**
refer to the following links for the installation of pipenv
https://packaging.python.org/tutorials/managing-dependencies/

    https://pipenv-fork.readthedocs.io/en/latest/basics.html

    pipenv install
    pipenv shell

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
