from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data to represent employee records
employees = []

@app.route('/employees', methods=['GET'])
def get_employees():
    return jsonify(employees)

@app.route('/employees', methods=['POST'])
def add_employee():
    employee = request.json
    employees.append(employee)
    return jsonify(employee), 201

@app.route('/employees/<int:employee_id>', methods=['GET'])
def get_employee(employee_id):
    employee = next((emp for emp in employees if emp['id'] == employee_id), None)
    return jsonify(employee) if employee else ('', 404)

@app.route('/employees/<int:employee_id>', methods=['PUT'])
def update_employee(employee_id):
    employee = next((emp for emp in employees if emp['id'] == employee_id), None)
    if employee:
        updates = request.json
        employee.update(updates)
        return jsonify(employee)
    return ('', 404)

@app.route('/employees/<int:employee_id>', methods=['DELETE'])
def delete_employee(employee_id):
    global employees
    employees = [emp for emp in employees if emp['id'] != employee_id]
    return ('', 204)

if __name__ == '__main__':
    app.run(debug=True)