from locust import HttpUser, task

class MutantBehavior(HttpUser):
    @task
    def test(self):
        self.client.post("/mutant/", json={
            "dna": [
                "AAAAGA",
                "AGGTGC",
                "ACATGT",
                "TTTAGG",
                "TGACGT",
                "TCACCT",
                "TCACTG"
            ]
        })
