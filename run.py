import utils
import datetime
import logging
import asyncio
from api import user_request, stream_request
from session import startRecord
from multiprocessing import Pool

if __name__ == "__main__":
    logging.basicConfig(
        filename = f'{datetime.datetime.utcnow()}_log.log', 
        level = logging.INFO
    )
    logging.info ('[INFO] Starting ProjectX v0.1 Beta')
    streamers = utils.appendText("streamers.txt")
    logging.info ('[INFO] Loading Streamers Information')
    for id in streamers:
        data = user_request (id)
        logging.info (f'[INFO] User Confirmed : {data["data"][0]["display_name"]} ({id})')
    while True:
        if not streamers:
            break
        for id in streamers:
            data = stream_request (id)
            if len(data["data"]) > 0 :
                logging.info (f'[INFO] Detected streams for {id}, making a record session')
                startRecord (id)
                streamers.remove (id)
            else :
                logging.info (f'[INFO] Not Detected streams for {id}, keep going')
    