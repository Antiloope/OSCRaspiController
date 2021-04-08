import argparse
from osc.osc_client import OSCClient
from osc.osc_server import OSCServer
from manager.queue.events_queue import EventsQueue
from display.display_manager import DisplayManager
from heg.heg import HEG
from manager.events_manager import EventsManager

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument(
        "--ip", default="127.0.0.1",
        help="The ip of the OSC server")

  parser.add_argument(
        "--port", type=int, default=9001,
        help="The port the OSC server is listening on")

  args = parser.parse_args()

  # Create osc_client
  osc_client = OSCClient(args.ip, args.port)

  # Create display_manager
  display_manager = DisplayManager()

  # Create events_queue
  queue = EventsQueue()

  # Create osc_server
  osc_server = OSCServer(args.ip, args.port, queue)

  # Create heg
  heg = HEG(queue)

  # Create events_manager
  events_manager = EventsManager(heg, osc_server, queue, osc_client, display_manager)

  events_manager.start()
