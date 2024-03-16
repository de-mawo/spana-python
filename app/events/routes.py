"""Events API routes"""

from . import events


@events.route("/", methods=["GET", "POST"])
def index():
    return "<h1> This is the events routes </h1>"
