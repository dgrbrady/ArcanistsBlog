from flask import Blueprint

bp = Blueprint('sql', __name__)

from app.sql import models