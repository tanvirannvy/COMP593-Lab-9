# importing the package
import tkinter as tk

# creating a new window
window = tk.Tk()
# setting the window size
window.geometry("300x400")
# setting the window title
window.title("Pokemon Data")


# creating frames for user input and info & stats output
frame1 = tk.Frame(window).grid(row=0, column=0)
frame2 = tk.Frame(window).grid(row=1, column=0)

# creating label and entry box in frame1
tk.Label(frame1, text="Pokemon's Name :").grid()
name_var = tk.StringVar()
name_entry = tk.Entry(frame1, textvariable=name_var).grid()

# creating a button inside frame1
def info_action():
 # if no name is entered 
 if name_var.get() == "":
  # print an error message using a dialogue box
  tk.messagebox.showerror("Error", "Please Enter a Valid Pokemons Name!")
 # if a name is entered  
 else:
  # try importing data from the API
  try:
   import requests
   # parsing the data from API by the input
   api_info = parse_data(name_var.get())
   # creating labels and entries
   tk.Label(frame2, text="Types:").grid(column=0, row=0)
   types_var = tk.StringVar()
   types_entry = tk.Entry(frame2, textvariable=types_var).grid(
       column=1, row=0)
   tk.Label(frame2, text="Stats").grid(column=0, row=1)
   # extracting the data
   types_var.set(api_info["types"])
   attack_var = tk.StringVar()
   attack_bar = tk.Scale(
       frame2,
       from_=0,
       to=200,
       orient=tk.HORIZONTAL,
       length=100,
       label="Attack",
   )
   attack_bar.set(api_info["specialAttack"])
   attack_bar.grid(column=1, row=1)
   defence_var = tk.StringVar()
   defence_bar = tk.Scale(
       frame2,
       from_=0,
       to=200,
       orient=tk.HORIZONTAL,
       length=100,
       label="Defence",
   )
   defence_bar.set(api_info["specialDefence"])
   defence_bar.grid(column=1, row=2)
   speed_var = tk.StringVar()
   speed_bar = tk.Scale(
       frame2,
       from_=0,
       to=200,
       orient=tk.HORIZONTAL,
       length=100,
       label="Speed",
   )
   speed_bar.set(api_info["speed"])
   speed_bar.grid(column=1, row=3)

  # if an error occurs due to an invalid pokemon name
  except:
   # prompt an error message using a dialogue box
   tk.messagebox.showerror(
       "Error", "Unable to fetch information for the given name from the PokeAPI"
   )
# creating the button in frame1
tk.Button(frame1, text="Get Info", command=info_action).grid()


# creating a function to parse the data from the API
def parse_data(pokemon_name):
 try:
  # assigning the JSON data to a variable
  pokemon_data = requests.get(
      "https://pokeapi.co/api/v2/pokemon/{}".format(pokemon_name.lower())
  ).json()
  pokemon_type = pokemon_data['types']
  # Empty list for types 
  type_list = [] 
  # Loop over the array in the dictionary 
  for types in pokemon_type: 
   # Append the types to the list 
   type_list.append(types['type']['name']) 
  # Join the array elements with a comma 
  final_types = ','.join(type_list)
  # assigning the stats to variables
  special_attack = pokemon_data.get("stats")[4].get("base_stat")
  special_defence = pokemon_data.get("stats")[5].get("base_stat")
  speed = pokemon_data.get("stats")[0].get("base_stat")

  # return the pokemon type and stats
  return {"types": final_types,
          "specialAttack": special_attack,
          "specialDefence": special_defence,
          "speed": speed}
 except:
  # prompt an error 
  print("Error Occurred")

# run the window
window.mainloop()