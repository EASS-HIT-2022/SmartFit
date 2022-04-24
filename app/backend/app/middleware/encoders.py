# # -*- coding: utf-8 -*-
# # -----------------------------------
# # @CreateTime   : 2020/7/25 0:27
# # @Author       : Mark Shawn
# # @Email        : shawninjuly@gmail.com
# # ------------------------------------

# from typing import Callable, Union
# import json
# from datetime import datetime, date
# from uuid import UUID
# from bson import ObjectId
# from fastapi import Request
# from httpcore import request
# from pydantic import BaseModel


# # def mongo_json_encoder(record: Union[dict, list, BaseModel]):
# #     """
# #     This is a json_encoder designed specially for dump mongodb records.

# #     It can deal with both record_item and record_list type queried from mongodb.

# #     You can extend the encoder ability in the recursive function `convert_type`.

# #     I just covered the following datatype: datetime, date, UUID, ObjectID.

# #     Contact me if any further support needs.

# #     Attention: it will change the raw record, so copy it before operating this function if necessary.

# #     Parameters
# #     ----------
# #     **record**: a dict or a list, like the queried documents from mongodb.

# #     Returns
# #     -------
# #     json formatted data.
# #     """

# #     def convert_type(data):
# #         if isinstance(data, (datetime, date)):
# #             # ISO format: data.isoformat()
# #             return str(data)
# #         elif isinstance(data, (UUID, ObjectId)):
# #             return str(data)
# #         elif isinstance(data, list):
# #             return list(map(convert_type, data))
# #         elif isinstance(data, dict):
# #             return mongo_json_encoder(data)
# #         try:
# #             json.dumps(data)
# #             return data
# #         except TypeError:
# #             raise TypeError({
# #                 "error_msg": "暂不支持此类型序列化",
# #                 "key": key,
# #                 "value": value,
# #                 "type": type(value)
# #             })

# #     # add support for BaseModel
# #     if isinstance(record, BaseModel):
# #         return mongo_json_encoder(record.dict(by_alias=True))
# #     elif isinstance(record, dict):
# #         for key, value in record.items():
# #             record[key] = convert_type(value)
# #         return record
# #     else:
# #         return list(map(mongo_json_encoder, record))


# # def mongo_json_encoder_decorator(func):
# #     """
# #     this is a decorator for converting the queried documents from mongodb

# #     Parameters
# #     ----------
# #     func

# #     Returns
# #     -------

# #     """
# #     def wrapper(*args, **kwargs):
# #         res = func(*args, **kwargs)
# #         return mongo_json_encoder(res)
# #     return wrapper


# class JSONEncoder(json.JSONEncoder):
#     def __init__(self):
#         pass

#     async def __call__(self, Request: Request, call_next: Callable):
#         content = Request.headers.get('Content-Type')
#         if isinstance(content, ObjectId):
#             content = str(content)
#         if isinstance(content, datetime):
#             if content == datetime().now():
#                 content = str(datetime.now())
#         content = json.JSONEncoder.default(self, content)
#         response = await call_next(content)

#         return response
