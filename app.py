from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
#this decorator tells the computer to execute the program in an internet browser of the computer
def visitors():

    # Load current count
    counter_read_file = open("count.txt", "r")
    visitors_count = int(counter_read_file.read())
    counter_read_file.close()

    # Increment the count
    visitors_count = visitors_count + 1

    # Overwrite the count
    counter_write_file = open("count.txt", "w")
    counter_write_file.write(str(visitors_count))
    counter_write_file.close()

    # Render HTML with count variable
    return render_template("index.html", count=visitors_count)

@app.route('/', methods=['POST']) #POST method will help us to fetch data from the input field.

def covid_stats():
    # Load current count
    counter_read_file = open("count.txt", "r")
    visitors_count = int(counter_read_file.read())
    counter_read_file.close()

    text = request.form['text']
    """ the request is a function imported from the flask library. It
    works as a middle man between Python code and HTML code."""

    corona_data = 'https://covid-api-262.herokuapp.com/?country='+text
    print(corona_data)
    return render_template("index.html", image=corona_data, count=visitors_count)

if __name__ == "__main__":
    app.run()
"""we will check if still, we are under flask code by writing the if
condition and if the condition satisfies then we will run our flask application by
using run() function followed by the variable app which holds the initialization
of flask.
"""
