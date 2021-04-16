import argparse
from osc.osc_client import OSCClient
from osc.osc_server import OSCServer
from manager.queue.events_queue import EventsQueue
from display.display_manager import DisplayManager
from heg.heg import HEG
from manager.events_manager import EventsManager
import os

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument(
        "--ip", default="127.0.0.1",
        help="The ip of the OSC server")

  parser.add_argument(
        "--port", type=int, default=8001,
        help="The port the OSC server is listening on")

  local_address = os.popen('ip address | grep -oP "192.168.0.[0-9]{3}(?=/24)"').read()

  args = parser.parse_args()

  # Create osc_client
  osc_client = OSCClient(args.ip, args.port)

  # Create display_manager
  display_manager = DisplayManager()

  # Create events_queue
  queue = EventsQueue()

  # Create osc_server
  osc_server = OSCServer(local_address, args.port + 1000, queue)

  # Create heg
  heg = HEG(queue)

  # Create events_manager
  events_manager = EventsManager(heg, osc_server, queue, osc_client, display_manager)

  events_manager.start()
