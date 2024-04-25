from flask import Flask

app=Flask(__name__)

@app.route('/')
def welcome():
  return "Welcome to url_building"

@app.route('/success/<int:marks>')
def success(marks):
  return "The person is passed and scored the "+str(marks)

@app.route('/fail/<int:marks>')
def fail(marks):
  return "The person is failed and scored the "+str(marks)
   
###RESULT_CHECKER

@app.route('/results/<int:marks>')
def results(marks):
  results=""
  if(marks>=35):
    return "The person is passed and scored the "+str(marks)
  else:
    return "The person is failed and scored the "+str(marks)

  return redirect(url_for('results'))

if __name__=='__main__':
  app.run(debug=True)

