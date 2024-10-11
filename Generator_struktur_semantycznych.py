#!/usr/bin/env python
# coding: utf-8

# In[8]:


import tkinter as tk
from tkinter import ttk, messagebox

# Data
nouns = [
    "cat", "dog", "book", "car", "table", "chair", "apple", "bicycle", "computer", "phone", 
    "flower", "river", "mountain", "city", "street", "school", "teacher", "student", "friend", 
    "photo", "bread", "key", "shoe", "hat", "watch", "lamp", "star", "pen", "club",
    "cloud", "fish", "fruit", "leaf", "egg", "box", "cup", "ball", "pencil", "notebook", 
    "cookie", "task", "drum", "soup", "skirt", "ticket", "sandwich", "coat", "lamp"
]

pronouns_singular = ["I", "you", "he", "she", "it"]
pronouns_plural = ["we", "you", "they"]

verbs = [
    "agree", "applaud", "arrive", "belong", "calculate", "clean", "decide", "deliver", 
    "deny", "develop", "discover", "enjoy", "explain", "fail", "follow", "help", "involve", 
    "invite", "jump", "kiss", "listen", "live", "look", "manage", "need", "open", "plan", 
    "play", "prefer", "protect", "remind", "respond", "save", "share", "smile", "start", 
    "study", "suggest", "taste", "test", "thank", "trade", "try", "use", "visit", "wait", 
    "work"
]

adjectives = [
    "red", "blue", "green", "big", "small", "happy",
    "sad", "fast", "slow", "bright", "dark", "light",
    "heavy", "thin", "thick", "long", "short", "tall",
    "young", "old", "new", "ancient", "clean", "dirty",
    "smooth", "rough", "soft", "hard", "sweet", "bitter",
    "spicy", "sour", "funny", "serious", "calm", "noisy"
]

tenses = ["Present", "Past", "Future"]
moods = ["Indicative", "Imperative"]

# Function to generate a sentence
def generate_sentence(subject, verb, obj):
    return f"{subject} {verb} {obj}"

def update_subject_entries(event):
    subject_type = subject_type_combobox.get()
    subject_plur = subject_combobox.get()

    if subject_type == "Noun":
        subject_entry.grid(row=5, column=1)
        subject_entry.config(values=nouns)
    elif subject_type == "Pronoun":
        subject_entry.grid(row=5, column=1)
        subject_entry.config(values=pronouns_plural if subject_plur == "Plural" else pronouns_singular)

def update_adjective_entries(event):
    if subject_adj_combobox.get() == "Yes":
        subject_adj_combobox.grid(row=4, column=1)
        subject_adj_combobox.config(values=adjectives)

def update_object_entries(event):
    object_type = object_type_combobox.get()
    object_plur = object_combobox.get()

    if object_type == "Noun":
        object_entry.grid(row=12, column=1)
        object_entry.config(values=nouns)
    elif object_type == "Pronoun":
        object_entry.grid(row=12, column=1)
        object_entry.config(values=pronouns_plural if object_plur == "Plural" else pronouns_singular)

def update_object_adjective_entries(event):
    if object_adj_combobox.get() == "Yes":
        object_adj_label.grid(row=11, column=0)
        object_adj_combobox.grid(row=11, column=1)
        object_adj_combobox.config(values=adjectives)


# Function to gather data from GUI
def on_submit():
    subject_type = subject_type_combobox.get()
    subject = subject_entry.get()
    verb = verb_combobox.get()
    obj_type = object_type_combobox.get()
    obj = object_entry.get()

    if subject and verb and obj:
        tense = tense_combobox.get()
        mood = mood_combobox.get()

        # Prepare verb form based on tense
        verb_form = verb
        if tense == "Past":
            verb_form = f"{verb}ed"
        elif tense == "Future":
            verb_form = f"will {verb}"

        # Prepare subject form with adjective if selected
        if subject_adj_combobox.get():
            subject_adj = subject_adj_combobox.get()
            subject = subject_adj + " " + subject
        
        # Prepare object form with adjective if selected
        if object_adj_combobox.get():
            obj_adj = object_adj_combobox.get()
            obj = obj_adj + " " + obj
            
        # Generate the final sentence
        sentence = generate_sentence(subject, verb_form, obj)
        messagebox.showinfo("Generated Sentence", sentence)
    else:
        messagebox.showwarning("Input Error", "Please fill in all fields.")

# GUI Setup
root = tk.Tk()
root.title("Sentence Generator")

# Subject Type
tk.Label(root, text="Subject Type:").grid(row=0, column=0)
subject_type_combobox = ttk.Combobox(root, values=["Noun", "Pronoun"])
subject_type_combobox.grid(row=0, column=1)
subject_type_combobox.bind("<<ComboboxSelected>>", update_subject_entries)

