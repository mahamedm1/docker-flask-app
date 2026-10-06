1. Import Flask framework which is responsible for building web apps in python to create the web app

2. app = Flask(name) - creates the app instance and passes the name variable so flask knows where the app lives and can find things like files and templates within it.

3. @app.route('/') - declares the landing page for a homepage.

4. def welcome_page() - defining a function responsible for returning welcome screen
