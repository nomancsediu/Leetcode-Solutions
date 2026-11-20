import os, re, json, html, time, sys, urllib.request, urllib.error

GROQ_KEY = os.environ["GROQ_API_KEY"]
MODEL = "openai/gpt-oss-120b"
PER_DAY = 3

BROWSER_UA = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/120.0 Safari/537.36"
)

# ---------- Roadmap: 300 top interview problems, topic wise (Easy to Hard) ----------
ROADMAP = [
    ("Array and Hashing", [
        "two-sum", "contains-duplicate", "valid-anagram", "majority-element",
        "single-number", "missing-number", "move-zeroes", "plus-one",
        "best-time-to-buy-and-sell-stock", "pascals-triangle",
        "find-all-numbers-disappeared-in-an-array", "isomorphic-strings",
        "word-pattern", "maximum-subarray", "group-anagrams",
        "top-k-frequent-elements", "product-of-array-except-self",
        "valid-sudoku", "longest-consecutive-sequence", "subarray-sum-equals-k",
        "find-the-duplicate-number", "set-matrix-zeroes", "rotate-array",
        "rotate-image", "spiral-matrix", "sort-colors", "next-permutation",
        "maximum-product-subarray", "contiguous-array", "first-missing-positive",
    ]),
    ("Two Pointers", [
        "valid-palindrome", "reverse-string", "remove-duplicates-from-sorted-array",
        "remove-element", "merge-sorted-array", "squares-of-a-sorted-array",
        "is-subsequence", "valid-palindrome-ii",
        "two-sum-ii-input-array-is-sorted", "3sum", "container-with-most-water",
        "remove-duplicates-from-sorted-array-ii", "3sum-closest", "4sum",
        "trapping-rain-water",
    ]),
    ("Strings", [
        "longest-common-prefix", "length-of-last-word",
        "find-the-index-of-the-first-occurrence-in-a-string", "roman-to-integer",
        "add-binary", "ransom-note", "first-unique-character-in-a-string",
        "reverse-vowels-of-a-string", "add-strings", "longest-palindrome",
        "reverse-words-in-a-string", "integer-to-roman",
        "longest-palindromic-substring", "palindromic-substrings",
        "string-to-integer-atoi", "multiply-strings", "zigzag-conversion",
        "count-and-say", "compare-version-numbers", "text-justification",
    ]),
    ("Sliding Window", [
        "maximum-average-subarray-i", "contains-duplicate-ii",
        "longest-substring-without-repeating-characters",
        "longest-repeating-character-replacement", "permutation-in-string",
        "find-all-anagrams-in-a-string", "minimum-size-subarray-sum",
        "fruit-into-baskets", "max-consecutive-ones-iii",
        "minimum-window-substring", "sliding-window-maximum",
    ]),
    ("Stack and Queue", [
        "valid-parentheses", "min-stack", "implement-queue-using-stacks",
        "implement-stack-using-queues", "next-greater-element-i",
        "evaluate-reverse-polish-notation", "daily-temperatures", "car-fleet",
        "next-greater-element-ii", "decode-string", "simplify-path",
        "remove-k-digits", "asteroid-collision", "basic-calculator-ii",
        "largest-rectangle-in-histogram",
    ]),
    ("Binary Search", [
        "binary-search", "search-insert-position", "sqrtx", "first-bad-version",
        "valid-perfect-square", "search-a-2d-matrix", "koko-eating-bananas",
        "find-minimum-in-rotated-sorted-array",
        "search-in-rotated-sorted-array", "search-in-rotated-sorted-array-ii",
        "find-first-and-last-position-of-element-in-sorted-array",
        "find-peak-element", "capacity-to-ship-packages-within-d-days",
        "time-based-key-value-store", "median-of-two-sorted-arrays",
    ]),
    ("Linked List", [
        "reverse-linked-list", "merge-two-sorted-lists", "linked-list-cycle",
        "middle-of-the-linked-list", "remove-duplicates-from-sorted-list",
        "palindrome-linked-list", "intersection-of-two-linked-lists",
        "remove-linked-list-elements", "reorder-list",
        "remove-nth-node-from-end-of-list", "add-two-numbers",
        "linked-list-cycle-ii", "swap-nodes-in-pairs", "odd-even-linked-list",
        "rotate-list", "sort-list", "copy-list-with-random-pointer",
        "lru-cache", "merge-k-sorted-lists", "reverse-nodes-in-k-group",
    ]),
    ("Trees", [
        "maximum-depth-of-binary-tree", "invert-binary-tree", "same-tree",
        "symmetric-tree", "binary-tree-inorder-traversal",
        "binary-tree-preorder-traversal", "binary-tree-postorder-traversal",
        "path-sum", "diameter-of-binary-tree", "balanced-binary-tree",
        "minimum-depth-of-binary-tree", "subtree-of-another-tree",
        "lowest-common-ancestor-of-a-binary-search-tree",
        "convert-sorted-array-to-binary-search-tree",
        "binary-tree-level-order-traversal", "binary-tree-right-side-view",
        "count-good-nodes-in-binary-tree", "validate-binary-search-tree",
        "kth-smallest-element-in-a-bst",
        "construct-binary-tree-from-preorder-and-inorder-traversal",
        "binary-tree-zigzag-level-order-traversal", "path-sum-ii",
        "flatten-binary-tree-to-linked-list", "sum-root-to-leaf-numbers",
        "populating-next-right-pointers-in-each-node", "delete-node-in-a-bst",
        "lowest-common-ancestor-of-a-binary-tree", "house-robber-iii",
        "binary-tree-maximum-path-sum", "serialize-and-deserialize-binary-tree",
    ]),
    ("Backtracking", [
        "subsets", "subsets-ii", "permutations", "permutations-ii",
        "combinations", "combination-sum", "combination-sum-ii",
        "combination-sum-iii", "letter-combinations-of-a-phone-number",
        "generate-parentheses", "word-search", "palindrome-partitioning",
        "restore-ip-addresses", "partition-to-k-equal-sum-subsets", "n-queens",
    ]),
    ("Heap and Priority Queue", [
        "kth-largest-element-in-a-stream", "last-stone-weight",
        "k-closest-points-to-origin", "kth-largest-element-in-an-array",
        "top-k-frequent-words", "sort-characters-by-frequency",
        "reorganize-string", "task-scheduler", "ugly-number-ii",
        "design-twitter", "find-median-from-data-stream",
    ]),
    ("Graphs", [
        "flood-fill", "island-perimeter", "find-center-of-star-graph",
        "find-the-town-judge", "find-if-path-exists-in-graph",
        "number-of-islands", "max-area-of-island", "clone-graph",
        "pacific-atlantic-water-flow", "surrounded-regions", "rotting-oranges",
        "01-matrix", "keys-and-rooms", "number-of-provinces",
        "is-graph-bipartite", "course-schedule", "course-schedule-ii",
        "redundant-connection", "accounts-merge", "network-delay-time",
        "cheapest-flights-within-k-stops", "min-cost-to-connect-all-points",
        "word-ladder", "reconstruct-itinerary", "swim-in-rising-water",
    ]),
    ("Dynamic Programming", [
        "climbing-stairs", "fibonacci-number", "n-th-tribonacci-number",
        "min-cost-climbing-stairs", "pascals-triangle-ii", "house-robber",
        "house-robber-ii", "decode-ways", "coin-change", "word-break",
        "longest-increasing-subsequence", "partition-equal-subset-sum",
        "unique-paths", "unique-paths-ii", "minimum-path-sum", "triangle",
        "perfect-squares", "combination-sum-iv", "ones-and-zeroes",
        "longest-common-subsequence", "longest-palindromic-subsequence",
        "delete-operation-for-two-strings", "maximum-length-of-repeated-subarray",
        "longest-string-chain", "best-time-to-buy-and-sell-stock-ii",
        "best-time-to-buy-and-sell-stock-with-cooldown",
        "best-time-to-buy-and-sell-stock-with-transaction-fee",
        "best-time-to-buy-and-sell-stock-iii", "coin-change-ii", "target-sum",
        "maximal-square", "number-of-longest-increasing-subsequence",
        "russian-doll-envelopes", "longest-increasing-path-in-a-matrix",
        "interleaving-string", "edit-distance", "distinct-subsequences",
        "wildcard-matching", "regular-expression-matching", "burst-balloons",
    ]),
    ("Greedy", [
        "assign-cookies", "lemonade-change", "can-place-flowers", "h-index",
        "jump-game", "jump-game-ii", "gas-station", "candy",
        "hand-of-straights", "merge-triplets-to-form-target-triplet",
        "partition-labels", "valid-parenthesis-string",
        "queue-reconstruction-by-height", "boats-to-save-people",
        "minimum-number-of-arrows-to-burst-balloons",
    ]),
    ("Intervals", [
        "summary-ranges", "my-calendar-i", "car-pooling", "merge-intervals",
        "insert-interval", "non-overlapping-intervals",
        "remove-covered-intervals", "interval-list-intersections",
    ]),
    ("Math and Bit Manipulation", [
        "palindrome-number", "fizz-buzz", "power-of-two", "number-of-1-bits",
        "counting-bits", "reverse-bits", "hamming-distance", "add-digits",
        "ugly-number", "happy-number", "excel-sheet-column-number",
        "excel-sheet-column-title", "sum-of-two-integers", "reverse-integer",
        "factorial-trailing-zeroes", "count-primes", "powx-n",
        "single-number-ii", "single-number-iii", "bitwise-and-of-numbers-range",
    ]),
    ("Trie and Design", [
        "implement-trie-prefix-tree", "design-hashset", "design-hashmap",
        "design-browser-history", "insert-delete-getrandom-o1",
        "design-add-and-search-words-data-structure",
        "binary-search-tree-iterator", "flatten-nested-list-iterator",
        "word-search-ii", "lfu-cache",
    ]),
]

