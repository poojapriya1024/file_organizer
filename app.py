from flask import Flask, render_template, request
import os
import shutil
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        folder_path = request.form.get("folder-path")

        organize_files(folder_path)
        print(f"the folder path received is : {folder_path}")

    return render_template("index.html")

def organize_files(folder_path):

    list_of_folders = {
        "Pictures" : [".jpeg",".jpg",".png",".gif"],
        "Videos":[".wmv", ".mov",".mp4",".mpeg",".mkv"],
        "Zips":[".iso",".tar",".gz",".rz",".7z",".dmg",".rar",".zip"],
        "Music": [".mp3",".msv",".wav",".wma"],
        "PDFs":[".pdf"],
        "CPP_C":[".cpp",".c"],
        "Python":[".py"],
        "Java":[".java"],
        "JS_TS":[".js", ".ts"],
        "HTML":[".html5",".html",".htm",".xhtml"],
        "CSS":[".css"],
        "Documents and PPTs":[".doc",".docm",".docx",".pptx",".ppt"],
        "Spreadsheets":[".xlsx",".xls",".ods",".csv",".tsv"],
        "Executables":[".exe",".msi",".bat"],
        "Text Documents":[".txt"]
    }

    #iterate through each file in the folder
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)

        #check if it is a file
        if os.path.isfile(file_path):
            #move this file to its corresponding folder if it exists
            #else, a new folder is created

            for folder, extensions in list_of_folders.items():
                if any(file.lower().endswith(extension) for extension in extensions):
                    #creating a new path based on its appropriate directory
                    folder_path_new = os.path.join(folder_path, folder)

                    #if such folder doesn't exist, create a new one
                    os.makedirs(folder_path_new, exist_ok=True)
                    
                    #finally, move the file to the new path
                    shutil.move(file_path, os.path.join(folder_path_new, file))

    print("All organized!")


if __name__ == "__main__":
    app.run(debug=1)