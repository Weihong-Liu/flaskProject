from flask import Blueprint, render_template

file = Blueprint("file", __name__, url_prefix="/file")