TOTAL = sum(len(s) for _, s in ROADMAP)
PROGRESS_FILE = "progress.json"


class ApiError(Exception):
    pass


def post(url, payload, headers, retries=3):
    headers = {"User-Agent": BROWSER_UA, "Accept": "application/json", **headers}
    for attempt in range(retries):
        req = urllib.request.Request(url, data=json.dumps(payload).encode(), headers=headers)
        try:
            return json.load(urllib.request.urlopen(req, timeout=180))
        except urllib.error.HTTPError as e:
            body = e.read().decode()[:500]
            print("HTTP ERROR", e.code, "from", url)
            print(body)
            if e.code in (429, 500, 502, 503) and attempt < retries - 1:
                time.sleep(30 * (attempt + 1))
                continue
            raise ApiError(f"HTTP {e.code} from {url}")
        except Exception as e:
            print("Network error:", e)
            if attempt < retries - 1:
                time.sleep(10)
                continue
            raise ApiError(str(e))


EMOJI_RE = re.compile(
    "[\U0001F000-\U0001FFFF\U00002600-\U000027BF\U00002300-\U000023FF"
    "\U00002B00-\U00002BFF\U0000FE0F\U0000200D]+",
    flags=re.UNICODE,
)


def strip_emoji(s):
    return EMOJI_RE.sub("", s) if isinstance(s, str) else s


