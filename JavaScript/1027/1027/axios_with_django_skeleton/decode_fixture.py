import json
json_list = [
    'articles/fixtures/articles.json',
    'articles/fixtures/comments.json',
    'accounts/fixtures/users.json',
]
    
for path in json_list:
    with open(path, 'r') as f:
        decoded_data = json.load(f)
        with open(path, 'w', encoding='utf-8', newline='') as rf:
            json.dump(decoded_data, rf, indent=2, ensure_ascii=False)