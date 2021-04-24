
# Simple React Node.JS app serving API content from python Flask API
This project is based on [How To Create a React + Flask Project](https://blog.miguelgrinberg.com/post/how-to-create-a-react--flask-project)


React Javascript front-end

yarn install  
of create from scratch with: yarn create-react-app react-flask-app

API (python side):
cd api
create venv (I created in pycharm as api/venv which will hold the python runtime and dependencies)
pip install -r requirements.txt (will add those dependencies to venv)


React's app.js has fetch('api/time') for requesting current time or 'api/todos for requesting JSON 
* Node.js provides webserver
    * Node's (npm init)  (change port in .env file)
    * forwards to Flask  (package.json: "proxy": "http://localhost:5000")
* Flask python web server
    * .flaskenv configuration: FLASK_APP=api.py (redirects queries to api.py)
    * flask route 'api/time' is mapped by annotation to get_current_time()
* Yarn
    * dependency manager (like maven)
    * script shortcuts in package.json:
        * "yarn start" (start node) (http://localhost:3000/ would invoke index.html from node express)
        * "yarn start-api" (start flask) (http://127.0.0.1:5000/api/time is an example of going straight to the API)


#Part 2 Deploy to Heroku: [How to Deploy a React + Flask Project](https://blog.miguelgrinberg.com/post/how-to-deploy-a-react--flask-project) 