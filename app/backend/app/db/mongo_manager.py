import logging
from motor.motor_asyncio import AsyncIOMotorClient
from motor.motor_tornado import MotorDatabase


class MongoManager:
    client: AsyncIOMotorClient = None
    db: MotorDatabase = None

    def connect_to_database(self, path: str, db_name: str):
        logging.info("Connecting to MongoDB.")
        self.client = AsyncIOMotorClient(path)
        self.db = self.client[db_name]
        logging.info("Connected to MongoDB.")

    def close_database_connection(self):
        logging.info("Closing connection with MongoDB.")
        self.client.close()
        logging.info("Closed connection with MongoDB.")

    def get_users(self):
        users_query = self.db.users.find({}, {'_id': 0})
        return list(users_query)

    def get_collection(self, collection_name: str):
        return self.db[collection_name]
