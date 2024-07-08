from flask import Flask, render_template,request
from stories import story

app = Flask(__name__)

@app.route('/')
def show_home():
  """show Greeting homepage"""

  prompts = story.prompts

  return render_template("home.html",prompts = prompts)




@app.route('/story')
def show_story():
  """Create story and show to the user"""

  text = story.generate(request.args)

  return render_template("story.html",text = text)