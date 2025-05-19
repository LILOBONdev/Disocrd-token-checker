from utils import *
from checker import main
from utils.logo import logo

print(Fore.RED + logo + Fore.WHITE)
while True:
    input('[+] Enter to continue BRO')
    _ = asyncio.run(main())