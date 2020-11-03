from flask import Flask
app = Flask(__name__)

@app.route('/')
def welcome_world():
    return '''<html>
    	<h1>
    		Hello!
    	</h1>
    	<p>
    		This is where you welcome the user. 
    	</p>
    	<form action="/map">
    		<input type="submit" value="View Map" />
		</form>
    </html>
    '''

@app.route('/map')
def goodbye_world():
    return '''
    <html>
    	<h1>
    		Farmworker Advocacy and Community Groups
    	</h1>
    	<p>
    		Groups by EPA Region
    	</p>
    	<form action="/">
    		<input type="submit" value="Go Back" />
		</form>
		<iframe src='https://www.arcgis.com/home/webmap/viewer.html?webmap=41281c51f9de45edaf1c8ed44bb10e30' width="100%" height="90%"></iframe>
    </html>
    '''