# Subject Plurality
tk.Label(root, text="Singular or Plural?").grid(row=1, column=0)
subject_combobox = ttk.Combobox(root, values=["Singular", "Plural"])
subject_combobox.grid(row=1, column=1)
subject_combobox.bind("<<ComboboxSelected>>", update_subject_entries)

# Subject Adjective Selection
subject_adj_label = tk.Label(root, text="Want Adjective?")
subject_adj_combobox = ttk.Combobox(root, values=["Yes", "No"])
subject_adj_label.grid(row=2, column=0)
subject_adj_combobox.grid(row=2, column=1)
subject_adj_combobox.bind("<<ComboboxSelected>>", update_adjective_entries)

# Subject Entry
subject_entry = ttk.Combobox(root)
subject_entry.grid(row=5, column=1)

# Verb Selection
tk.Label(root, text="Verb:").grid(row=7, column=0)
verb_combobox = ttk.Combobox(root, values=verbs)
verb_combobox.grid(row=7, column=1)

# Object Type
tk.Label(root, text="Object Type:").grid(row=8, column=0)
object_type_combobox = ttk.Combobox(root, values=["Noun", "Pronoun"])
object_type_combobox.grid(row=8, column=1)

tk.Label(root, text="Singular or Plural?").grid(row=9, column=0)
subject_combobox = ttk.Combobox(root, values=["Singular", "Plural"])
subject_combobox.grid(row=9, column=1)
subject_combobox.bind("<<ComboboxSelected>>", update_subject_entries)

# Object Adjective Selection
object_adj_label = tk.Label(root, text="Want Adjective?")
object_adj_combobox = ttk.Combobox(root, values=["Yes", "No"])
object_adj_label.grid(row=10, column=0)
object_adj_combobox.grid(row=10, column=1)
object_adj_combobox.bind("<<ComboboxSelected>>", update_object_adjective_entries)

# Object Entry
tk.Label(root, text="Object:").grid(row=11, column=0)
object_entry = ttk.Combobox(root, values=nouns)
object_entry.grid(row=12, column=1)

# Tense Selection
tk.Label(root, text="Tense:").grid(row=13, column=0)
tense_combobox = ttk.Combobox(root, values=tenses)
tense_combobox.grid(row=13, column=1)

# Mood Selection
tk.Label(root, text="Mood:").grid(row=14, column=0)
mood_combobox = ttk.Combobox(root, values=moods)
mood_combobox.grid(row=14, column=1)

# Submit Button
submit_button = tk.Button(root, text="Generate Sentence", command=on_submit)
submit_button.grid(row=15, columnspan=2)

# Run the application
root.mainloop()


# In[ ]:


import tkinter as tk
from tkinter import ttk, messagebox

verbs= {
    "give": ["give", "gives", "gave"], 
    "tell": ["tell", "tells", "told"], 
    "tell about": ["tell about", "tells about", "told about"], 
    "show": ["show", "shows", "showed"], 
    "offer": ["offer", "offers", "offered"], 
    "ask": ["ask", "asks", "asked"], 
    "ask about":["ask about","asks about","asked about"], 
    "help": ["help", "helps", "helped", "help with"], 
    "feed" : ["feed","feeds","fed"], 
    "sleep": ["sleep", "sleeps", "slept"], 
    "sleep with":["sleep with","sleeps with","slept with"],
    "jump": ["jump over", "jumps over","jumped over"],
    "cry about": [ "cry about","cries about","cried about"],
    "laugh at": [ "laugh at","laughs at","laughed at"],
    "laugh with": [ "laugh with","laughs with","laughed with"],
    "smile": ["smile to","smiles to","smiled to"],
    "run to": ["run to", "runs to", "ran to"],
    "bring": ["bring", "brings", "brought"],
    "send": ["send", "sends", "sent"],
    "send to":["send to", "sends to","sent to"],
    "teach about": ["teach about", "teaches about", "taught about"],
    "eat": ["eat", "eats", "ate", "eat with"],
    "eat with": ["eat with", "eats with", "ate with"],
    "read": ["read", "reads", "read"],
    "read about":["read about", "reads about", "read about"],
    "write": ["write to", "writes to", "wrote to"],
    "write about":["write about", "writes about", "wrote about"],
    "speak to": ["speak to","speaks to","spoke to"],
    "speak about":["speak about","speaks about","spoke about"],
    "listen to": ["listen to","listens to","listened to"],
    "talk to": ["talk to", "talks to", "talked to"],
    "walk with": ["walk with", "walks with", "walked with"],
    "run to": ["run to", "runs to", "ran to"],
    "meet with": ["meet with", "meets with", "met with"],
    "play with": ["play with", "plays with", "played with"],
    "study about": ["study about", "studies about", "studied about"],
    "clean": ["clean", "cleans", "cleaned"],
    "build": ["build", "builds", "built"],
    "fix": ["fix", "fixes", "fixed"],
    "paint": ["paint", "paints", "painted"],
    "open": ["open", "opens", "opened"],
    "close": ["close", "closes", "closed"],
    "cook": ["cook", "cooks", "cooked"],
    "buy": ["buy", "buys", "bought"],
    "enjoy": ["enjoy", "enjoys", "enjoyed"],
    "prepare": ["prepare", "prepares", "prepared"],
    "introduce": ["introduce", "introduces", "introduced"],
    "kill": ["kill", "kills", "killed"],
    "wash": ["wash", "washes", "washed"],
    "hide": ["hide", "hides", "hid"],
    "hide from" : [ "hide from", "hides from", "hid from"],
    "cut": ["cut", "cuts", "cut"]
}


