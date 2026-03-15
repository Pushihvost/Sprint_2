class EmployeeSalary:

    hourly_payment = 400

    def __init__(self, name, hours, rest_days, email):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email

        #print("Создан объект EmployeeSalary:")
        #print("Имя:", self.name)
        #print("Часы:", self.hours)
        #print("Выходные:", self.rest_days)
        #print("Email:", self.email)

    @classmethod
    def get_hours(cls, name, rest_days, email):
        hours = (7 - rest_days) * 8
        return cls(name, hours, rest_days, email)

    @classmethod
    def get_email(cls, name, hours, rest_days):
        email = f"{name}@email.com"
        return cls(name, hours, rest_days, email)

    @classmethod
    def set_hourly_payment(cls, payment):
        cls.hourly_payment = payment
    
    def salary(self):
        return self.hours * self.hourly_payment

#emp = EmployeeSalary("Alex", 40, 2, "alex@email.com")
#emp2 = EmployeeSalary.get_hours("Nastya", 5, "nastya@email.com")
#EmployeeSalary.get_email("Dima", 30, 3)