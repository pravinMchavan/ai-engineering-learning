#A Virtual Environment in Python is like creating a separate, isolated space for each project where you can install libraries without affecting other projects or your system Python.
# It allows you to manage dependencies for different projects independently, ensuring that each project has its own set of libraries and versions.
# This is particularly useful when working on multiple projects that may require different versions of the same library or when you want to avoid conflicts between project dependencies and the global Python environment.
# Virtual environments are created using the `venv` module, which is included in the Python standard library. You can create a virtual environment by running the command `python -m venv myenv`, where `myenv` is the name of your virtual environment.
# Once the virtual environment is created, you can activate it using the command `source myenv

#How to create virtual environment
# 1. Open a terminal or command prompt.
# 2. Navigate to the directory where you want to create your virtual environment.
# 3. Run the command `python -m venv myenv`, replacing `my
#env` with the name you want for your virtual environment.
# 4. After running the command, a new directory named `myenv` will be created in your current directory. This directory contains the virtual environment and its own Python interpreter.
# 5. To activate the virtual environment, use the following command:
# - On Windows: `myenv\Scripts\activate`
# - On macOS and Linux: `source myenv/bin/activate`
# 6. Once activated, you will see the name of your virtual environment in the terminal prompt, indicating that you are now working within that environment.
# 7. You can now install packages using pip, and they will be installed in the virtual environment rather than globally on your system.
# 8. To deactivate the virtual environment and return to the global Python environment, simply run the command `deactivate`.

# pip freeze > requirements.txt # this command is used to create a requirements.txt file that lists all the installed packages and their versions in the current virtual environment. This file can be used to recreate the same environment on another machine or share it with others.