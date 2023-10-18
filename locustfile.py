import random
import time

from locust import HttpUser, between, task


class ChatUser(HttpUser):
    wait_time = between(5, 20)

    @task
    def ask_question(self):
        self.client.get("/")
        time.sleep(5)
        self.client.post(
            "/chat",
            json={
                "history": [
                    {
                        "content": random.choice(
                            [
                                "What are the different job roles involved in managing, controlling, and using data?",
                                "How has the increase in data generated affected data professionals?",
                                "Can you provide an example of a table structure in Azure Cosmos DB for Apache Cassandra?",
                                "What is the syntax used to retrieve a specific record in Azure Cosmos DB for Apache Cassandra?",
                            ]
                        ),
                        "role": "user",
                    },
                ],
                "overrides": {
                    "retrieval_mode": "hybrid",
                    "semantic_ranker": True,
                    "semantic_captions": False,
                    "top": 3,
                    "suggest_followup_questions": False,
                },
            },
        )
        time.sleep(5)
        self.client.post(
            "/chat",
            json={
                "history": [
                    {"content": "How has the increase in data generated affected data professionals?", "role": "user"},
                    {
                        "content": "The increase in data generated has led to the emergence of new technologies, roles, and approaches in the field of data, affecting data professionals [info-3.pdf].",
                        "role": "assistant",
                    },
                    {"content": "What are the responsibilities of a data engineer in defining and managing data pipelines?", "role": "user"},
                ],
                "overrides": {
                    "retrieval_mode": "hybrid",
                    "semantic_ranker": True,
                    "semantic_captions": False,
                    "top": 3,
                    "suggest_followup_questions": False,
                },
            },
        )
