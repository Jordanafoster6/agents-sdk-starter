## Agent-Demo Sandbox startup

### Backend Setup
- Install Deps: `npm i`
- Startup Backend: `npx ts-node-dev --respawn --require tsconfig-paths/register src/index.ts`

## Frontend Setup
- Install deps: `npm i`
- Startup frontend: `npm start`

### Agent Service Setup
You're going to need to setup a virtual environment (venv) and make sure the main dependencies are installed:
- Python
- pip/pipx
- fastapi
- uvicorn
- openAI SDK: `pip install openai-agents`

The steps below are in somewhat working order.. I ran into a few errors along the way but wanted to provide some sort of guide to get this thing running.

1. Install python with homebrew
- `brew install python`
2. Install `pipx`
- Verify `pip` installed with brew: `pip3 --version`
- If not, then: `brew install pipx`
- Verify `pipx` installed: `pipx ensurepath`
2. Install `uvicorn`
- `pip install uvicorn`
- Verify `uvicorn` installed: `uvicorn --version`
3. Add pipx `bin` directory to app
- `export PATH="$HOME/.local/bin:$PATH"`
4. Install `fastapi`
- `pipx install fastapi`
5. Startup Micro-Service
- `uvicorn main:app --port 5100 --reload` OR `python -m uvicorn main:app --port 5100 --reload`
