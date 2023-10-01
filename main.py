import logging

import dy

if __name__ == '__main__':
    LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
    logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT)

    # dy.parseLiveRoomUrl("https://live.douyin.com/31598223623")
    dy.parseLiveRoomUrl("https://live.douyin.com/443876969868")

