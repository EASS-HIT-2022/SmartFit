from motor.motor_asyncio import (
    AsyncIOMotorClient as MotorClient,
)
import motor.core
import asyncio
import logging
from motor.motor_asyncio import AsyncIOMotorClient


class MongoManager:
    client: AsyncIOMotorClient = None
    db = None

    async def connect_to_database(self, path: str, db_name: str):
        logging.info("Connecting to MongoDB.")
        self.client = AsyncIOMotorClient(path)
        self.client.get_io_loop = asyncio.get_running_loop
        self.db = self.client[db_name]
        logging.info("Connected to MongoDB.")

    def close_database_connection(self):
        logging.info("Closing connection with MongoDB.")
        self.client.close()
        logging.info("Closed connection with MongoDB.")

    def get_collection(self, collection_name: str):
        return self.db[collection_name]


