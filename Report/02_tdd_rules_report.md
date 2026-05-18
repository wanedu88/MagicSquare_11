# 02. TDD Rules Report

## Summary

`.cursorrules` 파일의 `tdd_rules` 섹션을 TDD 흐름에 맞게 작성했다.

## Updated Section

- `tdd_rules`

## Added Rules

### red_phase

- 테스트를 먼저 작성한다.
- 테스트 실패를 확인한 뒤 다음 단계로 진행한다.

### green_phase

- 테스트를 통과시키기 위한 최소 코드만 작성한다.
- 이 단계에서는 리팩터링을 금지한다.

### refactor_phase

- 기능 변경 없이 구조를 개선한다.
- 기존 테스트 커버리지를 유지한다.

## Result

TDD의 Red, Green, Refactor 단계별 진행 조건이 YAML 형식으로 반영되었다.
