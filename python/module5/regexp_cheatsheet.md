# 🛠️ Advanced Regular Expressions (Regex) - Instructor Cheat Sheet

This cheat sheet is intended for **Instructors** to quickly reference advanced Regex patterns, edge cases, and lookarounds in case students ask questions beyond the scope of the basic Module 5 handout.

---

## 1. The Core Engine (Tokens & Classes)

| Token | Matches | Example Match |
| :--- | :--- | :--- |
| `.` | Any character (except newline unless `re.DOTALL` is used) | `c.t` ➔ `cat`, `c0t` |
| `\w` | Word character (Alphanumeric + `_`) | `\w+` ➔ `user_name123` |
| `\W` | NON-word character | `\W` ➔ `@`, `!`, ` ` |
| `\d` | Digit (0-9) | `\d+` ➔ `404` |
| `\D` | NON-digit | `\D+` ➔ `error` |
| `\s` | Whitespace (space, tab `\t`, newline `\n`) | `\s+` ➔ `   ` |
| `\S` | NON-whitespace | `\S+` ➔ `text` |

## 2. Anchors & Boundaries

Anchors don't match characters; they match **positions** in the string.

| Anchor | Description | Example |
| :--- | :--- | :--- |
| `^` | Start of the string (or line with `re.MULTILINE`) | `^ERROR` ➔ Must start with ERROR |
| `$` | End of the string (or line with `re.MULTILINE`) | `success$` ➔ Must end with success |
| `\b` | Word Boundary (transition between `\w` and `\W`) | `\bcat\b` ➔ Matches "cat" but NOT "catalog" |
| `\B` | NON-word Boundary | `\Bcat\b` ➔ Matches "cat" in "tomcat" |

## 3. Quantifiers: Greedy vs. Lazy

By default, Regex is **Greedy** (it matches as much text as possible). Adding `?` makes it **Lazy** (it matches as little as possible).

| Greedy | Lazy | Description |
| :--- | :--- | :--- |
| `*` | `*?` | 0 or more times |
| `+` | `+?` | 1 or more times |
| `?` | `??` | 0 or 1 time (optional) |
| `{n}` | - | Exactly *n* times |
| `{n,}` | `{n,}?` | *n* or more times |
| `{n,m}`| `{n,m}?`| Between *n* and *m* times |

💡 **The Lazy Trap:** `<.*>` matching `<div>Hello</div>` will grab the *entire string*. `<.*?>` will grab *just* `<div>`.

## 4. Groups, Sets, and Alternation

| Syntax | Name | Description |
| :--- | :--- | :--- |
| `[abc]` | Character Set | Matches ONE of: a, b, or c. |
| `[^abc]` | Negated Set | Matches ONE character that is NOT a, b, or c. |
| `[a-z]` | Range | Matches any lowercase letter. |
| `(abc)` | Capture Group | Groups tokens together and captures the match for later extraction (`match.group(1)`). |
| `(?:abc)`| Non-Capturing Group | Groups tokens for logic (e.g., quantifiers), but does NOT save the data. |
| <code>a&#124;b</code> | Alternation (OR) | Matches `a` OR `b`. |

## 5. Advanced: Lookaround Assertions

Lookarounds check the surroundings of a match **without consuming characters**. They are 0-width assertions (like `^` and `$`).

| Syntax | Name | Description | Example |
| :--- | :--- | :--- | :--- |
| `(?=...)` | Positive Lookahead | "Is followed by" | `admin(?=\s logged)` ➔ Matches "admin" only if followed by " logged". |
| `(?!...)` | Negative Lookahead | "Is NOT followed by" | `admin(?!\s failed)` ➔ Matches "admin" only if NOT followed by " failed". |
| `(?<=...)`| Positive Lookbehind | "Is preceded by" | `(?<=User\s)admin` ➔ Matches "admin" only if preceded by "User ". |
| `(?<!...)`| Negative Lookbehind | "Is NOT preceded by" | `(?<!Super)admin` ➔ Matches "admin" only if NOT preceded by "Super". |

## 6. Python `re` Module Flags

Pass these as the third argument (or second if no flags exist) to modify engine behavior: `re.search(pattern, string, flags=re.IGNORECASE)`.

*   **`re.IGNORECASE` (`re.I`)**: Case-insensitive matching.
*   **`re.MULTILINE` (`re.M`)**: Makes `^` and `$` match the start/end of *every line* (after a `\n`), not just the start/end of the whole string.
*   **`re.DOTALL` (`re.S`)**: Makes the `.` token match *everything*, including newlines (`\n`).

---

## 7. Common DevOps Regex Patterns (Copy & Paste)

### IP Addresses (Basic vs Strict)
*   **Basic (Forgiving):** `r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"`
    *   *Matches: `192.168.1.1` but also accidentally matches invalid IPs like `999.999.999.999`.*
*   **Strict (Accurate IPv4):** `r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"`

### MAC Addresses
*   **Colon or Hyphen Separated:** `r"^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$"`

### Email Addresses (RFC Standard Simplified)
*   **Standard Business Emails:** `r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"`

### Date / Time Extraction
*   **ISO 8601 Date (`YYYY-MM-DD`):** `r"\d{4}-\d{2}-\d{2}"`
*   **Time (`HH:MM:SS`):** `r"\d{2}:\d{2}:\d{2}"`
