import requests

drug_list_url = 'http://imd.jd.local/prod/mark/api/api/drugins/idsAndUuids'
token = 'e747e7e3-addf-4c7c-9ef5-ab7c30e1b2d8'
header_token = {
    'X-Token': token
}

res_get_ids = requests.get(drug_list_url, headers=header_token)
print(res_get_ids.text)