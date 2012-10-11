import multiprocessing


# Unix sockets should avoid a few context switches, as well as a bunch
# of TCP processing. TCP is better for development, though.
#bind = "unix:/tmp/gunicorn.sock"
bind = "127.0.0.1:8100"

# We're fairly I/O-bound, so keep extra workers around.
workers = multiprocessing.cpu_count() * 2 + 1

# Use the asychronous worker class based on gevent.
worker_class = "gevent"

accesslog = "-"
errlog = "-"
