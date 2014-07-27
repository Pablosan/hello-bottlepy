from bottle import route, run

@route('/')
def index():
  return "<h1>Hello from bootlepy!</h1>"

# You might want to make these values configurable
run(host='0.0.0.0', port=8003, debug=True)
