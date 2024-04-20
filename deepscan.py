import requests

def substring_r(text, substring):
    return text.replace(substring, '')

def flws(text, substring):
    lines = text.split('\n')  # Split the text into lines
    matching_lines = [line for line in lines if substring in line]
    return matching_lines

def ripscan(site):
    try:
        response = requests.get(site)
        response.raise_for_status()
        if 'discord.me' in site:
            modifications = []
            invites = flws(response.text, 'joinServer(')
            for invite in invites:
                mod1 = substring_r(invite, '<div onclick="return')
                mod2 = substring_r(mod1, '">Join Now</div>')
                modifications.append(mod2)
            return modifications
    except requests.RequestException as e:
        print(f"Error fetching {site}: {e}")
        return []


discord_invites_log = open('scan_log.txt', "w")

g = 2
while g < 1250:
    for server in ripscan(f'https://discord.me/servers?page={str(g)}'):
        discord_invites_log.write(server + '\n')
        print(server)
    g += 1

discord_invites_log.close()
