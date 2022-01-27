from _testcapi import instancemethod
from flask import Blueprint, render_template, request, jsonify
import os
import datetime


class Root:
    def __init__(self, server):
        self.server = server
        self.blueprint = Blueprint("Root", __name__)
        self.blueprint.add_url_rule("/", view_func=self.index)
        self.blueprint.add_url_rule("/api/time-till", view_func=self.get_time_till)
        self.server.after_request(self.after_request)

    @instancemethod
    def index(self):
        return render_template("index.html")

    @instancemethod
    def get_time_till(self):
        now = datetime.datetime.now()
        delta = datetime.datetime(year=now.year + 1, month=1, day=1, hour=0, minute=0) - now
        hours, r = divmod(delta.seconds, 3600)
        minutes, seconds = divmod(r, 60)
        return jsonify({
            "year": now.year + 1,
            "days": delta.days,
            "hours": hours,
            "minutes": minutes,
            "seconds": seconds
        })

    def after_request(self, response):
        try:
            self.server.console.server_log(f"[{request.remote_addr}][bold] [{response.status}][/bold] {request.path}")
        except Exception as e:
            self.server.console.error_log(f"Logging error: {e}")
        return response
