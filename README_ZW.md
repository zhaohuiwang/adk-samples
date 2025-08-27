

## Directory 
```bash
.   # run command here eg. adk web, agent1Name, ... agentXName will be the options
├── .env
├── .venv # python-dotenv search order: Explicit path if specified > current working dir > Parent dirs, recursively searches partent dirs up to the root of the filesystem.
├── README.md
├── poetry.lock
├── pyproject.toml
├── agent1Name # can be multiple levels hierarchy. Also shown on UI
│     ├── __init__.py
│     ├── agent.py   # agent's logic, default agent.py. Must have a `root_agent` variable as an entry point.
│     ├── prompts.py # optional
│     ├── tools.py   # optional, with all user defined tool functions
│     ├── sub_agents # optional, suggest to organize with agent.py, prompt.py and tools.py as the root agent.
│     └── utils      # optional
└──agentXName ...
```
## Environment variables 
- First create a `.env` copy from the example (plain text), `$ cp .env.example .env`
- Then replace with your own credentials (KEY=Value one item per line)
- Preferred: keep the `.env` file in project root dir or preferred working dir
- `python-dotenv` search order: Explicit path if specified > current working dir > Parent dirs, recursively searches partent dirs up to the root of the filesystem. `load_dotenv()` loads environment variables from a `.env` file into the system's environment variables making them accessable via `os.getenv('KEY')`. `dotenv_values()` parses a `.env` file and returns a dictionary containing the key-value pairs of environment variables defined in the file, without modifying the system's environment variables. `find_dotenv()` searches for a `.env` file and returns the path to the first .env file it finds, otherwise an empty string.
- To avoid exposing sensitive information, exclude it from version control `echo "*.env" >> .gitignore`
## Google Agent Development Kit (ADK)
`google.adk.cli` module (part of the `google-adk` package) is the command-line interface (CLI) entry point for the Google ADK, a framework for building, evaluating, and deploying AI agents. 
The `web` subcommand of `google.adk.cli` launches the ADK's built-in web-based developer UI (referred to as `adk web`). This UI is designed to simplify agent development and debugging by providing an interactive interface to test and inspect agents.

