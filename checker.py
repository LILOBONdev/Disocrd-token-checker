from utils import *

async def fetch(session,auth):
    async with session.get('https://discord.com/api/v10/users/@me',headers={'user-agent': FakeUserAgent().chrome,'authorization': auth}) as res:
        return res.status

async def check_token(auth, session):
    response_status = await fetch(session,auth)
    if response_status == 200 or response_status == 201:
        print(Fore.GREEN + f'{auth} is good!' + Fore.WHITE)
        with open('results/valid.txt','a',encoding='utf-8') as valid: valid.write(auth + '\n')
    else:
        print(Fore.RED + f'{auth} is bad!' + Fore.WHITE)
        with open('results/bad.txt','a',encoding='utf-8') as valid: valid.write(auth + '\n')


async def main():
    os.makedirs('results', exist_ok=True)
    for _ in ['bad.txt','valid.txt']: open(f'results/{_}').close()

    try:
        with open('input/tokens.txt', 'r', encoding='utf-8') as file:
            tokens = file.read().strip().split()
        if tokens == []: print(Fore.RED + 'Токены не найдены input/tokens.txt' + Fore.WHITE)
    except FileNotFoundError:
        print(f"{Fore.RED}Ошибка: файл input/codes.txt не найден{Fore.RESET}")
        return
    
    chunk_size = 100
    async with aiohttp.ClientSession() as session:
        for i in range(0, len(tokens), chunk_size):
            batch = tokens[i:i + chunk_size]
            os.system(f'title checked: {i} good tokens: {open('results/valid.txt','r',encoding='utf-8').read().split('\n').__len__()-1} bad tokens: {open('results/bad.txt','r',encoding='utf-8').read().split('\n').__len__()-1}')
            tasks = [check_token(code, session) for code in batch]
            await asyncio.gather(*tasks)
