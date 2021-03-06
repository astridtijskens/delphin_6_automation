__author__ = "Christian Kongsgaard"
__license__ = "MIT"
__version__ = "0.0.1"

# -------------------------------------------------------------------------------------------------------------------- #
# IMPORTS

from datetime import datetime

# Modules:
import mongoengine

# RiBuild Modules:
import delphin_6_automation.database_interactions.database_collections as collections


#from delphin_6_automation.nosql.db_templates import delphin_entry as delphin_db

# -------------------------------------------------------------------------------------------------------------------- #
# RESULT CLASS


class Result(mongoengine.Document):

    added_date = mongoengine.DateTimeField(default=datetime.now)
    delphin = mongoengine.GenericReferenceField(required=True)
    results_processed = mongoengine.GenericReferenceField()

    log = mongoengine.DictField(required=True)
    results = mongoengine.DictField(required=True)
    geometry_file = mongoengine.DictField(required=True)
    geometry_file_hash = mongoengine.IntField(required=True)
    simulation_started = mongoengine.DateTimeField(required=True)

    meta = collections.raw_result_db


