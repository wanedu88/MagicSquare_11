# 06. C++ Rules Migration Report

## Summary

기존 `.cursor/rules`의 `.mdc` 규칙을 C++ 프로젝트 방식으로 마이그레이션해 `.cursor/rules/cpp`에 생성했다.

## Source Rules

- `.cursor/rules/project-overview.mdc`
- `.cursor/rules/python-code-style.mdc`
- `.cursor/rules/ecb-architecture.mdc`
- `.cursor/rules/tdd-rules.mdc`
- `.cursor/rules/pytest-testing.mdc`
- `.cursor/rules/forbidden-patterns.mdc`
- `.cursor/rules/file-structure.mdc`
- `.cursor/rules/ai-behavior.mdc`

## Created C++ Rules

- `.cursor/rules/cpp/project-overview.mdc`
- `.cursor/rules/cpp/cpp-code-style.mdc`
- `.cursor/rules/cpp/ecb-architecture.mdc`
- `.cursor/rules/cpp/tdd-rules.mdc`
- `.cursor/rules/cpp/cpp-testing.mdc`
- `.cursor/rules/cpp/forbidden-patterns.mdc`
- `.cursor/rules/cpp/file-structure.mdc`
- `.cursor/rules/cpp/ai-behavior.mdc`

## Migration Details

- Python 기준 프로젝트 규칙을 C++ 기준으로 변경했다.
- `**/*.py` globs를 `**/*.{cpp,cc,cxx,h,hpp,hxx}`로 변경했다.
- pytest 테스트 규칙을 GoogleTest, Catch2, doctest 등 C++ 테스트 프레임워크 기준으로 변경했다.
- Python 코드 스타일 규칙을 C++17+, RAII, const correctness, smart pointer, header self-containment 기준으로 변경했다.
- 금지 패턴을 `std::cout` 디버깅 출력, 하드코딩 상수, `catch (...)`, raw owning pointer, header 내 `using namespace std;` 기준으로 변경했다.
- 파일 구조를 `include/`, `src/`, `tests/` 기반의 C++ ECB 구조로 변경했다.

## Verification

- `.cursor/rules/cpp` 디렉토리에 총 8개의 `.mdc` 파일이 생성되었다.
- 생성된 C++ 규칙 파일에서 린터 오류는 발견되지 않았다.
