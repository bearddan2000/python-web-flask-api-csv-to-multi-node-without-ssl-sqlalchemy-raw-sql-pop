from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine.result import ChunkedIteratorResult
from sqlalchemy.sql import select, delete, insert, update, func

from model import DbModel

class Chained():
    UNSUPPORTED = {"results": "This action is unsupported"}
    def __init__(self, db: sessionmaker) -> None:
        self.db = db

    def jsonify_results(self, collection: ChunkedIteratorResult) -> dict:
        results = []
        for item in collection:
            for obj in item:
                results.append({
                    "id": obj.id,
                    "name": obj.name,
                    "color": obj.color
                })

        return {"results": results}

    def all(self):
        stm = select(DbModel)
        collection: ChunkedIteratorResult = self.db.execute(stm)
        return self.jsonify_results(collection)
        
    def commit_refresh(self, stm, args: dict=None) -> dict:
        if args is not None:
            self.db.execute(statement=stm,params=args)
        else:
            self.db.execute(statement=stm)
        self.db.commit()
        return self.all()
    
    def filter_by(self, pop_id):
        stm = select(DbModel).where(DbModel.id == pop_id)
        collection: ChunkedIteratorResult = self.db.execute(statement=stm)
        return self.jsonify_results(collection)

    def delete_by(self, pop_id: int):
        return self.UNSUPPORTED
    
    def insert_entry(self, pop_name: str, pop_color: str):
        return self.UNSUPPORTED

    def update_entry(self, pop_id: int, pop_name: str, pop_color: str):
        return self.UNSUPPORTED
