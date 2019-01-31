import time
import logging


logger = logging.getLogger(__name__)

logging.basicConfig(level=logging.DEBUG)

handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

logger.propagate = False


def app(environ, start_response):
    logger.info('Entered app')
    data = b"Hello, World!\n"
    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(data)))
    ])
    # Intentionally lower than nginx timeout, so few requests can complete
    time.sleep(10)
    logger.info('Gonna return the response from app')
    return iter([data])
