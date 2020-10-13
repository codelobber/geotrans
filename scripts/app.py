from database import init_db
from flask import Flask
from flask_graphql import GraphQLView
from schema import schema

app = Flask(__name__)
app.debug = True

default_query = '''
{
  allPoints {
    edges {
      node {
        name,
        latitude,
       	longitud,
        phone,
        due
      }
    }
  }
}
'''.strip()

add_query = '''
mutation myFirstMutation {
    add(name:"Peter", latitude: "0", longitud: "0", phone: "0", due: "2020-09-25T18:37:44.586000" ) {
        result {
            name
        }
    }
}
'''.strip()

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True)
)
@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    init_db()
    app.run(host= '0.0.0.0')