## ATM Simulator

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/status-complete-brightgreen)
![License](https://img.shields.io/badge/license-MIT-blue)
![Platform](https://img.shields.io/badge/platform-CLI-lightgrey)

A command-line ATM simulator built in Python. Simulates PIN authentication, balance checks, withdrawals, and deposits with proper input validation and account lockout after failed attempts.

## Features

- **PIN authentication** with a 3-attempt limit before account lockout
- **Balance inquiry**
- **Withdrawal** with insufficient-balance handling
- **Deposit** (redirects to in-branch service)
- **Exit confirmation** to prevent accidental logout
- **Input validation** for all numeric and text entries (`ValueError` handling throughout)

## How It Works

1. User enters a PIN (or types `exit` to quit).
2. On 3 incorrect attempts, the account locks and the program terminates.
3. On correct PIN, the user is shown a menu:
   - `1` → Check balance
   - `2` → Deposit (directs to counter)
   - `3` → Withdraw (validates against current balance)
   - `4` → Exit (requires yes/no confirmation)

## Usage

```bash
python atm_simulator.py
```

Follow the on-screen prompts. Default test PIN: `7300`.

## Tech Stack

- Python 3 (standard library only — no external dependencies)

## Known Limitations

- Single hardcoded account (no multi-user support)
- Balance and PIN reset on program restart (no persistent storage)
- Deposit option doesn't actually update balance (by design — simulates in-branch deposit)

## Roadmap / Possible Improvements

- [ ] Persistent storage (file or database) for balance and transaction history
- [ ] Multi-account support
- [ ] Transaction history log
- [ ] Unit tests with `pytest`

## Author

**Lawrence** ([@kaluokekelawrence-web](https://github.com/kaluokekelawrence-web))

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
