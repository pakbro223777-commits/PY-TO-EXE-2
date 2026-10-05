PY TO EXE - GITHUB ACTIONS TEMPLATE

NO PYTHON OR PIP REQUIRED ON YOUR PC

1. Create a new GitHub repository.
2. Upload EVERY file and folder from this ZIP.
3. Replace main.py with your own Python file.
   IMPORTANT: keep your file name as main.py.
4. Open the repository on GitHub.
5. Click the "Actions" tab.
6. Click "Build EXE" on the left.
7. Click "Run workflow".
8. Wait for the workflow to finish.
9. Open the completed workflow run.
10. Scroll to "Artifacts".
11. Download "MyProgram-Windows".
12. Extract the ZIP to get MyProgram.exe.

NOTES
- The build runs on a GitHub-hosted Windows machine.
- Your PC does NOT need Python or pip.
- The current build uses PyInstaller.
- The EXE is built with --noconsole.
- If your program needs a console window, remove --noconsole
  from .github/workflows/build-exe.yml.

DEPENDENCIES
If your program needs extra Python packages, add install commands
before the Build EXE step, for example:

python -m pip install requests flask

Then run the workflow again.