When executed, `adk web` starts a local web server (typically on http://localhost:8000 or http://127.0.0.1:8000) that hosts the ADK developer UI, allowing users to interact with their agents, view event logs, and test functionalities like text, voice, or video streaming.

The Google ADK is an open-source, modular framework for developing and deploying AI agents, optimized for Google’s Gemini models and the Google Cloud ecosystem but designed to be model-agnostic and deployment-agnostic. It simplifies the creation of intelligent agents that can perform tasks, use tools, and collaborate in multi-agent systems.

* ### Environment Setup by uv:
    * `uv run` ensures that the Python environment is correctly configured with the required version (Python 3.9+ for ADK) and dependencies (e.g., google-adk). If the google-adk package is not installed, uv can automatically install it, assuming it's specified in a pyproject.toml or similar configuration file.
    * It activates a virtual environment (or creates one if needed) to isolate dependencies, avoiding conflicts with other Python projects.
* ### Launching the Python Interpreter:
    * The `python -m google.adk.cli` part invokes the Python interpreter to execute the `google.adk.cli` module, which is the CLI component of the ADK.
* ### Executing the web Subcommand:
    * The `web` subcommand starts a local web server that hosts the ADK developer UI. This UI is built using Angular and requires Node.js, npm, and the google-adk Python package to be installed.
    * The UI allows you to interact with the agent via a chat interface, access to Trace/Events/State/Artifacts/Sessions/Eval, create/delete/export a session.
* ### Agent Configuration:
    * The agent's logic must be defined in an `agent.py` file within an agent directory (e.g., `multi_tool_agent/`), with a `root_agent` variable specifying the agent's properties (name, model, tools, instructions)
    * A .env file in the agent directory should contain necessary configurations (authentication), such as:
    ```bash
    # you do not have to put the value inside quotation marks unless it contains special characters
    GOOGLE_GENAI_USE_VERTEXAI=TRUE
    GOOGLE_API_KEY=your-api-key
    GOOGLE_CLOUD_PROJECT=your-project-id    # default if not specified
    GOOGLE_CLOUD_LOCATION=us-central1       # default if not specified
    ```
* ### Agent Configuration:
    * The `google-adk` package must be installed 
    * For the web UI, additional dependencies like Angular CLI, Node.js, npm and uvicorn/gradio may be required
    * If voice or video streaming is used, a Gemini model supporting the Live API must be specified in the agent.py file



## Example Workflow

#### 1. Set up the Project:
- Create a project directory with an agent folder (e.g., search_assistant/)
- Define an `agent.py` file with a root_agent, such as
```python
from datetime import datatime
# The LlmAgent (often aliased simply as Agent)
from google.adk.agents import Agent
from google.adk.tools import google_search

# Suggest to save function tools in a seperate script file like tools.py
def get_current_time() -> Dict:
    """Get the current time in the format YYYY_MM_DD HH:MM:SS"""
    return {"Current_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
    # adk by default wrap the return into json/dictionary, e.g. {"Result": "2025-07-11 00:00:00"}. So we want to specify it is the current time to be helpful as possible to the agent.
    # Also note that parameters with default values do not working at the present time.

root_agent = Agent(
    name="search_assistant",
    model="gemini-2.0-flash",
    instruction="You are a helpful assistant. Answer user questions using Google Search when needed.",
    description="An assistant that can search the web.",
    tools=[google_search],
    # can only use one Built-in tool at a time, not a combination of Build-in tool and Funciton tool
    sub_agents=[],
)
```
- `name` (Required): A unique string identifier for the agent.
- `model` (Required): Specify the underlying LLM that will power this agent's reasoning.
- `instruction` parameter is arguably the most critical for shaping an LlmAgent's behavior. It's a string (or a function returning a string) that tells the agent:
    - Its core task or goal.
    - Its personality or persona (e.g., "You are a helpful assistant," "You are a witty pirate").
    - Constraints on its behavior (e.g., "Only answer questions about X," "Never reveal Y").
    - How and when to use its tools. You should explain the purpose of each tool and the circumstances under which it should be called, supplementing any descriptions within the tool itself.
    - The desired format for its output (e.g., "Respond in JSON," "Provide a bulleted list").

    The instruction is a string template, you can use the {var} syntax to insert dynamic values into the instruction. {var} is used to insert the value of the state variable named var. {artifact.var} is used to insert the text content of the artifact named var. If the state variable or artifact does not exist, the agent will raise an error. If you want to ignore the error, you can append a ? to the variable name as in {var?}.
- `description` (Optional, Recommended for Multi-Agent): Provide a concise summary of the agent's capabilities. This description is primarily used by other LLM agents to determine if they should route a task to this agent. Make it specific enough to differentiate it from peers.

- `tools` (Optional): Provide a list of tools the agent can use. Tools give your LlmAgent capabilities beyond the LLM's built-in knowledge or reasoning. They allow the agent to interact with the outside world, perform calculations, fetch real-time data, or execute specific actions.
- `sub_agents` (Optional): Specialized agents under the root agent, each with their own tools, instructions, and scopes. They handle specific tasks (e.g., querying BigQuery) and can share context with the root agent.

- Advanced Configuration & Control  (`generate_content_config`, `input_schema`, `output_schema`, `output_key`, `include_contents`)
- `input_schema` (Optional): Define a schema representing the expected input structure. It is kind of stringent or rigid and prone to fail so use it wisely. 
- `output_schema` (Optional): Define a schema representing the desired output structure.
- `output_key` (Optional): Provide a string key. The text content of the agent's final response will be automatically saved to the session's state dictionary under this key. This is useful for passing results between agents or steps in a workflow.

#### 2. Create a `.env` file with Google Cloud credentials or API keys
#### 3. Install Dependencies
```bash
# Install uv if not already installed
curl -LsSf https://astral.sh/uv/install.sh | sh
# Install google-adk and other dependencies
uv pip install google-adk
```

#### 4. Run the Command
```bash
# To run the agent via the web UI
uv run python -m google.adk.cli web
# To run the agent via CLI instead of the web UI
uv run python -m google.adk.cli run <agent_name>
# To start the API server for the web UI
uv run python -m google.adk.cli api_server --allow_origins=http://localhost:4200 --host=0.0.0.0

# or if the virtual environment is activated, you can simply the command like
adk     # list all options
adk web 
```
#### 5. Access the UI
- Open http://localhost:8000 in a browser.
- Select the agent (e.g., search_assistant) from the UI dropdown.
- Type a prompt (e.g., “What’s the weather in New York?”) or use voice input if configured.
- View the agent’s responses and debug events in the “Events” tab
#### 6. Stop the Server
- Press `Ctrl+c` in the terminal to stop the web server.


## Tools
There are three types of tools in ADK: Function tools, Built-in tools (by Google and only works for Gemini models as of 07/2025) and Thrid-party tools.

## References

[Google Agent Development Kit](https://google.github.io/adk-docs/)