#!/usr/bin/python3
# coding: utf-8
from redis import Redis

config = {
    'host': '127.0.0.1',
    'port': 6379,
    'db': 5,
    'decode_responses': True
}


rd_client = Redis(**config)

if __name__ == '__main__':
    rd_client.keys('*')