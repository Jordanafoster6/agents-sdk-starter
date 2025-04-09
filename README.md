## Agent-Demo Sandbox startup

### Backend Setup
- Install Deps: `npm i`
- Startup Backend: `npx ts-node-dev --respawn --require tsconfig-paths/register src/index.ts`

## Frontend Setup
- Install deps: `npm i`
- Startup frontend: `npm start`

### Agent Service Setup
You'll need to set up a Python virtual environment (venv) with the required dependencies:

1. Install Python with Homebrew
   - `brew install python`

2. Navigate to the agent-service directory
   - `cd agent-service`

3. Create a virtual environment
   - `python -m venv .venv`

4. Activate the virtual environment
   - `source .venv/bin/activate`
   - Your prompt should now show `(agent-service)` at the beginning

5. Install pip if not available in the virtual environment
   - `python -m ensurepip --upgrade`

6. Install dependencies from requirements.txt
   - `python -m pip install -r requirements.txt`
   - If requirements.txt doesn't exist, install the required packages:
     - `python -m pip install fastapi uvicorn openai-agents tenacity cachetools`
     - Create requirements.txt for future use: `python -m pip freeze > requirements.txt`

7. Startup the Micro-Service
   - `python -m uvicorn main:app --port 5100 --reload`

8. To deactivate the virtual environment when done
   - `deactivate`
