from locust import HttpLocust, TaskSet, task

class UserBehavior(TaskSet):
    @task(1)
    def applications(self):
        self.client.get("/applications")

    @task(2)
    def loadBalancers(self):
        self.client.get("/loadBalancers?provider=kubernetes")

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 1
    max_wait = 2
