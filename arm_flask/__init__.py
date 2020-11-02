from flask import Flask

app = Flask(__name__)
app.secret_key = "ARM_2020"

from arm_flask import route