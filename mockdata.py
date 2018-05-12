import random 
import datetime

from main import User, Tag, Post, db

user = User.query.get(1)
tag_1 = Tag(u'python')
tag_2 = Tag(u'Flask')
tag_3 = Tag(u'Jinja')
tag_4 = Tag(u'Sql')
tag_list = [ tag_1, tag_2, tag_3, tag_4 ]

s = 'demo text'

for i in xrange(100):
  new_post = Post('Post' + str(i))
  new_post.user = user
  new_post.publish_date = datetime.datetime.now()
  new_post.text = s
  new_post.tags = random.sample(tag_list, random.randint(1, 3))
  db.session.add(new_post)

db.session.commit()
