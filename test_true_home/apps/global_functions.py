import uuid

def get_cleaned_uuid():
    uuid_ = (str(uuid.uuid1()).replace('-', ''))
    return uuid_
