fastapi
pydantic
typing


fastapi:
creates fastapi instance

creates route using fastapi instance decorator
create static and dyanmic paths using http methods like get, post

pydantic

creates pydantic model for user to validate the incoming data form cliend.
and also try to get multi data in form of array
use model dump method to convert object into python dictionary
user pydantic field validator to validate the email with sepcific domain

tpying 
use Optional to make our query parameters option and List to convert the array of user objects coming from clien into python list for further utilizing.


commands
create virtual environment
window: python -m venv "name"
macOS : python3 -m venv 'name'

acitve virtual envrionmetn

window: name/scripts/activate
macOS: source name/bin/activate

install fastapi with dependencies and extra librareis  like uvicorn, pydantic

pip install fastapi["standard"]

run the fastapi 

fastapi dev main.py
fatapi dev app/