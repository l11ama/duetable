from pythonosc import dispatcher
from pythonosc import osc_server

def parameter_handler(unused_addr, args, value):
    print(f"Received {args}: {value}")
    # Process the value to affect your parameters here

dispatcher = dispatcher.Dispatcher()
dispatcher.map("/RegeneratorNo", parameter_handler, "RegeneratorType")

ip = "127.0.0.1"  # Localhost
port = 12345  # Port to listen on

server = osc_server.ThreadingOSCUDPServer((ip, port), dispatcher)
print(f"Serving on {server.server_address}")

server.serve_forever()
