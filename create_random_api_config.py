from random import randint
import config

def api_list_enable():
    return eval_api("enable")

def create_api_file():
    if api_list_enable():
        api_keywords_list = get_api_list_keyword()
        print(api_keywords_list)
        print(len(api_keywords_list))
        for api_keyword in api_keywords_list:
            write_data = file_write(api_keyword)
            print(write_data)
     
def create_default_file():
    f = open("config/apilist.py","")
    f2 = open("config/api.py","w")
    f2.write(f.read())
    f.close()
    f2.close()

def eval_api(api_keyword):
    import_str = "config.{}".format(api_keyword)
    eval_api_value = eval(import_str)
    return eval_api_value

def file_write(api_keyword):
    raw_data = get_key_info(api_keyword).split(" ")
    eval_api_value = eval_api(api_keyword)
    random_index = randint(0,len(eval_api_value)-1)
    write_data = ""
    if len(raw_data) == 2:
        key_data = list(eval_api_value[random_index].keys())[0]
        value_data = eval_api_value[random_index].get(key_data)
        write_data = raw_data[0] + " = '" + key_data + "'\n"
        write_data = write_data + raw_data[1] + " = '" + value_data + "'\n\n\n"
    if len(raw_data) == 1:
        value_data = eval_api_value[random_index]
        write_data = raw_data[0] + " = '" + value_data + "'\n"
    return write_data

def get_api_list_keyword():
    data = list(dir(config))
    print(data)
    api_list = []
    for item in data:
        if "list" in item:
            api_list.append(item)
    return api_list


def get_key_info(api_keyword):
    if api_keyword == "":
        return ""
    if api_keyword == "censys_api_list":
        return "censys_api_id censys_api_secret"
    if api_keyword == "binaryedge_api_list":
        return "binaryedge_api"
    if api_keyword == "chinaz_api_list":
        return "chinaz_api"
    if api_keyword == "bing_api_list":
        return "bing_api_id bing_api_key"
    if api_keyword == "securitytrails_api_list":
        return "securitytrails_api"
    if api_keyword == "fofa_api_list":
        return "fofa_api_email fofa_api_key"
    if api_keyword == "google_api_list":
        return "google_api_id google_api_key"
    if api_keyword == "riskiq_api_list":
        return "riskiq_api_username riskiq_api_key"
    if api_keyword == "shodan_api_list":
        return "shodan_api_key"
    if api_keyword == "threatbook_api_list":
        return "threatbook_api_key"
    if api_keyword == "virustotal_api_list":
        return "virustotal_api_key"
    if api_keyword == "zoomeye_api_list":
        return "zoomeye_api_usermail zoomeye_api_password"
    if api_keyword == "spyse_api_list":
        return "spyse_api_token"
    if api_keyword == "circl_api_list":
        return "circl_api_username circl_api_password"
    if api_keyword == "dnsdb_api_list":
        return "dnsdb_api_key"
    if api_keyword == "ipv4info_api_list":
        return "ipv4info_api_key"
    if api_keyword == "passivedns_api_list":
        return "passivedns_api_addr passivedns_api_token"
    if api_keyword == "github_api_list":
        return "github_api_user github_api_token"
    if api_keyword == "cloudflare_api_list":
        return "cloudflare_api_token"
