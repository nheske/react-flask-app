
This project is based on [How To Create a React + Flask Project](https://blog.miguelgrinberg.com/post/how-to-create-a-react--flask-project)

* React as Javascript front-end
    * npx create-react-app react-flask-app
    * React's app.js has fetch('/time') to call server    
* Node.js provides webserver
    * Node's (npm init) package.json: "proxy": "http://localhost:5000"
    * forwards to Flask
* Flask python web server
    * .flaskenv configuration: FLASK_APP=api.py (redirects queries to api.py)
    * flask route '/time' is mapped by annotation to get_current_time()
* Yarn
    * dependency manager (like maven)
    * script shortcuts in package.json:
        * "yarn start" (start node)
        * "yarn start-api" (start flask)
