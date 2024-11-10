from neo4j import GraphDatabase

class MemoryAgent:
    def __init__(self, uri: str = "bolt://localhost:7687", user: str = "neo4j", password: str = "password"):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def save_preferences(self, user_id: str, preferences: dict):
        session = self.driver.session()
        session.run("MERGE (u:User {id: $user_id}) SET u.preferences = $preferences", 
                    user_id=user_id, preferences=preferences)
        session.close()

    def get_preferences(self, user_id: str):
        session = self.driver.session()
        result = session.run("MATCH (u:User {id: $user_id}) RETURN u.preferences", user_id=user_id)
        preferences = result.single()
        session.close()
        return preferences
