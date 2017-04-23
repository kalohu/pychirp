# Before running tests you have to set the pythonpath environment variable
# export PYTHONPATH=project_src_directory

python3 -m unittest discover

python3-coverage erase
python3-coverage run --branch -m unittest discover
python3-coverage report --omit *__init__*
python3-coverage html --omit *__init__*
