from flask import Flask, request
import json
app = Flask(__name__)

petList = []

class Pet:
	name=""
	species=""
	age=0

	def __init__(self, nameIn, speciesIn, ageIn):
		self.name=nameIn
		self.species=speciesIn
		self.age=ageIn

	def getJson(self):
		return "{\"name\": \"" + self.name + "\", \"species\": \"" + self.species + "\", \"age\": " + str(self.age) + "}"

def getPetsInJosn(listIn):
	out="["
	for i in range(0, len(listIn)):
		out+=listIn[i].getJson()
		if (i<len(listIn)-1):
			out+=", "
	out+="]"
	return out

petList.append(Pet("Spot", "dog", 3))
petList.append(Pet("Dot", "cat", 7))

@app.route("/pets", methods = ["GET"])
def getAllPets():
	out=getPetsInJosn(petList)
	return out, 200

@app.route("/pets", methods = ["POST"])
def createPet():
	result=request.form
	name=result["name"]
	species=result["species"]
	age=result["age"]
	if name!=None and species!=None and age!=None:
		pet=Pet(name, species, age)
		petList.append(pet)
		return pet.getJson(), 200
	else:
		return '{"error": "you didn\'t send a name, a species and an age"}', 400


if __name__ == "__main__":
    app.run()
