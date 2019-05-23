#!/usr/bin/env python

import http.server
import json
import sys
from typing import Dict
from uuid import uuid4

resource_vs_data = {}

registered_resources = set()

poll_interval = 0.1


class RESTRequestHandler(http.server.BaseHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        return http.server.BaseHTTPRequestHandler.__init__(self, *args, **kwargs)

    def do_GET(self):
        path = self.path
        probable_resource = path.split("/")[-1]
        # This is to support get_all
        if probable_resource in registered_resources:
            rv = resource_vs_data[path]
            self.create_response(200, rv)
            return
        resource_path = "/".join(path.split("/")[:-1])
        id = path.split("/")[-1]
        response = resource_vs_data[resource_path][id]
        self.create_response(200, response)

    def do_POST(self):
        resource = self.path.split("/")[-1]
        registered_resources.add(resource)

        pay_load = self.get_payload()
        id = pay_load.get("id")
        if not id:
            pay_load["id"] = str(uuid4())
        path_resources = resource_vs_data.get(self.path, {})
        path_resources[pay_load["id"]] = pay_load
        resource_vs_data[self.path] = path_resources
        self.create_response(200, pay_load)

    def do_PUT(self):
        path = self.path
        id = path.split("/")[-1]
        pay_load = self.get_payload()
        path_resources = resource_vs_data.get(self.path, {})
        path_resources[id] = pay_load
        resource_path = "/".join(self.path.split("/")[:-1])
        resource_vs_data[resource_path] = path_resources
        self.create_response(200, pay_load)

    def do_DELETE(self):
        path = self.path
        id = path.split("/")[-1]
        del resource_vs_data["/".join(path.split("/")[:-1])][id]
        self.send_response(200)
        self.end_headers()

    def get_payload(self):
        payload_len = int(self.headers.get("content-length", 0))
        payload = self.rfile.read(payload_len)
        payload = json.loads(payload.decode())
        return payload

    def create_response(self, status_code: int, pay_load: Dict):
        self.send_response(status_code)
        self.end_headers()
        self.wfile.write(json.dumps(pay_load).encode())


def rest_server(port):
    "Starts the REST server"
    http_server = http.server.HTTPServer(("", port), RESTRequestHandler)
    # http_server.service_actions = service_worker
    print("Starting HTTP server at port %d" % port)
    try:
        http_server.serve_forever(poll_interval)
    except KeyboardInterrupt:
        pass
    print("Stopping HTTP server")
    http_server.server_close()


def main(argv):
    rest_server(8080)


if __name__ == "__main__":
    main(sys.argv[1:])
