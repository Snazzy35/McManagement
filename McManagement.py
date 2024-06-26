import datetime
import logging
import sys
import argparse
import os
import subprocess
from subprocess import STDOUT, check_call
parser = argparse.ArgumentParser()
parser.add_argument("--docs", help="Provide a link to useful documentation and exit.",
                    action="store_true")
parser.add_argument("-v", "--verbose", help="increase output verbosity",
                    action="store_true")
parser.add_argument("-s", "--silent", help="Do not write any logs and execute all tasks in the background. Will still display errors in the terminal",
                    action="store_true")
parser.add_argument("--folderpath", type=str, help="The path to where existing MC files can be found or where new files should be put. Ex. /var/lib/mc")
parser.add_argument("--mc-version", type=int, help="The Version of Minecraft to Run or Install. Only latest releases. Must be in subversion form eg. 16 instead of 1.16.")
parser.add_argument("--mcmemory", type=int,
                    help="The Amount of memory in Megabytes (MB) that is allocated to Java. Default is 16000.")
parser.add_argument("--mc-difficulty", type=int,
                    help="Difficulty level of the Minecraft Server. 0=Peaceful, 1=Easy, 2=Normal, 3=Hard, 4=Hardcore. Default is 2 'Normal'")
parser.add_argument("--reset-server-config", action="store_true",
                    help="Deletes the Server.properties.bak file and uses other arguments to build it again. This is non-destructive to the current Minecraft world b")
parser.add_argument("--restart-interval", type=int,
                    help="Time between Server Restarts in Seconds. Will give a warning in chat 60 seconds before the restart is done.")
parser.add_argument("--accept-license", help="Accepts the Paper License. BY USING THIS YOU ARE ACCEPTING THE LICENSE OF PAPERMC.",
                    action="store_true")
parser.add_argument("--install", help="Installs the required files to the specified directory.",
                    action="store_true")
parser.add_argument("--reset-server", help="Deletes the specified directory and reinstalls the files. THIS IS DESTRUCTIVE!!!",
                    action="store_true")
parser.add_argument("--docker", help="Installs Docker and runs the server inside that container.",
                    action="store_true")
parser.add_argument("--no-docker-ssh", help="Disables SSH access to docker containers, thus blocking most access to the container. Not recommended but makes the container slightly more secure.",
                    action="store_true")
parser.add_argument("--docker-jupyter", help="Runs Jupyter inside each docker container",
                    action="store_true")
parser.add_argument("--docker-min-port", help="Bottom range of the ports that this will run on. Every port will be above this number. Don't make this below 1000 and DO NOT MAKE IT 65565.",
                    type=int)
parser.add_argument("--num-docker-containers", help="Number of Docker containers to run. Don't go crazy with this number!",
                    type=int)
parser.add_argument("--docker-group-name", help="Name to label docker containers with. In docker, the name will be x+y x = this variable and y = the number of the specific container.",
                    type=str)
parser.add_argument("--daemon", help="Runs the server as a Daemon. Runs on system start and is much more resistant to issues. Reccomended for single server use. NOT COMPATIBLE WITH --DOCKER!!!",
                    action="store_true")
parser.add_argument("--mc-port", type=int,
                    help="The Port That Minecraft will run on, and the port that must be connected to for Minecraft. Only compatible with Docker. Useful for setting up multiple Minecraft servers on the same Machine IP.")
parser.add_argument("--windows", help="Displays instructions on how to install WSL.",
                    action="store_true")
parser.add_argument("--docker-auto-install", help="NOT FOR MANUAL USE!!! REQUIRES MANY OTHER SPECIFIC VARIABLES THAT ARE NOT CHECKED FOR! ONLY RUN AUTOMATICALLY!",
                    action="store_true")
args = parser.parse_args()
if args.docs:
    print('find the docs here: https://github.com/Snazzy35/McManagement/blob/main/README.md')
    subprocess.run(["wget", "-P", './readme.md', "https://raw.githubusercontent.com/Snazzy35/McManagement/main/README.md"])
    subprocess.run(['cat', 'readme.md'])
def install_paper(MCV, MCP):
    if MCV == 8:
        subprocess.run(["wget", "-O", MCP, "https://api.papermc.io/v2/projects/paper/versions/1.8.8/builds/445/downloads/paper-1.8.8-445.jar"])
    elif MCV == 9:   
        subprocess.run(["wget", "-O", MCP, "https://api.papermc.io/v2/projects/paper/versions/1.9.4/builds/775/downloads/paper-1.9.4-775.jar"])
    elif MCV == 10:
        subprocess.run(["wget", "-O", MCP, "https://api.papermc.io/v2/projects/paper/versions/1.10.2/builds/918/downloads/paper-1.10.2-918.jar"])
    elif MCV == 11:
        subprocess.run(["wget", "-O", MCP, "https://api.papermc.io/v2/projects/paper/versions/1.11.2/builds/1106/downloads/paper-1.11.2-1106.jar"])
    elif MCV == 12:
        subprocess.run(["wget", "-O", MCP, "https://api.papermc.io/v2/projects/paper/versions/1.12.2/builds/1620/downloads/paper-1.12.2-1620.jar"])
    elif MCV == 13:
        subprocess.run(["wget", "-O", MCP, "https://api.papermc.io/v2/projects/paper/versions/1.13.2/builds/657/downloads/paper-1.13.2-657.jar"])
    elif MCV == 14:
        subprocess.run(["wget", "-O", MCP, "https://api.papermc.io/v2/projects/paper/versions/1.14.4/builds/245/downloads/paper-1.14.4-245.jar"])
    elif MCV == 15:
        subprocess.run(["wget", "-O", MCP, "https://api.papermc.io/v2/projects/paper/versions/1.15.2/builds/393/downloads/paper-1.15.2-393.jar"])
    elif MCV == 16:
        subprocess.run(["wget", "-O", MCP, "https://api.papermc.io/v2/projects/paper/versions/1.16.5/builds/794/downloads/paper-1.16.5-794.jar"])
    elif MCV == 17:
        subprocess.run(["wget", "-O", MCP, "https://api.papermc.io/v2/projects/paper/versions/1.17.1/builds/411/downloads/paper-1.17.1-411.jar"])
    elif MCV == 18:
        subprocess.run(["wget", "-O", MCP, "https://api.papermc.io/v2/projects/paper/versions/1.18.2/builds/388/downloads/paper-1.18.2-388.jar"])
    elif MCV == 19:
        subprocess.run(["wget", "-O", MCP, "https://api.papermc.io/v2/projects/paper/versions/1.19.4/builds/550/downloads/paper-1.19.4-550.jar"])
    elif MCV == 20:
        subprocess.run(["wget", "-O", MCP, "https://api.papermc.io/v2/projects/paper/versions/1.20.6/builds/134/downloads/paper-1.20.6-134.jar"])
    else:
        print('Unknown MC Version. Check your MC number.')
if args.docker and args.daemon:
    print("Error. Please choose either Docker or Daemon. Not both.")
    exit()
elif args.daemon:
    #Run the Daemon...
    print("You have found an unfinished piece of code. Sorry!")
elif args.docker:
    print("Installing Docker...")
    subprocess.run(["apt", "install", "-y", "docker.io"])
    #Portconfig!
    dockerminport = args.docker_min_port
    dockercontainers = args.num_docker_containers
    if args.no_docker_ssh and args.jupyter:
        minsshport = 0
        minmcport = dockerminport
        minjupyterport = dockerminport + dockercontainers
        totalports = 2*dockercontainers
        print("Port(s)"+dockerminport+"to"+dockerminport+dockercontainers-1+"are your MC Port(s). These Must be forwarded. Port(s)"+minjupyterport+"to"+minjupyterport+dockercontainers-1+"are your Jupyter port(s). Remember you have no SSH so Jupyter is the best connection to the container! Remember those port(s).")
        print("You are using"+totalports+"Ports!")
        print("Success!")
    elif args.no_docker_ssh:
        minsshport = 0
        minmcport = dockerminport
        totalports = dockercontainers
        print("Port(s)"+dockerminport+"to"+dockerminport+dockercontainers-1+"are your MC Port(s). These Must be forwarded.")
        print("You are using"+totalports+"Ports!")
        print("Success!")
    elif args.docker_jupyer:
        minsshport = dockerminport
        minmcport = dockerminport + dockercontainers
        minjupyterport = minmcport + dockercontainers
        totalports = 3*dockercontainers
        print("Ports"+minsshport+"to"+minsshport+dockercontainers-1+"are your SSH Ports. DO NOT FORWARD THESE!!! NEVER! Remember them for ssh access to specific containers. Port(s)"+minmcport+"to"+minmcport+dockercontainers-1+"are your MC Port(s). These Must be forwarded. Port(s)"+minjupyterport+"to"+minjupyterport+dockercontainers+"are your Jupyter port(s). Remember those port(s).")
        print("You are using"+totalports+"Ports!")
        print("Success!")
    else:
        print("default config.")
        minsshport = dockerminport
        minmcport = minsshport + dockercontainers
        totalports = 2*dockercontainers
        print("Ports"+minsshport+"to"+minsshport+dockercontainers-1+"are your SSH Ports. DO NOT FORWARD THESE!!! NEVER! Remember them for ssh access to specific containers. Port(s)"+minmcport+"to"+minmcport+dockercontainers-1+"are your MC Port(s). These Must be forwarded.")
        print("You are using"+dockercontainers+"Ports!")
        print("Success!")
print("Building Docker Create Command...")
print("ToDo Later Sorry")
    
    #subprocess.run(["sudo", "docker", "run", "-it", "ubuntu:latest", "-p", "22:"])
    #print("Done!")
    
McMemory = args.mcmemory
if McMemory is None:
    McMemory = 16000
elif McMemory > 0 and McMemory <100: 
    print('Memory amount is in Gigabytes. Correcting...')
    McMemory = McMemory * 1000
else:
    pass
FolderPath = args.folderpath
MCPath = str(FolderPath) + "/java"
print(args.mc_version)
McVersion = args.mc_version
if McVersion < 12 and McVersion > 7:
    javaversion = 8
elif McVersion < 16 and McVersion > 11:
    javaversion = 11
elif McVersion == 16:
    javaversion = 16
elif McVersion < 21 and McVersion > 16 or McVersion == 21:
    javaversion = 21
else:
    print("Check your Minecraft Version and Try Again!")
    exit()
print(javaversion)
#if args.verbose and args.silent:
    #print('FATAL: Both Verbose and Silent modes are on. Ending program. Please run with at most one of these variables.')
    #quit()
if args.silent:
    pass
else:
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')
    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setLevel(logging.DEBUG)
    stdout_handler.setFormatter(formatter)
    file_handler = logging.FileHandler("log.log")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    logger.addHandler(stdout_handler)
starttime = datetime.datetime.now()
if True or False:
    McExists = os.path.isdir(args.folderpath)
    if McExists == False or args.install:
        #print("Creating a directery for MC")
        os.makedirs(args.folderpath)
        os.chdir(args.folderpath)
        install_paper(MCV=McVersion, MCP=MCPath)
        print("Adding Java Repositories...")
        check_call(['sudo', 'add-apt-repository', 'ppa:linuxuprising/java', '-y'],
        stdout=open(os.devnull,'wb'), stderr=STDOUT)
        print("Running Apt Update...")
        check_call(['sudo', 'apt', 'update', '-y'],
        stdout=open(os.devnull,'wb'), stderr=STDOUT)
        print("Installing Java...")
        if javaversion == 8:
            check_call(['apt', 'install', '-y', 'openjdk-8-jdk'],
            stdout=open(os.devnull,'wb'), stderr=STDOUT)
        elif javaversion == 11:
            check_call(['apt', 'install', '-y', 'openjdk-11-jdk'],
            stdout=open(os.devnull,'wb'), stderr=STDOUT)
        elif javaversion == 16:
            print("Sorry, but the Packages for Java 16 have been removed. I will find a way around this soon. For a quick fix find the Minecraft 1.16.4 package at Papermc, put the download link into the existing wget command that is under Minecraft 1.16 earlier in the script. Then add a new line and copy the java install script for Java 11 to the line after where this text is from.")
        elif javaversion == 21:
            check_call(['apt', 'install', '-y', 'openjdk-17-jdk'],
            stdout=open(os.devnull,'wb'), stderr=STDOUT)
    elif McExists == True:
        pass
    else:
        print("A problem occured.")
    #check_call(['java', '-Xms'+McMemory+'M', '-Xms'+McMemory+'M', MCPath],
    #stdout=open(os.devnull,'wb'), stderr=STDOUT)
    if args.accept_license:
        subprocess.run(['rm', FolderPath+"/eula.txt"])
        f = open("eula.txt", "a")
        f.write("eula=true")
        f.close()
        pass
    else:
        manuallicenseaccept = input("DO YOU ACCEPT THE PAPERMC LICENSE? IT CAN BE FOUND AT https://www.minecraft.net/en-us/eula (Paper also requires it to be said that by agreeing to this EULA, you agree that tacos are tasty.)     [Y/CTRL+C]")
        print(manuallicenseaccept)
        if manuallicenseaccept == "Y" or "y" or "Yes" or "yes" or "YES":
            print('License Accepted!')
            subprocess.run(['rm', FolderPath+"/eula"])
            f = open("eula.txt", "a")
            f.write("eula=true")
            f.close()
            pass
        elif manuallicenseaccept == "N" or "No":
            print('License must be accepted for Paper to run.')
        else:
            print('unkonwn input. Try again. with a different input.')
            quit()
    mcmemorystr = str(McMemory)
    subprocess.run(["java", "-Xms"+mcmemorystr+'M', "-Xmx"+mcmemorystr+'M', "-jar", MCPath])


