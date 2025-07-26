# A Makefile is used to define tasks (targets) and their dependencies, typically for building and managing projects.

# target (task) named install
install:
	@command -v uv >/dev/null 2>&1 || { echo "uv is not installed. Installing uv..."; curl -LsSf https://astral.sh/uv/install.sh | sh; source $HOME/.local/bin/env; }
	uv sync && npm --prefix frontend install
# @Suppresses echoing the command itself when executed (only output is shown)
# command -v returns the path to the command if it exists, or nothing if it doesn't. (Here it check if the uv command is available in the system's PATH)
# >/dev/null 2>&1: Redirects both stdout and stderr to /dev/null, silencing any output or errors from the command -v uv check.
# ||: If the previous command fails (i.e., uv is not found, exit code non-zero), execute the commands in the following block.
# { ...; ...; ... }: Groups commands to execute

# curl -LsSf https://astral.sh/uv/install.sh Downloads and executes the uv installation script from the specified URL.
# | sh Pipes the script to a shell for execution.

# && Executes the next command only if uv sync succeeds.
# npm --prefix frontend install: Runs npm install in the frontend directory
# --prefix frontend Specifies the directory where npm should look for the package.json file.
# uv sync && npm --prefix frontend install Installs all dependencies for both the Python-based backend (via uv) and the Node.js-based frontend (via npm).

dev:
	make dev-backend & make dev-frontend
# Starts both the backend and frontend development servers (defined below) simultaneously in the background, enabling full-stack development.

dev-backend:
	uv run adk api_server app --allow_origins="*"

dev-frontend:
	npm --prefix frontend run dev
# npm --prefix frontend: Specifies that npm should operate in the frontend directory.

playground:
	uv run adk web --port 8501

lint:
	uv run codespell
	uv run ruff check . --diff
	uv run ruff format . --check --diff
	uv run mypy .
# codespell Runs the codespell tool, which checks for common spelling mistakes in code and documentation.
# ruff check . Runs ruff, a fast Python linter, to check for code style and potential errors in all files in the current directory (.).
# --diff: Outputs the changes needed to fix linting issues in a diff format, without applying them.
# ruff format . Runs ruff’s code formatter to check code formatting in all files in the current directory.
# --check Checks if files are formatted correctly without modifying them.
# --diff Outputs a diff of the changes needed to format the code properly.
# mypy . Runs mypy, a static type checker for Python, on all files in the current directory to check for type-related errors.