# 🤝 Contributing to This Project

Thanks for considering a contribution! To keep the project clean, consistent, and automatable, we follow the **Conventional Commits** standard for commit messages.

## ✅ Commit Message Format

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

### 🔑 Common Commit Types

| Type        | Use for... |
|-------------|------------|
| **feat**    | A new feature |
| **fix**     | A bug fix |
| **docs**    | Documentation changes only |
| **style**   | Code style changes (formatting, whitespace) |
| **refactor**| Code refactoring (no bug fix or feature) |
| **perf**    | Performance improvements |
| **test**    | Adding or improving tests |
| **chore**   | Maintenance (deps, build config, etc.) |
| **build**   | Build system or tooling changes |
| **ci**      | Continuous integration / deployment config |
| **revert**  | Reverting a previous commit |

### 🔍 Optional Scope

```bash
feat(auth): add OAuth2 login
fix(api): handle 500 error case
chore(deps): bump requests to 2.31.0
```

### 🚨 Breaking Changes

```
feat!: remove deprecated /v1 endpoint
```

or

```
fix: change response format

BREAKING CHANGE: the /users endpoint now returns JSON instead of XML
```

### 💬 Examples

```bash
feat: add user registration flow
fix: prevent crash on null user
docs: update README with new usage
style: reformat with black
refactor(api): simplify query logic
perf: cache image thumbnails
test: add test for edge case in calculator
chore: upgrade mypy to latest version
ci: add GitHub Actions for tests
```

### 🔧 Tooling (optional)

```bash
pip install commitizen
cz commit
cz bump
```
