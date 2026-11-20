import os, re, json, urllib.request, urllib.error

GROQ_KEY = os.environ["GROQ_API_KEY"]
MODEL = "llama-3.3-70b-versatile"

BROWSER_UA = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/120.0 Safari/537.36"
)


def post(url, payload, headers):
    headers = {
        "User-Agent": BROWSER_UA,
        "Accept": "application/json",
        **headers,
    }
    req = urllib.request.Request(
        url, data=json.dumps(payload).encode(), headers=headers
    )
    try:
        return json.load(urllib.request.urlopen(req, timeout=60))
    except urllib.error.HTTPError as e:
        print("HTTP ERROR", e.code, "from", url)
        print(e.read().decode()[:500])
        raise SystemExit(1)


# 1. Daily problem anao
q = post(
    "https://leetcode.com/graphql",
    {
        "query": """query { activeDailyCodingChallengeQuestion {
            question { questionFrontendId title titleSlug difficulty content } } }"""
    },
    {"Content-Type": "application/json", "Referer": "https://leetcode.com"},
)["data"]["activeDailyCodingChallengeQuestion"]["question"]

folder = f'{int(q["questionFrontendId"]):04d}-{q["titleSlug"]}'
if os.path.exists(folder):
    print("Already exists, skipping")
    raise SystemExit

text = re.sub(r"<[^>]+>", "", q["content"])
for a, b in [
    ("&nbsp;", " "),
    ("&lt;", "<"),
    ("&gt;", ">"),
    ("&amp;", "&"),
    ("&quot;", '"'),
]:
    text = text.replace(a, b)

# 2. Groq theke solution anao
prompt = f"""Solve this LeetCode problem in Python.
Title: {q['title']}
{text}

Reply ONLY with JSON with keys:
"approach" (short paragraph), "steps" (list of strings), "time" (string), "space" (string),
"code" (full Python solution using class Solution, as in LeetCode)."""

res = post(
    "https://api.groq.com/openai/v1/chat/completions",
    {
        "model": MODEL,
        "temperature": 0.2,
        "response_format": {"type": "json_object"},
        "messages": [{"role": "user", "content": prompt}],
    },
    {"Content-Type": "application/json", "Authorization": f"Bearer {GROQ_KEY}"},
)
d = json.loads(res["choices"][0]["message"]["content"])

# 3. Files banao
os.makedirs(folder, exist_ok=True)
steps = "\n".join(f"{i+1}. {s}" for i, s in enumerate(d["steps"]))
readme = f"""# {q['questionFrontendId']}. {q['title']}

**Difficulty:** {q['difficulty']}
**Link:** https://leetcode.com/problems/{q['titleSlug']}/

## Question
{text.strip()}

## Approach
{d['approach']}

## Steps
{steps}

## Complexity
- Time: {d['time']}
- Space: {d['space']}

> Draft generated with Groq ({MODEL}). Review before relying on it.
"""
open(f"{folder}/README.md", "w", encoding="utf-8").write(readme)
open(f"{folder}/solution.py", "w", encoding="utf-8").write(d["code"] + "\n")
print("Created", folder)
