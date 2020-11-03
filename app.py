from flask import Flask, request
import jinja2

app = Flask(__name__)

@app.route('/')
def index():
    # Render template
    templateLoader = jinja2.FileSystemLoader(searchpath="./assets")
    templateEnv = jinja2.Environment(loader=templateLoader)
    template = templateEnv.get_template("index.html")
    output = template.render()

    return output


@app.route('/groups')
def groups():
    # Get group query parameter
    group = request.args.get("group")

    # Render template with map parameter
    templateLoader = jinja2.FileSystemLoader(searchpath="./assets")
    templateEnv = jinja2.Environment(loader=templateLoader)
    template = templateEnv.get_template("groups.html")
    output = template.render(group=group)

    return output

