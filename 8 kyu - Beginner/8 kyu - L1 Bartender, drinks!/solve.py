def get_drink_by_profession(param):
    dict = {
         "Jabroni"         :	"Patron Tequila",
         "School Counselor":	"Anything with Alcohol",
         "Programmer"      :	"Hipster Craft Beer",
         "Bike Gang Member":	"Moonshine",
         "Politician"      :	"Your tax dollars", 
         "Rapper"          :	"Cristal" 
    }
    return dict.get(param.title(), "Beer")