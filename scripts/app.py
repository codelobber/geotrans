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
    add(name:"Тестовский Янович", latitude: "55.69343638", longitud: "37.60618714", phone: "79857273129", due: "2020-11-25T18:37:44.586000" ) {
        success
    }
}
'''.strip()

config_query = '''
{
  config(version: 1) {
        allowedRadius,
        isDayPeriodAllowed
  }
}
'''.strip()

set_config_query = '''
mutation myFirstMutation {
    config(version: 1, isDayPeriodAllowed: true, allowedRadius: 100) {
        success
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