nouns = [
    "cat", "dog", "book", "car", "table", "chair", "apple", "bicycle", "computer", "phone", 
    "flower", "river", "mountain", "city", "street", "school", "teacher", "student", "friend", 
    "photo", "bread", "key", "shoe", "hat", "watch", "lamp", "star", "pen", "club",
    "cloud", "fish", "fruit", "leaf", "egg", "box", "cup", "ball", "pencil", "notebook", 
    "cookie", "task", "drum", "soup", "skirt", "ticket", "sandwich", "coat", "lamp"
]

pronouns_singular = ["I", "you", "he", "she", "it"]
pronouns_plural = ["we", "you", "they"]
first = ["I","you","we","they"]
         
adjectives = [
    "red", "blue", "green", "big", "small",
    "happy", "sad", "fast", "slow", "bright",
    "dark", "light", "heavy", "thin", "thick",
    "long", "short", "tall", "young", "old",
    "new", "ancient", "clean", "dirty", "black",
    "white", "pink", "purple", "orange", "yellow",
    "warm", "cold", "sweet", "sour", "bitter",
    "spicy", "soft", "hard", "rough", "smooth",
    "quiet", "loud", "easy", "difficult", "rich",
    "poor", "brave", "cowardly", "friendly", "unfriendly"
]

pronouns_singular_adj=["me","you","him","her","it"]
pronouns_plural_adj=["us","you","them"]


# Funkcaj tworząca zdanie
def generate_sentence(subject, verb, obj):
    return f"{subject} {verb} {obj}."

# Obsluga klikniec
def update_subject_entries(event):
    subject_type = subject_type_combobox.get()
    subject_plurality = subject_plurality_combobox.get()

    if subject_type == "Noun":
        subject_entry.config(values=nouns)
    elif subject_type == "Pronoun":
        subject_entry.config(values=pronouns_plural if subject_plurality == "Plural" else pronouns_singular)

def update_adjective_entries(event):
    if subject_adj_combobox.get() == "No":
        sub_adj.grid_forget()
        sub_adj.grid_forget()


def update_object_entries(event):
    object_type = object_type_combobox.get()
    object_plurality = object_plurality_combobox.get()

    if object_type == "Noun":
        object_entry.config(values=nouns)
    elif object_type == "Pronoun":
        object_entry.config(values=pronouns_plural_adj if object_plurality == "Plural" else pronouns_singular_adj)

def update_object_adjective_entries(event):
    if object_adj_combobox.get() == "No":
        adjective_obj.grid_forget()
        adjective_obj.grid_forget()



# Zbieranie danych
def on_submit():
    subject_type = subject_type_combobox.get()
    subject = subject_entry.get()
    verb_type = verb_type_combobox.get()
    verb = verbs.get(verb_type)
    obj = object_entry.get()

    if subject and verb and obj:
        tense = tense_combobox.get()
        mood = mood_combobox.get()
        subject_adj = subject_adj_combobox.get()
        obj_adj = object_adj_combobox.get()

        # obsluga czasu, osoby i zaprzeczen
        verb_form = verb[0]  
        if tense == "Past":
            if mood == "Positive":
                verb_form = verb[2]
            else:
                verb_form = f"did not {verb[0]}"
        elif tense == "Future":
            if mood == "Positive":
                verb_form = f"will {verb[0]}"
            else:
                verb_form = f"will not {verb[0]}"
        elif subject_plurality_combobox.get() == "Plural":
            if mood == "Positive":
                verb_form = verb[0]  
            else:
                verb_form = f"do not {verb[0]}"
        else:
            if mood == "Positive":
                verb_form = verb[1]  
            else:
                verb_form = f"does not {verb[0]}"

        # stworzenie frazy rzeczonikowej dla subjectu
        if subject_adj == "Yes":
            subject_adj_value = sub_adj.get()
            subject = f"{subject_adj_value} {subject}"

        # stworzenie frazy rzeczonikowej dla objectu
        if obj_adj == "Yes":
            obj_adj_value = adjective_obj.get()
            obj = f"{obj_adj_value} {obj}"

        # Sklejenie zdania
        sentence = generate_sentence(subject, verb_form, obj)
        messagebox.showinfo("Generated Sentence", sentence)
    else:
        messagebox.showwarning("Input Error", "Please fill in all fields.")

