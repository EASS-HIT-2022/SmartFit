from __future__ import annotations
from email.policy import default
import uuid
from typing import List,Dict, Union
from pydantic import UUID4, BaseModel, Field, conlist


class Food(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    user_input_grams:float = Field(default=0.0)
    food_name: str = Field(..., description="Name of the food")
    brand_name: Union[str,None]
    serving_qty: str = Field(..., description="amount of serving for food")
    serving_unit: str = Field(..., description="any food serving type")
    serving_weight_grams: float = Field(..., description="serving weight grams")
    nf_calories: float = Field(..., description="calories of the food")
    nf_total_fat: float = Field(..., description="fat of the food")
    nf_saturated_fat: float = Field(..., description="saturated fat of the food")
    nf_cholesterol: float = Field(..., description="cholesterol of the food")
    nf_sodium: float = Field(..., description="sodium of the food")
    nf_total_carbohydrate: float = Field(..., description="carbohydrate of the food")
    nf_dietary_fiber: float = Field(..., description="fiber of the food")
    nf_sugars: float = Field(..., description="sugars of the food")
    nf_protein: float = Field(..., description="protein of the food")
    nf_potassium: float = Field(..., description="potassium of the food")
    nf_p:float = Field(...)
    full_nutrients: List[Dict] = [],
    nix_brand_name: Union[str,None]
    nix_brand_id: Union[str,None] = Field(..., description="brand of the food if exists")
    nix_item_name: Union[str,None] = Field(..., description="brand of the food if exists")
    nix_item_id: Union[str,None] = Field(..., description="brand of the food if exists")
    upc: Union[str,None] = Field(..., description="upc of the food if exists")
    consumed_at: Union[str,None]
    metadata: Dict
    source: int
    ndb_no: int
    tags: Dict
    alt_measures: List[Dict]
    lat: None
    lng: None
    meal_type: int
    photo: Dict
    sub_recipe: None
    class_code: None
    brick_code: None
    tag_id: None


    class Config:
        schema_extra = {
            "example":{
                "food_name": "pizza",
                "brand_name": None,
                "serving_qty": 1,
                "serving_unit": "slice",
                "serving_weight_grams": 107,
                "nf_calories": 284.62,
                "nf_total_fat": 10.37,
                "nf_saturated_fat": 4.78,
                "nf_cholesterol": 18.19,
                "nf_sodium": 639.86,
                "nf_total_carbohydrate": 35.66,
                "nf_dietary_fiber": 2.46,
                "nf_sugars": 3.83,
                "nf_protein": 12.19,
                "nf_potassium": 184.04,
                "nf_p": 231.12,
                "full_nutrients": [
                    {
                    "attr_id": 203,
                    "value": 12.1873
                    },
                    {
                    "attr_id": 204,
                    "value": 10.3683
                    },
                    {
                    "attr_id": 205,
                    "value": 35.6631
                    },
                    {
                    "attr_id": 207,
                    "value": 2.5787
                    },
                    {
                    "attr_id": 208,
                    "value": 284.62
                    },
                    {
                    "attr_id": 209,
                    "value": 28.8365
                    },
                    {
                    "attr_id": 210,
                    "value": 0.214
                    },
                    {
                    "attr_id": 211,
                    "value": 0.8346
                    },
                    {
                    "attr_id": 212,
                    "value": 1.07
                    },
                    {
                    "attr_id": 213,
                    "value": 0.4494
                    },
                    {
                    "attr_id": 214,
                    "value": 1.1235
                    },
                    {
                    "attr_id": 221,
                    "value": 0
                    },
                    {
                    "attr_id": 255,
                    "value": 46.1919
                    },
                    {
                    "attr_id": 262,
                    "value": 0
                    },
                    {
                    "attr_id": 263,
                    "value": 0
                    },
                    {
                    "attr_id": 268,
                    "value": 1190.91
                    },
                    {
                    "attr_id": 269,
                    "value": 3.8306
                    },
                    {
                    "attr_id": 287,
                    "value": 0.1391
                    },
                    {
                    "attr_id": 291,
                    "value": 2.461
                    },
                    {
                    "attr_id": 301,
                    "value": 201.16
                    },
                    {
                    "attr_id": 303,
                    "value": 2.6536
                    },
                    {
                    "attr_id": 304,
                    "value": 25.68
                    },
                    {
                    "attr_id": 305,
                    "value": 231.12
                    },
                    {
                    "attr_id": 306,
                    "value": 184.04
                    },
                    {
                    "attr_id": 307,
                    "value": 639.86
                    },
                    {
                    "attr_id": 309,
                    "value": 1.4338
                    },
                    {
                    "attr_id": 312,
                    "value": 0.1124
                    },
                    {
                    "attr_id": 315,
                    "value": 0.3852
                    },
                    {
                    "attr_id": 317,
                    "value": 21.293
                    },
                    {
                    "attr_id": 318,
                    "value": 383.06
                    },
                    {
                    "attr_id": 319,
                    "value": 65.27
                    },
                    {
                    "attr_id": 320,
                    "value": 73.83
                    },
                    {
                    "attr_id": 321,
                    "value": 98.44
                    },
                    {
                    "attr_id": 322,
                    "value": 0
                    },
                    {
                    "attr_id": 323,
                    "value": 0.8881
                    },
                    {
                    "attr_id": 324,
                    "value": 0
                    },
                    {
                    "attr_id": 328,
                    "value": 0
                    },
                    {
                    "attr_id": 334,
                    "value": 0
                    },
                    {
                    "attr_id": 337,
                    "value": 2049.05
                    },
                    {
                    "attr_id": 338,
                    "value": 62.06
                    },
                    {
                    "attr_id": 341,
                    "value": 0.0535
                    },
                    {
                    "attr_id": 342,
                    "value": 1.2733
                    },
                    {
                    "attr_id": 343,
                    "value": 0.3638
                    },
                    {
                    "attr_id": 344,
                    "value": 0.0642
                    },
                    {
                    "attr_id": 345,
                    "value": 0
                    },
                    {
                    "attr_id": 346,
                    "value": 0
                    },
                    {
                    "attr_id": 347,
                    "value": 0
                    },
                    {
                    "attr_id": 401,
                    "value": 1.498
                    },
                    {
                    "attr_id": 404,
                    "value": 0.4173
                    },
                    {
                    "attr_id": 405,
                    "value": 0.2087
                    },
                    {
                    "attr_id": 406,
                    "value": 4.0928
                    },
                    {
                    "attr_id": 415,
                    "value": 0.0856
                    },
                    {
                    "attr_id": 417,
                    "value": 99.51
                    },
                    {
                    "attr_id": 418,
                    "value": 0.4494
                    },
                    {
                    "attr_id": 421,
                    "value": 17.548
                    },
                    {
                    "attr_id": 429,
                    "value": 0
                    },
                    {
                    "attr_id": 430,
                    "value": 7.169
                    },
                    {
                    "attr_id": 431,
                    "value": 55.64
                    },
                    {
                    "attr_id": 432,
                    "value": 42.8
                    },
                    {
                    "attr_id": 435,
                    "value": 138.03
                    },
                    {
                    "attr_id": 454,
                    "value": 29.746
                    },
                    {
                    "attr_id": 502,
                    "value": 0.4387
                    },
                    {
                    "attr_id": 503,
                    "value": 0.6035
                    },
                    {
                    "attr_id": 504,
                    "value": 1.2187
                    },
                    {
                    "attr_id": 505,
                    "value": 0.8239
                    },
                    {
                    "attr_id": 506,
                    "value": 0.2825
                    },
                    {
                    "attr_id": 507,
                    "value": 0.1744
                    },
                    {
                    "attr_id": 508,
                    "value": 0.7105
                    },
                    {
                    "attr_id": 509,
                    "value": 0.5585
                    },
                    {
                    "attr_id": 510,
                    "value": 0.7704
                    },
                    {
                    "attr_id": 511,
                    "value": 0.52
                    },
                    {
                    "attr_id": 512,
                    "value": 0.3799
                    },
                    {
                    "attr_id": 513,
                    "value": 0.4483
                    },
                    {
                    "attr_id": 514,
                    "value": 0.8977
                    },
                    {
                    "attr_id": 515,
                    "value": 3.7825
                    },
                    {
                    "attr_id": 516,
                    "value": 0.3649
                    },
                    {
                    "attr_id": 517,
                    "value": 1.452
                    },
                    {
                    "attr_id": 518,
                    "value": 0.749
                    },
                    {
                    "attr_id": 521,
                    "value": 0
                    },
                    {
                    "attr_id": 601,
                    "value": 18.19
                    },
                    {
                    "attr_id": 605,
                    "value": 0.2579
                    },
                    {
                    "attr_id": 606,
                    "value": 4.7776
                    },
                    {
                    "attr_id": 607,
                    "value": 0.1081
                    },
                    {
                    "attr_id": 608,
                    "value": 0.0856
                    },
                    {
                    "attr_id": 609,
                    "value": 0.0589
                    },
                    {
                    "attr_id": 610,
                    "value": 0.1509
                    },
                    {
                    "attr_id": 611,
                    "value": 0.1873
                    },
                    {
                    "attr_id": 612,
                    "value": 0.6441
                    },
                    {
                    "attr_id": 613,
                    "value": 2.4589
                    },
                    {
                    "attr_id": 614,
                    "value": 0.9181
                    },
                    {
                    "attr_id": 615,
                    "value": 0.0225
                    },
                    {
                    "attr_id": 617,
                    "value": 2.5552
                    },
                    {
                    "attr_id": 618,
                    "value": 1.5654
                    },
                    {
                    "attr_id": 619,
                    "value": 0.1894
                    },
                    {
                    "attr_id": 620,
                    "value": 0.0128
                    },
                    {
                    "attr_id": 621,
                    "value": 0
                    },
                    {
                    "attr_id": 624,
                    "value": 0.015
                    },
                    {
                    "attr_id": 625,
                    "value": 0.0514
                    },
                    {
                    "attr_id": 626,
                    "value": 0.1252
                    },
                    {
                    "attr_id": 627,
                    "value": 0.0021
                    },
                    {
                    "attr_id": 628,
                    "value": 0.0396
                    },
                    {
                    "attr_id": 629,
                    "value": 0.0043
                    },
                    {
                    "attr_id": 630,
                    "value": 0.0021
                    },
                    {
                    "attr_id": 631,
                    "value": 0.0043
                    },
                    {
                    "attr_id": 645,
                    "value": 2.7906
                    },
                    {
                    "attr_id": 646,
                    "value": 1.7987
                    },
                    {
                    "attr_id": 652,
                    "value": 0.0685
                    },
                    {
                    "attr_id": 653,
                    "value": 0.046
                    },
                    {
                    "attr_id": 654,
                    "value": 0.0086
                    },
                    {
                    "attr_id": 662,
                    "value": 0.0235
                    },
                    {
                    "attr_id": 663,
                    "value": 0.1723
                    },
                    {
                    "attr_id": 664,
                    "value": 0
                    },
                    {
                    "attr_id": 670,
                    "value": 0.0417
                    },
                    {
                    "attr_id": 671,
                    "value": 0.0011
                    },
                    {
                    "attr_id": 672,
                    "value": 0.0032
                    },
                    {
                    "attr_id": 673,
                    "value": 0.1006
                    },
                    {
                    "attr_id": 674,
                    "value": 2.3829
                    },
                    {
                    "attr_id": 675,
                    "value": 1.4627
                    },
                    {
                    "attr_id": 676,
                    "value": 0.0021
                    },
                    {
                    "attr_id": 685,
                    "value": 0.0032
                    },
                    {
                    "attr_id": 687,
                    "value": 0.0161
                    },
                    {
                    "attr_id": 689,
                    "value": 0.0107
                    },
                    {
                    "attr_id": 693,
                    "value": 0.1958
                    },
                    {
                    "attr_id": 695,
                    "value": 0.061
                    },
                    {
                    "attr_id": 697,
                    "value": 0
                    },
                    {
                    "attr_id": 851,
                    "value": 0.1873
                    },
                    {
                    "attr_id": 852,
                    "value": 0
                    },
                    {
                    "attr_id": 853,
                    "value": 0.0096
                    },
                    {
                    "attr_id": 858,
                    "value": 0.0043
                    }
                ],
                "nix_brand_name": None,
                "nix_brand_id": None,
                "nix_item_name": None,
                "nix_item_id": None,
                "upc": None,
                "consumed_at": "2022-06-06T12:24:59+00:00",
                "metadata": {
                    "is_raw_food": False
                },
                "source": 1,
                "ndb_no": 21299,
                "tags": {
                    "item": "pizza",
                    "measure": None,
                    "quantity": "1.0",
                    "food_group": 8,
                    "tag_id": 1060
                },
                "alt_measures": [
                    {
                    "serving_weight": 107,
                    "measure": "slice",
                    "seq": 1,
                    "qty": 1
                    },
                    {
                    "serving_weight": 853,
                    "measure": "pizza",
                    "seq": 2,
                    "qty": 1
                    },
                    {
                    "serving_weight": 170,
                    "measure": "large slice",
                    "seq": 80,
                    "qty": 1
                    },
                    {
                    "serving_weight": 80,
                    "measure": "medium slice",
                    "seq": 81,
                    "qty": 1
                    },
                    {
                    "serving_weight": 65,
                    "measure": "small slice",
                    "seq": 82,
                    "qty": 1
                    },
                    {
                    "serving_weight": 853,
                    "measure": "large pizza",
                    "seq": 83,
                    "qty": 1
                    },
                    {
                    "serving_weight": 640,
                    "measure": "medium pizza",
                    "seq": 84,
                    "qty": 1
                    },
                    {
                    "serving_weight": 390,
                    "measure": "small pizza",
                    "seq": 85,
                    "qty": 1
                    },
                    {
                    "serving_weight": 225,
                    "measure": "personal pan pizza",
                    "seq": 86,
                    "qty": 1
                    },
                    {
                    "serving_weight": 56.25,
                    "measure": "personal pan pizza slice",
                    "seq": 87,
                    "qty": 1
                    },
                    {
                    "serving_weight": 100,
                    "measure": "g",
                    "seq": None,
                    "qty": 100
                    },
                    {
                    "serving_weight": 28.3495,
                    "measure": "wt. oz",
                    "seq": None,
                    "qty": 1
                    }
                ],
                "lat": None,
                "lng": None,
                "meal_type": 1,
                "photo": {
                    "thumb": "https://nix-tag-images.s3.amazonaws.com/1060_thumb.jpg",
                    "highres": "https://nix-tag-images.s3.amazonaws.com/1060_highres.jpg",
                    "is_user_uploaded": False
                },
                "sub_recipe": None,
                "class_code": None,
                "brick_code": None,
                "tag_id": None
                },
    }
