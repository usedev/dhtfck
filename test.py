import logging
import time
from btdht import DHT

# Enable logging:
loglevel = logging.INFO
formatter = logging.Formatter("[%(levelname)s@%(created)s] %(message)s")
stdout_handler = logging.StreamHandler()
stdout_handler.setFormatter(formatter)
logging.getLogger("btdht").setLevel(loglevel)
logging.getLogger("btdht").addHandler(stdout_handler)

dht1 = DHT(host='0.0.0.0', port=60000)
dht1.start()
dht1.bootstrap('router.bittorrent.com', 6881)
time.sleep(10)

dht1.ht.add_hash("232db31bfa957866dad7d58cd3a8db1357bbf49c".decode("hex"))

while True:

    print dht1.rt.count()
    print dht1.rt.bad_count()
    print dht1.ht.count_hash_peers("232db31bfa957866dad7d58cd3a8db1357bbf49c".decode("hex"))
    print dht1.ht.count_all_peers()
    time.sleep(3)

dht1.stop()

print "OK"
time.sleep(1000)

