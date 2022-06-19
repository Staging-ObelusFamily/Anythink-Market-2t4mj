from sqlalchemy import create_engine
from sqlalchemy.sql import text

engine = create_engine('postgresql://user:@postgres:5432', echo=True)

user_insert_statement = text("""INSERT INTO users(username, email, salt, bio, hashed_password) VALUES(:username, :email, :salt, :bio, :hashed_password)""")
select_last_user_id = text("""SELECT * FROM users ORDER BY id DESC LIMIT 1""")
item_statement = text("""INSERT INTO items(slug, title, description, seller_id) VALUES(:slug, :title, :description, :seller_id)""")
select_last_item_id = text("""SELECT * FROM items ORDER BY id DESC LIMIT 1""")
comment_statement = text("""INSERT INTO commentaries(body, seller_id, item_id) VALUES(:body, :seller_id, :item_id)""")

clear_users = text("""DELETE FROM users""")
clear_items = text("""DELETE FROM items""")
clear_comments = text("""DELETE FROM commentaries""")

with engine.connect() as con:
    con.execute(clear_users)
    con.execute(clear_items)
    con.execute(clear_comments)

    for i in range(100):
        user = {'username': f'username{i}', 'email':f'a{i}@a.com', 'salt': 'abc', 'bio': 'bio', 'hashed_password':'12345689'}
        con.execute(user_insert_statement, **user)

        result = con.execute(select_last_user_id)
        for row in result:
            generated_user_id = row['id']

        item = {'slug':f'slug{i}', 'title':f'title{i}','description':f'desc{i}', 'seller_id':generated_user_id}
        con.execute(item_statement, **item)

        item_result = con.execute(select_last_item_id)
        for row in item_result:
            generated_item_id = row['id']
        comment = {'body': f'comment{i}', 'seller_id': generated_user_id, 'item_id': generated_item_id}
        con.execute(comment_statement, **comment)