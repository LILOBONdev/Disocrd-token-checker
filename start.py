from utils import *
from checker import main
from utils.logo import logo

print(Fore.RED + logo + Fore.WHITE)
while True:
    os.system('title DISCORD TOKEN CHECKER')
    input('[+] Enter to continue BRO')
    _ = asyncio.run(main())
