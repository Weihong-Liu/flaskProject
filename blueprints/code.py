from flask import Blueprint, render_template, request

code = Blueprint("code", __name__, url_prefix="/code")