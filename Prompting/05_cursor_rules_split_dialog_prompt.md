# 05. Cursor Rules Split Dialog Prompt

## Dialog Prompt

### User

```text
.cursor/rules에 .cursorrules를 분리해서 *.mdc 생성해줘
```

### Assistant

```text
.cursorrules를 읽고 최상위 섹션을 Cursor Rule 형식의 .mdc 파일로 분리한다.
각 .mdc 파일은 YAML frontmatter와 Markdown 본문을 포함한다.
항상 적용할 규칙은 alwaysApply: true로 설정한다.
Python 파일에만 적용할 규칙은 globs: **/*.py를 사용한다.
pytest 테스트 파일에 적용할 규칙은 globs: **/test_*.py를 사용한다.
```

## Expected Rule Files

```text
.cursor/rules/project-overview.mdc
.cursor/rules/python-code-style.mdc
.cursor/rules/ecb-architecture.mdc
.cursor/rules/tdd-rules.mdc
.cursor/rules/pytest-testing.mdc
.cursor/rules/forbidden-patterns.mdc
.cursor/rules/file-structure.mdc
.cursor/rules/ai-behavior.mdc
```

## Section Mapping

```text
project -> project-overview.mdc
code_style -> python-code-style.mdc
architecture -> ecb-architecture.mdc
tdd_rules -> tdd-rules.mdc
testing -> pytest-testing.mdc
forbidden -> forbidden-patterns.mdc
file_structure -> file-structure.mdc
ai_behavior -> ai-behavior.mdc
```

## Reusable Prompt

```text
.cursorrules를 읽고 .cursor/rules 디렉토리에 Cursor Rule .mdc 파일로 분리해줘.

요구사항:
- .cursorrules의 최상위 섹션별로 별도 .mdc 파일을 생성한다.
- 각 .mdc 파일은 YAML frontmatter를 포함한다.
- project, architecture, tdd_rules, file_structure, ai_behavior는 alwaysApply: true로 설정한다.
- code_style과 forbidden은 Python 파일 대상 규칙으로 만들고 globs: **/*.py를 설정한다.
- testing은 pytest 테스트 파일 대상 규칙으로 만들고 globs: **/test_*.py를 설정한다.
- 기존 .mdc 파일이 있으면 현재 .cursorrules 내용 기준으로 갱신한다.
- 작업 후 생성된 .mdc 파일 목록과 린터 확인 결과를 보고한다.
```
