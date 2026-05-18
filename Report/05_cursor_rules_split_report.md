# 05. Cursor Rules Split Report

## Summary

`.cursorrules`의 최상위 섹션을 Cursor Rule 형식에 맞춰 `.cursor/rules/*.mdc` 파일로 분리했다.

## Source

- `.cursorrules`

## Created And Updated Files

- `.cursor/rules/project-overview.mdc`
- `.cursor/rules/python-code-style.mdc`
- `.cursor/rules/ecb-architecture.mdc`
- `.cursor/rules/tdd-rules.mdc`
- `.cursor/rules/pytest-testing.mdc`
- `.cursor/rules/forbidden-patterns.mdc`
- `.cursor/rules/file-structure.mdc`
- `.cursor/rules/ai-behavior.mdc`

## Rule Mapping

- `project` -> `project-overview.mdc`
- `code_style` -> `python-code-style.mdc`
- `architecture` -> `ecb-architecture.mdc`
- `tdd_rules` -> `tdd-rules.mdc`
- `testing` -> `pytest-testing.mdc`
- `forbidden` -> `forbidden-patterns.mdc`
- `file_structure` -> `file-structure.mdc`
- `ai_behavior` -> `ai-behavior.mdc`

## Scope

- Always applied rules:
  - `project-overview.mdc`
  - `ecb-architecture.mdc`
  - `tdd-rules.mdc`
  - `file-structure.mdc`
  - `ai-behavior.mdc`
- Python file rules:
  - `python-code-style.mdc`
  - `forbidden-patterns.mdc`
- Test file rules:
  - `pytest-testing.mdc`

## Verification

- `.cursor/rules` 디렉토리에 총 8개의 `.mdc` 파일이 생성 또는 갱신되었다.
- 생성된 규칙 파일에서 린터 오류는 발견되지 않았다.