# obsluga GUI
root = tk.Tk()
root.title("Sentence Generator")

# Czasownik
tk.Label(root, text="Verb:").grid(row=0, column=0)
verb_type_combobox = ttk.Combobox(root, values=list(verbs.keys()))
verb_type_combobox.grid(row=0, column=1)

# Podmiot - zaimek czy rzeczownik
tk.Label(root, text="Subject Type:").grid(row=2, column=0)
subject_type_combobox = ttk.Combobox(root, values=["Noun", "Pronoun"])
subject_type_combobox.grid(row=2, column=1)
subject_type_combobox.bind("<<ComboboxSelected>>", update_subject_entries)

# Liczba pojedyncza czy mnoga
tk.Label(root, text="Singular or Plural?").grid(row=4, column=0)
subject_plurality_combobox = ttk.Combobox(root, values=["Singular", "Plural"])
subject_plurality_combobox.grid(row=4, column=1)
subject_plurality_combobox.bind("<<ComboboxSelected>>", update_subject_entries)

# Czy bedzie przymiotnik doklejony czy nie
subject_adj_label = tk.Label(root, text="Want Adjective?")
subject_adj_combobox = ttk.Combobox(root, values=["Yes", "No"])
subject_adj_label.grid(row=5, column=0)
subject_adj_combobox.grid(row=5, column=1)
subject_adj_combobox.bind("<<ComboboxSelected>>", update_adjective_entries)

# wybor przymiotnika
tk.Label(root, text="Adjective:").grid(row=6, column=0)
sub_adj = ttk.Combobox(root, values=adjectives)
sub_adj.grid(row=6, column=1)

# wybor podmiotu
subject_entry = ttk.Combobox(root)
subject_entry.grid(row=7, column=1)

# Dopelnienie - zaimek czy rzeczownik
tk.Label(root, text="Object Type:").grid(row=8, column=0)
object_type_combobox = ttk.Combobox(root, values=["Noun", "Pronoun"])
object_type_combobox.grid(row=8, column=1)
object_type_combobox.bind("<<ComboboxSelected>>", update_object_entries)

# Liczba mnoga czy pojedyncza
tk.Label(root, text="Singular or Plural?").grid(row=10, column=0)
object_plurality_combobox = ttk.Combobox(root, values=["Singular", "Plural"])
object_plurality_combobox.grid(row=10, column=1)
object_plurality_combobox.bind("<<ComboboxSelected>>", update_object_entries)

# Czy będzie przymiotnik
object_adj_label = tk.Label(root, text="Want Adjective?")
object_adj_combobox = ttk.Combobox(root, values=["Yes", "No"])
object_adj_label.grid(row=12, column=0)
object_adj_combobox.grid(row=12, column=1)
object_adj_combobox.bind("<<ComboboxSelected>>", update_object_adjective_entries)

# Wybor przymiotnika
tk.Label(root, text="Adjective:").grid(row=13, column=0)
adjective_obj = ttk.Combobox(root, values=adjectives)
adjective_obj.grid(row=13, column=1)

# Doplenienie
object_entry = ttk.Combobox(root)
object_entry.grid(row=14, column=1)

# Czas
tk.Label(root, text="Tense:").grid(row=16, column=0)
tense_combobox = ttk.Combobox(root, values=["Present", "Past", "Future"])
tense_combobox.grid(row=16, column=1)

# Zaprzeczenie czy twierdzące
tk.Label(root, text="Mood:").grid(row=18, column=0)
mood_combobox = ttk.Combobox(root, values=["Positive", "Negative"])
mood_combobox.grid(row=18, column=1)

# Przycisk do tworzenia zdania
generate_button = ttk.Button(root, text="Generate Sentence", command=on_submit)
generate_button.grid(row=20, column=1)

root.mainloop()


# In[ ]:





# In[ ]:




