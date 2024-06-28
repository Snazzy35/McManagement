# McManagement
A Simple yet Powerful Python program used to run, restart, and backup Java Minecraft Servers.
If you are on Windows, Do not attemt any of this. It will end in a mess due to missing windows commands such as wget or apt. Read the section titled "How to use this command with Windows" before going any further!
I do not currently know how to make this run on Mac! Sorry!
Can run Scalable Docker, Resiliant Daemon, or simple command style minecraft servers.
Default(Command) Style:
- Straightforward and Simple
- All variables needed are described in --help. The server is run on port 25565 or another specified port. All acccess is through the host machine.
- Example 1: python3 mcmanagement.py --folderpath /var/lib/mc --mc-version 8 --mcmemory 16000 --accept-license --mc-difficulty 3
- In Example 1, the script will install and run a Minecraft 1.8 server indefinately. This is not optimal, but it is a working example.

Daemon Style (Reccomended): DEVELOPMENT
- Most of the same rules as Command Style. Starts on system start.
- 

Docker Style (Advanced/Scalable)
- Completely different rules from either other style.
- This can create x identical servers with different ports. Each is neatly managed in its own container.
SSH:
SSH is highly recommended in Docker. It can be used for commands and file transfers such as WinSCP. Only disable SSH if you truly want the server to run headless. Never port forward SSH ports outside of a local network.
Jupyter:
Jupyter is also really nice but not required. It provides a GUI Web Interface complete with SSH Terminals, File Downloads, and file previews. Very helpful for any docker container.

How Docker Works:
- Docker is an efficient way to containerize certain tasks into seperate secure operating systems. Docker is useful here to make ports easy to route and to provide security to the host machine. Docker can do much more than this, but I am using it for these reasons. One complication of Docker is that all container files (Like your Minecraft Server) are keyhashed on the Host Machine. This is great for security but can become an issue when moving files from containers to elsewhere.

Examples:
Breakdown Example: Sudo python3 mcmanagement.py --docker --docker-jupyter --docker-min-port X --num-docker-containers Y --docker-group-name Z --mc-version 8 --mcmemory 8000 --mc-difficulty 3 --accept-license
- In this example I have left three variables open: The Docker Ones. X must be replaced with the minimum port you will allow servers to run on. Make this in the many of thousands but not above 60000. 65565 is the maximum port, and we do not want to go near that. I would go with 30000. Once the command is run it will tell you which of these ports should be opened up on the router and which should be kept local. DO NOT OPEN UP THE ENTIRE RANGE!!! SSH is a security vulnerability when forwarded. These ports can be rerouted again at the website endpoint or kept like they are. To reroute them go to where you got your domain from and forward 111.111.111.111:30004 > Minecraft.Server.Web:25565. You will obviously have to replace the given examples with your own IP and Site. Y Decides how many of these servers to make. This is up to you and mainly your desired amount of servers. There is a limit though. If you run out of Storage or Memory you will be unable to make any more containers. Finally there is Z. Docker-Group-Name decides what to call the group of docker containers. This is most useful if you create multiple groups of different servers, but is still required for naming reasons. If I enter MC for the variable, The First docker container created will be called "MC0" and containers created after will have sequentially increasing numbers.
Working Example: sudo python3 mcmanagement,py --docker --docker-jupyter --docker-min-port 300000 --num-docker-containers 10 --docker-group-name MC-1.8 --mc-version 8 --mcmemory 8000 --mc-difficulty 3 --accept license
- This example will create 10 Minecraft 1.8 servers enabled with SSH and Jupyter

How to use this command with Windows:
In order to be used on Windows, WSL must first be installed. Just run "Command" in Powershell and create a username and password. Follow all instructions. Once WSL is done, you can run commands as if you were in Ubuntu. This is not recommended but it will work in inflexible scenarios.

Datacenter Hosting Use:
AWS, Google Cloud, Azure, etc. can be used to reliably and scalably run servers. However it is very expensive. It would be a very reliable server but very unneccicary unless you need this up 24/7 with nothing unexpected. I have never used any of these providers before so I do not know how to run commands, but I am sure you can find a command line somewhere.

Community Cloud:
COMMUNITY CLOUD WARNING!! - These machines are not neccicarily reliable and are not guarenteed to stay online. Make constant backups to ensure you will not lose anything if it does go down. Also, make sure to pay a fair price for a given machine. Too low of a price could prompt the host to start over on a new machine thus deleting your instance. Also, if you can prepay an instance, it tells the host that you want to keep the machine for a while. It will help with disincentivising hosts to go offline but it does take an upfromt commitment of cash. Datacenter Machines are rarer and more expensive but would also help with these same issues.

You could also run this on a community cloud service, such as Vast.ai. Vast provies very fair pricing on CPU and GPU machines that are generally equipped with lots of storage and memory. Pricing is by the gpu/machine plus storage plus internet bandwidth. Many machines have powerful CPU's with up to about 64 vCPU's per GPU. Good machines have variable memory amounts but at least 2 Gigabtes of memory per thread. Obviously a server such as this costs money, but if Minecraft only uses the CPU, then the GPU can be used to cover the hourly rental cost. Many servers could be run on these types of could machines, but since Vast runs on unprivelaged Docker Containers, the Docker Option cannot be used, so each server/daemon must be run manually. This is the most cost effective option to run lots of servers but also the least reliable. To recoup costs of the server, you could either cryptocurrency mine or find a use for it for yourself or someone else. Cryptocurrency mining will slightly increase the odds of a crash, so find a good machine before committing to it. I personally would run an AI text generation interface using a Meta Llama2 model and create the instance as jupyter and running a cryptocurrency mining software from there. Then you can use the GPU time as either a chatbot or as a revenue-generating source. The crypto market moves quickly so make sure to pick a reliable(ish) crypto and mine that. You are looking for long-term mining revenue. If you want to be more attentive to this instance, you could do your research and mine a coin that you think will go up in the future. This is difficult to do though. It is easier to mine a big-ish coin such as Conflux (CFX), RavenCoin (RVN), or Ethereum Classic (ETC). Many of these are only profitable on very certain GPU's, so find an instance with a GPU that works with the coin you are mining, a good CPU, and a good reliability score. Do your research on which machine is best! It could save you a lot of trouble if you find a good one. 