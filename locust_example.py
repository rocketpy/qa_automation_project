# Origin taked from here:  https://habr.com/ru/company/infopulse/blog/430810/

import random as rnd
from locust import HttpLocust, TaskSet, task


class UserBehavior(TaskSet):
    @task(1)
    def check_albums(self):
        photo_id = rnd.randint(1, 5000)
        with self.client.get(f'/photos/{photo_id}', catch_response=True, name='/photos/[id]') as response:
            if response.status_code == 200:
                album_id = response.json().get('albumId')
                if album_id % 10 != 0:
                    response.success()
                else:
                    response.failure(f'album id cannot be {album_id}')
            else:
                response.failure(f'status code is {response.status_code}')


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 1000
    max_wait = 2000

#  
"""
from locust import HttpLocust, TaskSet, task

class FlowException(Exception):
    pass

class UserBehavior(TaskSet):
    @task(1)
    def check_flow(self):
        # step 1
        new_post = {'userId': 1, 'title': 'my shiny new post', 'body': 'hello everybody'}
        post_response = self.client.post('/posts', json=new_post)
        if post_response.status_code != 201:
            raise FlowException('post not created')
        post_id = post_response.json().get('id')

        # step 2
        new_comment = {
            "postId": post_id,
            "name": "my comment",
            "email": "test@user.habr",
            "body": "Author is cool. Some text. Hello world!"
        }
        comment_response = self.client.post('/comments', json=new_comment)
        if comment_response.status_code != 201:
            raise FlowException('comment not created')
        comment_id = comment_response.json().get('id')

        # step 3
        self.client.get(f'/comments/{comment_id}', name='/comments/[id]')
        if comment_response.status_code != 200:
            raise FlowException('comment not read')


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 1000
    max_wait = 2000
"""

# Making the load realistic
from locust import HttpLocust, TaskSet, task
import random as r

class UserBehavior(TaskSet):
   created_posts = []

   @task(1)
   def create_post(self):
       new_post = {'userId': 1, 'title': 'my shiny new post', 'body': 'hello everybody'}
       post_response = self.client.post('/posts', json=new_post)
       if post_response.status_code != 201:
           return
       post_id = post_response.json().get('id')
       self.created_posts.append(post_id)

   @task(10)
   def read_post(self):
       if len(self.created_posts) == 0:
           return
       post_id = r.choice(self.created_posts)
       self.client.get(f'/posts/{post_id}', name='read post')


class WebsiteUser(HttpLocust):
   task_set = UserBehavior
   min_wait = 1000
   max_wait = 2000

