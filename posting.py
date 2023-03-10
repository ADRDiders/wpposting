import requests
import base64
import openai

openai.api_key = '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'


def wph(text):
    code = f'<!-- wp:heading --><h2>{text}</h2><!-- /wp:heading -->'
    return code
def wpp(text):
    code = f'<!-- wp:paragraph --><p>{text}</p><!-- /wp:paragraph -->'
    return code

def opa_ans(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
)

    output = (response.get('choices')[0].get('text'))
    return output
keyword = input('Enter your keyword: ')
prompt = f'Write three questions about {keyword}'
content = wpp(opa_ans(f'Write short intro about {keyword}').strip().strip('\n'))
questions = opa_ans(prompt)
questions_list = questions.strip().split('\n')

end_line = 'write a paragraph about it'
qna = {}
for q in questions_list:
    command = f'{q} {end_line}'
    answer = opa_ans(command).strip().strip('\n')
    qna[q] = answer

user = 'username'
password = 'v7TD fHzN zC85 VNPW cb8l 5lGG'
credential = f'{user}:{password}'
token = base64.b64encode(credential.encode())
headers = {'Authorization': f'Basic {token.decode("utf-8")}'}


for key, value in qna.items():
    qn = wph(key)
    ans = wpp(value)
    qnas = qn + ans
    content = content + qnas

title = f'Common questions about {keyword}'

data = {
    'title': title,
    'content': content,
    'slug': keyword.replace(' ','-')
}

api_url = 'https://example.com/wp-json/wp/v2/posts'
r = requests.post(api_url, data=data, headers=headers, verify=False)











































