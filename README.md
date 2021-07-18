# flask_print_file_app

Test application to print content of the given file name on page

All files are present in the src/render_files dir.

to test run the application follow following steps:

- Create virtual env and activate it

```sh
python3 -m venv venv
. venv/bin/activate
```

- Install dependencies

```sh
pip install -r REQUIREMENTS.txt
```

- Run the application

```sh
python3 src/main.py
```
then go to localhost:5000 to use application

- src/config/constants.py
  It is the global constants file and following things can be changed:
  - DEFAULT_PORT : Application will run on port 5000 by default, which can be changed.
  - DEFAULT_RENDER_FOLDER : URL accepts File name as a path but inside the render_file dir only,
  - SHOW_SEPARATE_ERROR_PAGE : App can show error either on separate page or on the same page by changing this flag.
