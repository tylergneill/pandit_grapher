# data models

from typing import List, Dict


class Entity:
    def __init__(self, entity_id: str):
        self.id: str = entity_id
        self.type: str = ''  # "work" or "author"
        self.name: str = ''  # work title or author name

    def __str__(self) -> str:
        """String representation of the entity with newline-separated fields."""
        fields = vars(self)  # Get all fields as a dictionary
        return "\n".join(f"{key}: {value}" for key, value in fields.items())

    @staticmethod
    def from_dict(data: Dict):
        """Create an Entity instance (or subclass) from a dictionary."""
        entity_type = data.get("type", "entity")
        if entity_type == "work":
            return Work.from_dict(data)
        elif entity_type == "author":
            return Author.from_dict(data)
        else:
            raise ValueError(f"Unknown entity type: {entity_type}")

    def to_dict(self) -> Dict:
        """Convert an Entity instance to a dictionary."""
        return {
            "id": self.id,
            "name": self.name
        }


class Work(Entity):
    def __init__(self, entity_id: str):
        super().__init__(entity_id)
        self.type: str = "work"
        self.author_ids: List[str] = []
        self.base_text_ids: List[str] = []
        self.commentary_ids: List[str] = []

    @staticmethod
    def from_dict(data: Dict) -> "Work":
        work = Work(data["id"])
        work.name = data.get("name", "")
        work.author_ids = data.get("author_ids", [])
        work.base_text_ids = data.get("base_text_ids", [])
        work.commentary_ids = data.get("commentary_ids", [])
        return work

    def to_dict(self) -> Dict:
        """Convert a Work instance to a dictionary."""
        return {
            **super().to_dict(),
            "type": self.type,
            "author_ids": self.author_ids,
            "base_text_ids": self.base_text_ids,
            "commentary_ids": self.commentary_ids,
        }


class Author(Entity):
    def __init__(self, entity_id: str):
        super().__init__(entity_id)
        self.type: str = "author"
        self.work_ids: List[str] = []

    @staticmethod
    def from_dict(data: Dict) -> "Author":
        author = Author(data["id"])
        author.name = data.get("name", "")
        author.work_ids = data.get("work_ids", [])
        return author

    def to_dict(self) -> Dict:
        """Convert an Author instance to a dictionary."""
        return {
            **super().to_dict(),
            "type": self.type,
            "work_ids": self.work_ids,
        }
