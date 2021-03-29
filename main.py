from salary import calculation_salary
from people import get_employees
if __name__ == "__main__":
    name_db = input()
    password_db = input()
    name_user = input()
    department = input()
    name_column1 = input()
    name_column2 = input()
    value_column2 = input()
    count_worker = input()
    size_salary = input()
    calculation_salary(count_worker, size_salary)
    get_employees(name_db, password_db, name_user, department, name_column1, name_column2, value_column2)

