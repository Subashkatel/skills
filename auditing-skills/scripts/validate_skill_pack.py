#!/usr/bin/env python3
from __future__ import annotations
import json, re, sys
from pathlib import Path

NAME_RE = re.compile(r'^[a-z0-9-]{1,64}$')
BAD_PHRASES = [
    'show your reasoning',
    'chain of thought',
    'chain-of-thought',
    'reveal your reasoning',
    'explain your internal reasoning',
    'do not stop until',
    'must always use',
]

def parse_frontmatter(text: str):
    if not text.startswith('---\n'):
        raise ValueError('missing frontmatter')
    end = text.find('\n---\n', 4)
    if end == -1:
        raise ValueError('unterminated frontmatter')
    fm_text = text[4:end]
    body = text[end+5:]
    fm = {}
    for line in fm_text.splitlines():
        if not line.strip():
            continue
        if ':' not in line:
            raise ValueError(f'bad frontmatter line: {line}')
        k, v = line.split(':', 1)
        fm[k.strip()] = v.strip().strip('"').strip("'")
    return fm, body

def validate_skill(path: Path):
    errors = []
    skill_file = path / 'SKILL.md'
    if not skill_file.exists():
        return ['missing SKILL.md']
    text = skill_file.read_text(encoding='utf-8')
    try:
        fm, body = parse_frontmatter(text)
    except Exception as e:
        return [str(e)]
    name = fm.get('name','')
    desc = fm.get('description','')
    if not NAME_RE.match(name):
        errors.append(f'invalid name: {name!r}')
    if name != path.name:
        errors.append(f'name {name!r} does not match directory {path.name!r}')
    if not desc:
        errors.append('empty description')
    if len(desc) > 1024:
        errors.append('description too long')
    if '<' in desc or '>' in desc:
        errors.append('description contains XML-like angle brackets')
    if len(body.splitlines()) > 500:
        errors.append('SKILL.md body exceeds 500 lines')
    lower = text.lower()
    for phrase in BAD_PHRASES:
        if phrase in lower:
            errors.append(f'contains discouraged phrase: {phrase}')
    eval_file = path / 'evals' / 'evals.json'
    if not eval_file.exists():
        errors.append('missing evals/evals.json')
    else:
        try:
            evals = json.loads(eval_file.read_text(encoding='utf-8'))
            if not isinstance(evals, list) or len(evals) < 3:
                errors.append('evals must contain at least 3 cases')
        except Exception as e:
            errors.append(f'bad evals json: {e}')
    # Progressive disclosure: reference/templates/scripts/evals may be nested exactly one level below skill.
    for sub in ['reference', 'templates']:
        d = path / sub
        if d.exists():
            for p in d.rglob('*'):
                if p.is_file() and len(p.relative_to(path).parts) > 2:
                    errors.append(f'deep nested support file: {p.relative_to(path)}')
    return errors

def main() -> int:
    skills_dir = Path(sys.argv[1] if len(sys.argv) > 1 else '.').resolve()
    if not skills_dir.exists():
        print(f'missing skills directory: {skills_dir}')
        return 1
    all_errors = {}
    skill_dirs = sorted([p for p in skills_dir.iterdir() if p.is_dir() and (p / 'SKILL.md').exists()])
    if not skill_dirs:
        print(f'no skill directories found in {skills_dir}')
        return 1
    for skill in skill_dirs:
        errs = validate_skill(skill)
        if errs:
            all_errors[skill.name] = errs
    if all_errors:
        for name, errs in all_errors.items():
            print(f'FAIL {name}')
            for e in errs:
                print(f'  - {e}')
        return 1
    print(f'All {len(skill_dirs)} skills passed structural validation.')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
