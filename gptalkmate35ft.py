from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
  model="ft:gpt-3.5-turbo-1106:hdi-lab::8b2P0rri",
  messages=[
    {"role": "user", "content": "GPTalkmateは、ユーザーの言語レベルに応じて返答のレベルを自動的に調整する適応型の会話型AIです。主に、内容の深さ、単語の難易度、文法の難易度、そしてそのトピックに対する理解度などが異なります。"},
    {"role": "assistant", "content": "わかりました。アウトドア活動はお好きですか？どんな活動がお好きですか？もしくは最後に行ったアウトドアでの経験について教えてください。"},
    {"role": "user", "content": "すきでないです。"}

  ]
)
print(completion.choices[0].message)