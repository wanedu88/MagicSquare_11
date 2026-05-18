# 04. User Entity Export Transcript Prompt

## Transcript

### User

```text
.cursorrules를 읽고
MagicSquare의 User 엔티티 클래스를 ECB 패턴으로 작성해줘.
타입힌트, Google docstring, pytest 테스트 파일도 함께 만들어줘.
```

### Assistant

```text
요청을 처리하기 전에 .cursorrules를 읽고 현재 프로젝트 구조를 확인한다.
ECB 패턴 기준으로 User 엔티티는 entity 레이어에 배치한다.
TDD 규칙에 따라 pytest 테스트 파일을 먼저 작성한 뒤 최소 구현을 추가한다.
```

### Generated Files

```text
entity/__init__.py
entity/user.py
tests/entity/test_user.py
```

### Implementation Requirements

```text
- User 엔티티는 MagicSquare 프로젝트의 entity 레이어에 작성한다.
- 모든 함수와 메서드에는 타입힌트를 작성한다.
- public 클래스와 public 메서드에는 Google 스타일 docstring을 작성한다.
- pytest 테스트 파일을 함께 작성한다.
- 테스트는 User 생성, 속성 저장, 표시 이름 반환, 잘못된 입력 예외를 검증한다.
```

### Verification Notes

```text
- 린터 오류가 없는지 확인한다.
- 가능한 경우 pytest를 실행한다.
- Python 또는 pytest 명령을 사용할 수 없으면 실행 불가 사유를 기록한다.
```

## Reusable Prompt

```text
.cursorrules를 읽고 현재 프로젝트 규칙을 따른다.
MagicSquare 프로젝트에 User 엔티티 클래스를 ECB 패턴으로 작성한다.

요구사항:
- User 엔티티는 entity 레이어에 둔다.
- 타입힌트를 모든 함수 파라미터와 반환값에 작성한다.
- Google 스타일 docstring을 public 클래스와 public 메서드에 작성한다.
- pytest 테스트 파일을 함께 작성한다.
- TDD 흐름에 따라 테스트를 먼저 작성하고 최소 구현으로 통과시키는 구조로 진행한다.
- 작업 후 린터 오류와 테스트 실행 가능 여부를 보고한다.
```
