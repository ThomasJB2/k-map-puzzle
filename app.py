from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# @app.route("/")
# def symbols(result):
#     result = "A and B or A and not B"
#     andTarget = "and"
#     orTarget = "or"
#     if andTarget in result:
#         andChar = "∧"
#     else:
#         andChar = ""
#     if orTarget in result:
#         orChar = "∨"
#     else:
#         orChar = ""
#     return render_template("index.html", andChar=andChar, orChar=orChar)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_table', methods=['POST'])
def submit_table():
    # Get the posted JSON data
    table_data = request.get_json()
    
    # Extract the 2D array from the data
    table_2d_array = table_data['data']
    
    # Process the 2D array (this is your Python 2D array now)
    print("Received 2D array:", table_2d_array)

    # You can now work with table_2d_array (for example, save it, process it, etc.)
    

    
    # Respond back to the frontend
    return jsonify({
        'status': 'success',
        'data': table_2d_array
    })

@app.route("/")    
def clean_table(oldArray):
    def remove_first_two_lists(array):
        return array[2:]
    def remove_first_two_elements(list):
        return list[2:]
    cleanerArray = remove_first_two_lists(oldArray)

    list1 = cleanerArray[0]
    list2 = cleanerArray[1]
    list3 = cleanerArray[2]
    list4 = cleanerArray[3]

    clean1 = remove_first_two_elements(list1)
    clean2 = remove_first_two_elements(list2)
    clean3 = remove_first_two_elements(list3)
    clean4 = remove_first_two_elements(list4)

    def combine(list1, list2, list3, list4):
        return [list1, list2, list3, list4]
    cleanArray = combine(clean1, clean2, clean3, clean4)
    return cleanArray

print(clean_table(submit_table()))




if __name__ == "__main__":
    app.run(debug=True)


