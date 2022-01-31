# sys = using Python with argument in windows CLI
# os = creating a directory in Windows
# shutil = moving files through directories
import sys, os, shutil

#list of supported format
picture_format = ['jpg', 'png', 'gif']
document_format = ['pdf']
programming_format = ['py']
installer_format = ['exe', 'msi']
model_format = ['obj', 'fbx', 'hipnc', 'hiplc', 'usd']
archive_format = ['zip', '7z']
miscellaneous_format = ['gdtf']

supported_format = [picture_format, document_format, programming_format, installer_format, model_format, archive_format, miscellaneous_format]
folder_list = ['Pictures', 'Document', 'Programming', 'Installer', 'Model', 'Archive', 'Miscellaneous']
user_choice = 0

# change working directory for the folder that we want to organize
# sys.argv[0] can be used to specify a path argument when we launch the program from shell
os.chdir('C:\\Users\AMD-X570\Downloads')
cwd = os.getcwd()

#function to move a file to its destination
def organize_function(file_name, file_extension):
    loop_counter = 0
    while loop_counter < len(supported_format):
        if file_extension in supported_format[loop_counter]:
            hierarchy_building(loop_counter)
            # create a variable for the actual path where the file is located
            file_path = cwd + '\\' + file_name + '.' + file_extension
            # create a variable for the destination path where the file will be moved
            file_destination_path = cwd + '\\' + '0' + str(loop_counter) + '.' + folder_list[loop_counter] + '\\' + file_name + '.' + file_extension
            try:
                shutil.move(file_path, file_destination_path)
                print(file_name + '.' + file_extension + ' has been moved to ' + file_destination_path)
            except OSError as error:
                raise Exception('An error has occured with ' + file_name + '.' + file_extension)
        loop_counter += 1

#function to create the folder hierarchy
def hierarchy_building(loop_counter):
        folder_name = folder_list[loop_counter]
        print("Creating " + folder_name + " folder in " + cwd)
        try:
            os.mkdir("0" + str(loop_counter) + "." + folder_name)
            print("0" + str(loop_counter) + "." + folder_name + " folder succesfully created !")
        except OSError as error:
            print(folder_name + " folder already exist")


# for loop through every files in a specific folder
# validate that the current entry is a file or a directory
def main():

    print('current working directory is ' + cwd)
    print("1. PRESS 1 to to organize files in " + cwd)
    print("2. PRESS 2 to exit this tool")

    try:
        user_choice = int(input())
        if user_choice not in [1,2]:
            print('Sorry, you number is not valid')
            main()
    except ValueError:
        print("Sorry, I didn't understand that.")
        # better try again... Return to the start of the loop
        main()

    if user_choice == 1:
        for x in os.listdir(cwd):
            if os.path.isfile(x):
                x = x.split('.')
                file_extension = x[1]
                file_name = x[0]
                organize_function(file_name, file_extension)
            elif os.path.isdir(x):
                print(x + ' is a directory')
            else:
                print(x + ' is not recognized')

    if user_choice == 2:
        exit()

if __name__ == "__main__":
    main()