def clean(obj):
    if isinstance(obj, str):
        return strip_emoji(obj)
    if isinstance(obj, list):
        return [clean(x) for x in obj]
    return obj


def html_to_md(h):
    h = re.sub(
        r"<pre>(.*?)</pre>",
        lambda m: "\n```\n" + re.sub(r"<[^>]+>", "", m.group(1)).strip() + "\n```\n",
        h, flags=re.S,
    )
    h = re.sub(r"<sup>(.*?)</sup>", r"^\1", h)
    h = re.sub(r"<strong[^>]*>|</strong>|<b>|</b>", "**", h)
    h = re.sub(r"</?code>", "`", h)
    h = re.sub(r"<li>", "- ", h)
    h = re.sub(r"</p>|<br\s*/?>|</li>|</ul>", "\n", h)
    h = re.sub(r"<[^>]+>", "", h)
    h = html.unescape(h)
    return re.sub(r"\n{3,}", "\n\n", h).strip()


def load_progress():
    if os.path.exists(PROGRESS_FILE):
        return json.load(open(PROGRESS_FILE, encoding="utf-8"))
    return []


def pick_next(progress):
    seen = {p["slug"] for p in progress}
    for ti, (topic, slugs) in enumerate(ROADMAP, 1):
        for slug in slugs:
            if slug not in seen:
                return ti, topic, slug
    return None


