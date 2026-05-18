# MagicSquare

MagicSquare는 마방진 생성, 검증, 테스트를 TDD 방식으로 구현하기 위한 프로젝트입니다.
프로젝트 규칙은 ECB(Entity-Control-Boundary) 패턴과 pytest 기반 테스트 흐름을 기준으로 정리되어 있습니다.

## Project Goals

- 정확한 마방진 생성 로직 구현
- 검증 가능한 도메인 규칙 분리
- TDD 흐름에 따른 테스트 우선 개발
- ECB 레이어 경계 유지

## Current Structure

```text
.
├── .cursor/
│   └── rules/
│       ├── *.mdc
│       └── cpp/
│           └── *.mdc
├── entity/
│   ├── __init__.py
│   └── user.py
├── tests/
│   └── entity/
│       └── test_user.py
├── Report/
├── Prompting/
└── .cursorrules
```

## Architecture

이 프로젝트는 ECB 패턴을 따릅니다.

- `boundary`: 외부 입출력 담당
- `control`: 비즈니스 로직 흐름 담당
- `entity`: 도메인 데이터 및 규칙 담당

의존성 방향은 `boundary -> control -> entity`만 허용합니다.

## Implemented Domain

현재 구현된 도메인 엔티티:

- `entity.user.User`

`User` 엔티티는 사용자 이름과 이메일을 보관하며, 빈 이름과 `@`가 없는 이메일을 거부합니다.

## Rules

프로젝트 규칙은 두 형태로 관리됩니다.

- `.cursorrules`: 전체 규칙 원본
- `.cursor/rules/*.mdc`: Cursor Rule 분리본

C++ 마이그레이션 규칙은 `.cursor/rules/cpp/*.mdc`에 별도로 정리되어 있습니다.

## Testing

테스트 프레임워크는 `pytest`를 기준으로 합니다.

```powershell
pytest
```

현재 환경에서 `pytest` 명령이 설치되어 있지 않으면 Python과 pytest 설치 후 실행해야 합니다.

## Development Workflow

1. 실패하는 테스트를 먼저 작성합니다.
2. 테스트 실패를 확인합니다.
3. 테스트를 통과시키는 최소 구현을 작성합니다.
4. 테스트가 통과하는 상태에서만 리팩터링합니다.
