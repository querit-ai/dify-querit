# Contributing to Querit Search Plugin for Dify

Thank you for your interest in contributing to the Querit Dify Plugin! This document provides guidelines and best practices for contributing.

---

## Code of Conduct

By participating in this project, you are expected to uphold our [Code of Conduct](https://github.com/querit-ai/dify-querit/blob/main/CODE_OF_CONDUCT.md). Please report unacceptable behavior to the maintainers.

---

## How to Contribute

### Reporting Bugs

1. **Search existing issues** - Check if the bug has already been reported
2. **Create a new issue** with:
   - Clear title and description
   - Steps to reproduce
   - Expected vs actual behavior
   - Environment details (OS, Python version, etc.)
   - Screenshots if applicable

### Suggesting Features

1. Open a new issue with the `feature` label
2. Describe the feature and its use case
3. Explain why this feature would be valuable
4. Include any relevant mockups or examples

### Pull Requests

1. **Fork** the repository
2. **Create a feature branch**: `git checkout -b feature/my-feature`
3. **Make your changes** and commit with clear messages
4. **Push to your fork** and submit a Pull Request
5. **Fill out the PR template** completely

---

## Development Setup

### Prerequisites

- Python 3.11 or higher
- Git
- A Dify development environment

### Setup Steps

1. Clone your fork:
   ```bash
   git clone https://github.com/YOUR_USERNAME/dify-querit.git
   cd dify-querit
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Copy environment file:
   ```bash
   cp .env.example .env
   ```

5. Add your Querit API key to `.env`

---

## Coding Standards

### Python Style

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guide
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Keep lines under 120 characters

### Type Hints

Use type hints where appropriate:

```python
def search(query: str, count: int = 10) -> list[dict]:
    """Search for query and return results.

    Args:
        query: The search query string
        count: Number of results to return

    Returns:
        List of search result dictionaries
    """
    ...
```

### Commit Messages

Use clear, descriptive commit messages:

```
type(scope): description

[optional body]

[optional footer]
```

Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`

Example:
```
feat(search): add country filter parameter

Add ability to filter search results by country code.
This helps users get region-specific results.

Closes #123
```

---

## Testing

### Running Tests

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_search.py

# Run with coverage
pytest --cov=.
```

### Writing Tests

- Write tests for new features
- Keep tests focused and atomic
- Use descriptive test names: `test_search_returns_results_for_valid_query`

---

## Documentation

### Updating Documentation

- Update README.md for user-facing changes
- Update GUIDE.md for development documentation
- Add docstrings to new functions
- Comment complex logic

### Language

- Use English for code and comments
- Provide multi-language support for user-facing strings (as shown in the YAML files)

---

## Review Process

1. Maintainers will review your PR
2. Address any feedback promptly
3. Once approved, your PR will be merged
4. Thank you for your contribution!

---

## Publishing Releases

This plugin uses the official Dify plugin auto-publish workflow. When you publish a release in this repository, the plugin will be automatically submitted to the Dify Marketplace.

### Release Process

1. **Prepare Changes**: Ensure all code changes are merged to the `main` branch
2. **Update Version**: Bump the version in:
   - `manifest.yaml` (version field)
   - `README.md` (version badge)
3. **Create Release**:
   - Go to [Releases](https://github.com/querit-ai/dify-querit/releases)
   - Click "Draft a new release"
   - Select a tag version (e.g., `v0.0.2`)
   - Publish the release

### What Happens After Release

Once you publish a release:

1. GitHub Actions automatically:
   - Packages the plugin into a `.difypkg` file
   - Creates a new branch in [dify-plugins](https://github.com/querit-ai/dify-plugins)
2. The branch is then merged to the official Dify plugin repository
3. The plugin becomes available in the Dify Marketplace

### Version Naming

Follow semantic versioning:
- `v0.0.1` - Initial release
- `v0.0.2` - Bug fixes
- `v0.1.0` - New features (backward compatible)
- `v1.0.0` - Major version (breaking changes)

### Release Checklist

Before publishing, ensure:
- [ ] Version updated in `manifest.yaml`
- [ ] Version badge updated in `README.md`
- [ ] Changelog added to release notes
- [ ] All tests passing
- [ ] Code follows coding standards

---

## Recognition

Contributors will be recognized in the README.md and on the project repository.

---

## Questions?

- Open an issue for questions
- Check existing [GitHub Issues](https://github.com/querit-ai/dify-querit/issues)
- Contact the maintainers

We appreciate your contributions!
