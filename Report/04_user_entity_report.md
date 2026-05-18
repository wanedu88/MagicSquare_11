# 04. User Entity Report

## Summary

`.cursorrules`의 TDD 및 ECB 기준에 따라 MagicSquare 프로젝트의 `User` 엔티티와 pytest 테스트를 작성했다.

## Created Files

- `entity/__init__.py`
- `entity/user.py`
- `tests/entity/test_user.py`

## Implementation

- `User` 엔티티는 `entity` 레이어에 배치했다.
- `name`과 `email`을 가진 불변 dataclass로 작성했다.
- 모든 public 메서드에 타입힌트와 Google 스타일 docstring을 추가했다.
- 빈 이름은 `ValueError`로 거부한다.
- `@`가 없는 이메일은 `ValueError`로 거부한다.
- `display_name()`은 표시용 사용자 이름을 반환한다.

## Testing

- `tests/entity/test_user.py`에 pytest 테스트를 작성했다.
- 사용자 이름과 이메일 저장 동작을 검증한다.
- 표시 이름 반환 동작을 검증한다.
- 빈 이름과 잘못된 이메일 입력 예외를 검증한다.

## Verification

- 린터 오류 없음.
- `python -m pytest`, `py -m pytest`, `pytest` 실행을 시도했지만 현재 환경에서 Python 또는 pytest 명령을 찾을 수 없어 테스트는 실행하지 못했다.