def fetch_problem(slug):
    r = post(
        "https://leetcode.com/graphql",
        {
            "query": """query q($s: String!) { question(titleSlug: $s) {
                questionFrontendId title titleSlug difficulty content isPaidOnly } }""",
            "variables": {"s": slug},
        },
        {"Content-Type": "application/json", "Referer": "https://leetcode.com"},
    )
    return (r.get("data") or {}).get("question")


KEYS = ["pattern", "brute_force", "intuition", "approach", "steps", "dry_run",
        "time", "time_why", "space", "space_why", "edge_cases",
        "interview_tips", "follow_ups", "takeaways", "related", "code"]


def ask_groq(title, text, topic):
    prompt = f"""You are an expert interview coach teaching DSA. Solve this LeetCode problem in Python.
Topic: {topic}
Title: {title}

{text}

Do NOT use any emojis anywhere in your answer.

Reply ONLY with a JSON object with these keys:
"pattern": string, the name of the core pattern/technique (e.g. "Hash Map lookup", "Two Pointers"),
"brute_force": string, the naive approach with its complexity, in 1-3 sentences,
"intuition": string, 2-4 sentences explaining WHY the optimal idea works (use **bold** for key terms),
"approach": string, short paragraph naming the technique/data structure (use **bold** for key terms),
"steps": list of strings, 4-7 clear algorithm steps (use **bold** for key terms),
"dry_run": list of strings, a small example traced step by step,
"time": string like "O(n)",
"time_why": string, one sentence,
"space": string like "O(1)",
"space_why": string, one sentence,
"edge_cases": list of strings,
"interview_tips": list of strings, 2-4 tips on what to say/clarify/mention in a real interview,
"follow_ups": list of strings, 1-3 likely follow-up questions an interviewer may ask,
"takeaways": list of strings, 2-3 patterns to remember (use **bold** for key terms),
"related": list of strings, 2-4 titles of similar LeetCode problems,
"code": string, full Python solution using `class Solution` exactly like LeetCode's template,
with short helpful comments. Do not include markdown fences inside the code string."""
    for attempt in range(3):
        res = post(
            "https://api.groq.com/openai/v1/chat/completions",
            {
                "model": MODEL,
                "temperature": 0.2,
                "max_tokens": 8000,
                "reasoning_effort": "low",
                "response_format": {"type": "json_object"},
                "messages": [{"role": "user", "content": prompt}],
            },
            {"Content-Type": "application/json", "Authorization": f"Bearer {GROQ_KEY}"},
        )
        try:
            d = json.loads(res["choices"][0]["message"]["content"])
            for k in KEYS:
                assert k in d, f"missing {k}"
            return {k: clean(v) for k, v in d.items()}
        except Exception as e:
            print("Bad JSON, retrying...", e)
            time.sleep(5)
    raise ApiError("Groq did not return valid JSON")


def bullets(items):
    return "\n".join(f"- {i}" for i in items)


def numbered(items):
    return "\n".join(f"{n}. {s}" for n, s in enumerate(items, 1))


def build_readme(q, topic, d):
    pid = int(q["questionFrontendId"])
    return f"""# {pid}. {q['title']}

| | |
|---|---|
| **Difficulty** | {q['difficulty']} |
| **Topic** | {topic} |
| **Pattern** | {d['pattern']} |
| **LeetCode** | [Open problem](https://leetcode.com/problems/{q['titleSlug']}/) |
| **Solution** | [solution.py](./solution.py) |

---

## Problem

{strip_emoji(html_to_md(q['content']))}

---

## Brute Force

{d['brute_force']}

## Intuition

{d['intuition']}

## Optimal Approach

{d['approach']}

## Step-by-Step Algorithm

{numbered(d['steps'])}

## Dry Run

{bullets(d['dry_run'])}

---

## Code

```python
{d['code'].strip()}
```

## Complexity

| | Complexity | Why |
|---|---|---|
| **Time** | `{d['time']}` | {d['time_why']} |
| **Space** | `{d['space']}` | {d['space_why']} |

## Edge Cases

{bullets(d['edge_cases'])}

---

## Interview Tips

{bullets(d['interview_tips'])}

## Follow-up Questions

{bullets(d['follow_ups'])}

## Key Takeaways

{bullets(d['takeaways'])}

## Related Problems

{bullets(d['related'])}

---

> Draft generated with Groq (`{MODEL}`). Review before relying on it.
"""


