"""Leave API routes"""

from . import leave


@leave.route("/", methods=["GET", "POST"])
def index():
    return "<h1> This is the leave routes </h1>"