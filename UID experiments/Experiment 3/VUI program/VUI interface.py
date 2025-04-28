import speech_recognition as sr
import pyttsx3
import json
import os

TASK_FILE = "tasks.json"

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio)
            print(f"🔊 You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that.")
        except sr.RequestError:
            speak("Network error.")
    return ""

def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(TASK_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def add_task(tasks):
    speak("What is the title of the task?")
    title = listen()
    if not title:
        return
    speak("What is the description?")
    description = listen()
    tasks.append({
        "title": title,
        "description": description,
        "completed": False
    })
    speak("Task added.")

def view_tasks(tasks):
    if not tasks:
        speak("No tasks available.")
        return
    for i, task in enumerate(tasks, start=1):
        status = "done" if task["completed"] else "not done"
        speak(f"Task {i}: {task['title']}, {task['description']}. Status: {status}")

def complete_task(tasks):
    view_tasks(tasks)
    speak("Which task number to mark as complete?")
    try:
        index = int(listen()) - 1
        if 0 <= index < len(tasks):
            tasks[index]["completed"] = True
            speak("Task marked as complete.")
        else:
            speak("Invalid number.")
    except:
        speak("Could not understand the number.")

def delete_task(tasks):
    view_tasks(tasks)
    speak("Which task number to delete?")
    try:
        index = int(listen()) - 1
        if 0 <= index < len(tasks):
            tasks.pop(index)
            speak("Task deleted.")
        else:
            speak("Invalid number.")
    except:
        speak("Could not understand the number.")

def main():
    tasks = load_tasks()
    speak("Welcome to the voice task manager.")
    while True:
        speak("Say add, view, complete, delete or exit.")
        command = listen()

        if "add" in command:
            add_task(tasks)
        elif "view" in command:
            view_tasks(tasks)
        elif "complete" in command:
            complete_task(tasks)
        elif "delete" in command:
            delete_task(tasks)
        elif "exit" in command:
            save_tasks(tasks)
            speak("Goodbye!")
            break
        else:
            speak("Invalid command.")

if __name__ == "__main__":
    main()
