
from flask import Flask, jsonify
from database_credentials import conn
import csv

app = Flask(__name__)


@app.route('/create_table/', methods=['POST'])
def create_table():
    cursor = conn.cursor()
    query_1 = 'create table if not exists _students_data (student_Id integer, first_name varchar(200), last_name varchar(200),' + \
                                                         ' gender varchar(50), age integer, email varchar(200), mobile varchar(20),' +\
                                                         ' Education varchar(200), rating integer)'    
                                                         
    cursor.execute(query_1)
    cursor.close()
    conn.close()
    
    return jsonify({'message': 'table created'})


@app.route('/insert_data/', methods=['POST'])
def insert_student_data():
    cursor = conn.cursor()                                                         
    query1 = 'insert into _students_data (student_Id, first_name, last_name, gender, age, email, mobile, Education, rating) values '

    with open('C:\\Users\\91807\\Downloads\\students_data_table_new.csv', mode='r', newline='\n') as f:
        reader = csv.reader(f, delimiter=',')
        data = list(reader)[1:]
    # print(data)
        
    for rec in data:
        print(query1 + str(tuple(rec)))
        cursor.execute(query1 + str(tuple(rec)))
    conn.commit()
    cursor.close()
    conn.close()
    
    return jsonify({'message': 'data inserted into database'})


@app.route('/get_data/<int:Student_Id>')
def get_student_record(Student_Id):
    cursor = conn.cursor()
    query = 'select * from _students_data where student_Id = ' + str(Student_Id)
    cursor.execute(query)
    print('444444444444444444444444444444')
    res = list(cursor)

    if res:
        return {'message': 'record found',
                'data': res}
    else:
        return {'message': 'no data found'}
        
    
if __name__ == '__main__':
    app.run()