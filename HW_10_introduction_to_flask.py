from flask import Flask

app = Flask(__name__)


@app.route('/avr_data')
def get_avr_data():
    with open('hw.csv', 'r') as students_file:
        data = [row.strip().split(', ') for row in students_file][1:-1]
    # get average height, convert from inches to centimeters
    height_lst = list(map(lambda x: float(x[1]), data))
    avg_height_cm = round(sum(height_lst)/len(height_lst) * 2.54, 2)
    # get average weight, convert from pounds to kilograms
    weight_lst = list(map(lambda x: float(x[2]), data))
    avg_weight_kg = round(sum(weight_lst) / len(weight_lst) * 0.45359237, 2)
    return f'Average height: {avg_height_cm} cm<br>Average weight: {avg_weight_kg} kg'


@app.route('/requirements')
def get_requirements():
    with open('requirements.txt', 'r') as requirements_file:
        data = requirements_file.read().replace('\n', '<br>')
    return f'<h2>Required packages:</h2> <h3>{data}</h3>'


if __name__ == "__main__":
    app.run(debug=True, port=5000)
