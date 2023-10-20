from bson import ObjectId


class CollectionMock:
    """Mocked collection of measurements."""

    def __init__(self, data: list[dict] = []):
        self.data: list[dict] = data

    def find(self):
        return self.data

    def insert_one(self, document):
        self.data.append(document)
        document["_id"] = ObjectId()
        return document


measurements_collection_mock = CollectionMock(
    [
        {
            "_id": ObjectId(),
            "thickness": 2.5,
            "cookTime": 90,
            "doneness": "RARE",
        },
        {
            "_id": ObjectId(),
            "thickness": 2.5,
            "cookTime": 120,
            "doneness": "MEDIUM",
        },
    ]
)
