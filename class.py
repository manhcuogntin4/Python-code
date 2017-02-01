class Student:
	def __init__(self, name):
		self.name=name
	def set_age(self, age):
		self.age=age
st=Student("Nguyen")
print st.name
st.set_age(20)
print st.age
class Super(Student):
	def __init__(self, discipline):
		self.discipline=discipline
su=Super("Math")
su.set_age(30)
print su.discipline
print su.age