else:
    logger.info(starttime)
if args.silent:
    pass
else:
    logger.info('Checking for Existing Server files...')







#Unused
#if McVersion == 8:
#            subprocess.run(["wget", "-P", MCPath, "https://api.papermc.io/v2/projects/paper/versions/1.8.8/builds/445/downloads/paper-1.8.8-445.jar"])
#        elif McVersion == 9:   
#            subprocess.run(["wget", "-P", MCPath, "https://api.papermc.io/v2/projects/paper/versions/1.9.4/builds/775/downloads/paper-1.9.4-775.jar"])
#        elif McVersion == 10:
 #           subprocess.run(["wget", "-P", MCPath, "https://api.papermc.io/v2/projects/paper/versions/1.10.2/builds/918/downloads/paper-1.10.2-918.jar"])
  #      elif McVersion == 11:
#            subprocess.run(["wget", "-P", MCPath, "https://api.papermc.io/v2/projects/paper/versions/1.11.2/builds/1106/downloads/paper-1.11.2-1106.jar"])
      #  elif McVersion == 12:
   #         subprocess.run(["wget", "-P", MCPath, "https://api.papermc.io/v2/projects/paper/versions/1.12.2/builds/1620/downloads/paper-1.12.2-1620.jar"])
      #  elif McVersion == 13:
    #        subprocess.run(["wget", "-P", MCPath, "https://api.papermc.io/v2/projects/paper/versions/1.13.2/builds/657/downloads/paper-1.13.2-657.jar"])
      #  elif McVersion == 14:
   #         subprocess.run(["wget", "-P", MCPath, "https://api.papermc.io/v2/projects/paper/versions/1.14.4/builds/245/downloads/paper-1.14.4-245.jar"])
     #   elif McVersion == 15:
     #       subprocess.run(["wget", "-P", MCPath, "https://api.papermc.io/v2/projects/paper/versions/1.15.2/builds/393/downloads/paper-1.15.2-393.jar"])
      #  elif McVersion == 16:
     #       subprocess.run(["wget", "-P", MCPath, "https://api.papermc.io/v2/projects/paper/versions/1.16.5/builds/794/downloads/paper-1.16.5-794.jar"])
       # elif McVersion == 17:
       #     subprocess.run(["wget", "-P", MCPath, "https://api.papermc.io/v2/projects/paper/versions/1.17.1/builds/411/downloads/paper-1.17.1-411.jar"])
        #elif McVersion == 18:
       ##     subprocess.run(["wget", "-P", MCPath, "https://api.papermc.io/v2/projects/paper/versions/1.18.2/builds/388/downloads/paper-1.18.2-388.jar"])
       # elif McVersion == 19:
        #    subprocess.run(["wget", "-P", MCPath, "https://api.papermc.io/v2/projects/paper/versions/1.19.4/builds/550/downloads/paper-1.19.4-550.jar"])
      #  elif McVersion == 20:
     #       subprocess.run(["wget", "-P", MCPath, "https://api.papermc.io/v2/projects/paper/versions/1.20.6/builds/134/downloads/paper-1.20.6-134.jar"])
 #