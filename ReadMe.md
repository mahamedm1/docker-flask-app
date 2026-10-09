1. Import Flask framework which is responsible for building web apps in python to create the web app

2. app = Flask(name) - creates the app instance and passes the name variable so flask knows where the app lives and can find things like files and templates within it.

3. @app.route('/') - declares the landing page for a homepage.

4. def welcome_page() - defining a function responsible for returning welcome screen

5. if **name** == '**main**': "**name**" Checks if this Python file is being run directly rather than being imported by another Python file

app.run(host='0.0.0.0', port=5002) - listen on all network interfaces on port 5002, then start the server