def build_root_readme(progress):
    done = [p for p in progress if p.get("status", "done") == "done"]
    n = len(done)
    filled = int(20 * n / TOTAL)
    bar = "#" * filled + "-" * (20 - filled)
    cnt = {k: sum(1 for p in done if p["difficulty"] == k) for k in ("Easy", "Medium", "Hard")}
    lines = [
        "# LeetCode Top 300 - Interview Prep",
        "",
        "Most popular **interview problems**, **topic wise** and ordered **Easy to Hard**. "
        f"**{PER_DAY} problems/day**, auto-updated with GitHub Actions.",
        "",
        f"**Progress:** `[{bar}]` **{n} / {TOTAL}**",
        "",
        f"Easy: **{cnt['Easy']}** | Medium: **{cnt['Medium']}** | Hard: **{cnt['Hard']}**",
        "",
        "## Topics",
        "",
        "| # | Topic | Solved |",
        "|---|-------|--------|",
    ]
    for ti, (topic, slugs) in enumerate(ROADMAP, 1):
        c = sum(1 for p in done if p["topic"] == topic)
        anchor = f"{ti}-{re.sub(r'[^a-z0-9]+', '-', topic.lower()).strip('-')}"
        lines.append(f"| {ti} | [{topic}](#{anchor}) | {c} / {len(slugs)} |")
    lines.append("")
    for ti, (topic, slugs) in enumerate(ROADMAP, 1):
        items = [p for p in done if p["topic"] == topic]
        lines += [
            f"## {ti}. {topic}",
            "",
            f"**{len(items)} / {len(slugs)} solved**",
            "",
        ]
        if items:
            lines += [
                "| # | Problem | Difficulty | LeetCode |",
                "|---|---------|------------|----------|",
            ]
            for p in items:
                lines.append(
                    f"| {p['id']} | [{p['title']}](./{p['path']}) | "
                    f"{p['difficulty']} | "
                    f"[Link](https://leetcode.com/problems/{p['slug']}/) |"
                )
        else:
            lines.append("_Coming soon..._")
        lines.append("")
    open("README.md", "w", encoding="utf-8").write("\n".join(lines))


def solve_one(progress):
    nxt = pick_next(progress)
    if not nxt:
        print("All problems in roadmap are done!")
        return False
    ti, topic, slug = nxt
    print("Next problem:", slug, "| Topic:", topic)

    q = fetch_problem(slug)
    if not q or not q.get("content") or q.get("isPaidOnly"):
        print(f"Skipping '{slug}' (premium or not found)")
        progress.append({"slug": slug, "topic": topic, "status": "skipped"})
        return True

    text = html_to_md(q["content"])
    d = ask_groq(q["title"], text, topic)

    topic_dir = f"{ti:02d}-{re.sub(r'[^A-Za-z0-9]+', '-', topic).strip('-')}"
    folder = f"{topic_dir}/{int(q['questionFrontendId']):04d}-{slug}"
    os.makedirs(folder, exist_ok=True)
    open(f"{folder}/README.md", "w", encoding="utf-8").write(build_readme(q, topic, d))
    open(f"{folder}/solution.py", "w", encoding="utf-8").write(d["code"].strip() + "\n")

    progress.append({
        "id": int(q["questionFrontendId"]), "title": q["title"], "slug": slug,
        "difficulty": q["difficulty"], "topic": topic, "path": folder,
        "status": "done",
    })
    print("Created", folder)
    return True


def save(progress):
    json.dump(progress, open(PROGRESS_FILE, "w", encoding="utf-8"), indent=2)
    build_root_readme(progress)


def main():
    progress = load_progress()
    solved_now = 0
    error = False
    while solved_now < PER_DAY:
        try:
            more = solve_one(progress)
        except ApiError as e:
            print("Stopped:", e)
            error = True
            break
        if not more:
            break
        if progress and progress[-1].get("status") == "done":
            solved_now += 1
        save(progress)
        time.sleep(10)
    save(progress)
    if error and solved_now == 0:
        sys.exit(1)


main()
