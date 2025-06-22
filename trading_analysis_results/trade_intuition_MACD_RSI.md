# Strategy: MACD_RSI - Trade Rationale and Indicator States

## Strategy Rules:
- Strategy: MACD Crossover with RSI confirmation.
- Long Entry: MACD line crosses above Signal line AND RSI_14 > 50.
- Short Entry: MACD line crosses below Signal line AND RSI_14 < 50.
- Exits: 1.2% Profit Target, 0.8% Stop Loss, or End-of-Day/Session.

---

## Trade 1: SHORT at 2025-06-13 10:50:00-04:00

- **Entry Time:** 2025-06-13 10:50:00-04:00
- **Entry Price:** 527.98
- **Trade Type:** short
- **Exit Time:** 2025-06-13 15:00:00-04:00
- **Exit Price:** 527.20
- **Exit Reason:** End of Day / Time Exit
- **PnL (Underlying Abs):** 0.78
- **PnL (Net %):** 0.1277%

### Indicator States at Entry:
- **Current Close:** 527.98
- **Current VWAP_D:** 528.55
- **Previous Close:** 528.00
- **Previous VWAP_D:** 528.55
- **EMA_9:** 528.15
- **EMA_21:** 528.04
- **RSI_14:** 49.41

### Entry Rationale:
Entered short because:
- Previous Close (528.00) was >= Previous VWAP_D (528.55).
- Current Close (527.98) crossed < Current VWAP_D (528.55).
- EMA_9 (528.15) was < EMA_21 (528.04).
- RSI_14 (49.41) was > Oversold threshold (25).

---

## Trade 2: SHORT at 2025-06-13 15:19:00-04:00

- **Entry Time:** 2025-06-13 15:19:00-04:00
- **Entry Price:** 527.22
- **Trade Type:** short
- **Exit Time:** 2025-06-13 15:20:00-04:00
- **Exit Price:** 527.45
- **Exit Reason:** End of Day / Time Exit
- **PnL (Underlying Abs):** -0.23
- **PnL (Net %):** -0.0636%

### Indicator States at Entry:
- **Current Close:** 527.22
- **Current VWAP_D:** 528.95
- **Previous Close:** 527.33
- **Previous VWAP_D:** 528.95
- **EMA_9:** 527.40
- **EMA_21:** 527.30
- **RSI_14:** 48.83

### Entry Rationale:
Entered short because:
- Previous Close (527.33) was >= Previous VWAP_D (528.95).
- Current Close (527.22) crossed < Current VWAP_D (528.95).
- EMA_9 (527.40) was < EMA_21 (527.30).
- RSI_14 (48.83) was > Oversold threshold (25).

---

## Trade 3: LONG at 2025-06-16 11:02:00-04:00

- **Entry Time:** 2025-06-16 11:02:00-04:00
- **Entry Price:** 534.78
- **Trade Type:** long
- **Exit Time:** 2025-06-16 15:00:00-04:00
- **Exit Price:** 534.12
- **Exit Reason:** End of Day / Time Exit
- **PnL (Underlying Abs):** -0.66
- **PnL (Net %):** -0.1434%

### Indicator States at Entry:
- **Current Close:** 534.78
- **Current VWAP_D:** 533.46
- **Previous Close:** 534.73
- **Previous VWAP_D:** 533.46
- **EMA_9:** 534.59
- **EMA_21:** 534.58
- **RSI_14:** 58.91

### Entry Rationale:
Entered long because:
- Previous Close (534.73) was <= Previous VWAP_D (533.46).
- Current Close (534.78) crossed > Current VWAP_D (533.46).
- EMA_9 (534.59) was > EMA_21 (534.58).
- RSI_14 (58.91) was < Overbought threshold (75).

---

## Trade 4: SHORT at 2025-06-16 15:06:00-04:00

- **Entry Time:** 2025-06-16 15:06:00-04:00
- **Entry Price:** 533.88
- **Trade Type:** short
- **Exit Time:** 2025-06-16 15:07:00-04:00
- **Exit Price:** 533.80
- **Exit Reason:** End of Day / Time Exit
- **PnL (Underlying Abs):** 0.08
- **PnL (Net %):** -0.0050%

### Indicator States at Entry:
- **Current Close:** 533.88
- **Current VWAP_D:** 533.90
- **Previous Close:** 533.87
- **Previous VWAP_D:** 533.90
- **EMA_9:** 533.95
- **EMA_21:** 533.93
- **RSI_14:** 47.61

### Entry Rationale:
Entered short because:
- Previous Close (533.87) was >= Previous VWAP_D (533.90).
- Current Close (533.88) crossed < Current VWAP_D (533.90).
- EMA_9 (533.95) was < EMA_21 (533.93).
- RSI_14 (47.61) was > Oversold threshold (25).

---

## Trade 5: LONG at 2025-06-16 15:16:00-04:00

- **Entry Time:** 2025-06-16 15:16:00-04:00
- **Entry Price:** 533.98
- **Trade Type:** long
- **Exit Time:** 2025-06-16 15:17:00-04:00
- **Exit Price:** 533.73
- **Exit Reason:** End of Day / Time Exit
- **PnL (Underlying Abs):** -0.25
- **PnL (Net %):** -0.0668%

### Indicator States at Entry:
- **Current Close:** 533.98
- **Current VWAP_D:** 533.90
- **Previous Close:** 533.71
- **Previous VWAP_D:** 533.90
- **EMA_9:** 533.77
- **EMA_21:** 533.80
- **RSI_14:** 55.78

### Entry Rationale:
Entered long because:
- Previous Close (533.71) was <= Previous VWAP_D (533.90).
- Current Close (533.98) crossed > Current VWAP_D (533.90).
- EMA_9 (533.77) was > EMA_21 (533.80).
- RSI_14 (55.78) was < Overbought threshold (75).

---

## Trade 6: SHORT at 2025-06-16 15:18:00-04:00

- **Entry Time:** 2025-06-16 15:18:00-04:00
- **Entry Price:** 533.67
- **Trade Type:** short
- **Exit Time:** 2025-06-16 15:19:00-04:00
- **Exit Price:** 533.65
- **Exit Reason:** End of Day / Time Exit
- **PnL (Underlying Abs):** 0.02
- **PnL (Net %):** -0.0163%

### Indicator States at Entry:
- **Current Close:** 533.67
- **Current VWAP_D:** 533.90
- **Previous Close:** 533.73
- **Previous VWAP_D:** 533.90
- **EMA_9:** 533.75
- **EMA_21:** 533.79
- **RSI_14:** 45.42

### Entry Rationale:
Entered short because:
- Previous Close (533.73) was >= Previous VWAP_D (533.90).
- Current Close (533.67) crossed < Current VWAP_D (533.90).
- EMA_9 (533.75) was < EMA_21 (533.79).
- RSI_14 (45.42) was > Oversold threshold (25).

---

## Trade 7: LONG at 2025-06-16 15:21:00-04:00

- **Entry Time:** 2025-06-16 15:21:00-04:00
- **Entry Price:** 534.23
- **Trade Type:** long
- **Exit Time:** 2025-06-16 15:22:00-04:00
- **Exit Price:** 534.27
- **Exit Reason:** End of Day / Time Exit
- **PnL (Underlying Abs):** 0.04
- **PnL (Net %):** -0.0125%

### Indicator States at Entry:
- **Current Close:** 534.23
- **Current VWAP_D:** 533.90
- **Previous Close:** 533.54
- **Previous VWAP_D:** 533.90
- **EMA_9:** 533.80
- **EMA_21:** 533.80
- **RSI_14:** 61.00

### Entry Rationale:
Entered long because:
- Previous Close (533.54) was <= Previous VWAP_D (533.90).
- Current Close (534.23) crossed > Current VWAP_D (533.90).
- EMA_9 (533.80) was > EMA_21 (533.80).
- RSI_14 (61.00) was < Overbought threshold (75).

---

## Trade 8: SHORT at 2025-06-17 09:30:00-04:00

- **Entry Time:** 2025-06-17 09:30:00-04:00
- **Entry Price:** 532.42
- **Trade Type:** short
- **Exit Time:** 2025-06-17 15:00:00-04:00
- **Exit Price:** 529.46
- **Exit Reason:** End of Day / Time Exit
- **PnL (Underlying Abs):** 2.96
- **PnL (Net %):** 0.5360%

### Indicator States at Entry:
- **Current Close:** 532.42
- **Current VWAP_D:** 532.02
- **Previous Close:** 534.27
- **Previous VWAP_D:** 533.91
- **EMA_9:** 533.64
- **EMA_21:** 533.80
- **RSI_14:** 32.23

### Entry Rationale:
Entered short because:
- Previous Close (534.27) was >= Previous VWAP_D (533.91).
- Current Close (532.42) crossed < Current VWAP_D (532.02).
- EMA_9 (533.64) was < EMA_21 (533.80).
- RSI_14 (32.23) was > Oversold threshold (25).

---

## Trade 9: SHORT at 2025-06-17 15:05:00-04:00

- **Entry Time:** 2025-06-17 15:05:00-04:00
- **Entry Price:** 528.92
- **Trade Type:** short
- **Exit Time:** 2025-06-17 15:06:00-04:00
- **Exit Price:** 529.01
- **Exit Reason:** End of Day / Time Exit
- **PnL (Underlying Abs):** -0.09
- **PnL (Net %):** -0.0370%

### Indicator States at Entry:
- **Current Close:** 528.92
- **Current VWAP_D:** 531.11
- **Previous Close:** 529.07
- **Previous VWAP_D:** 531.11
- **EMA_9:** 529.17
- **EMA_21:** 529.08
- **RSI_14:** 46.46

### Entry Rationale:
Entered short because:
- Previous Close (529.07) was >= Previous VWAP_D (531.11).
- Current Close (528.92) crossed < Current VWAP_D (531.11).
- EMA_9 (529.17) was < EMA_21 (529.08).
- RSI_14 (46.46) was > Oversold threshold (25).

---

## Trade 10: LONG at 2025-06-17 15:12:00-04:00

- **Entry Time:** 2025-06-17 15:12:00-04:00
- **Entry Price:** 529.48
- **Trade Type:** long
- **Exit Time:** 2025-06-17 15:13:00-04:00
- **Exit Price:** 529.30
- **Exit Reason:** End of Day / Time Exit
- **PnL (Underlying Abs):** -0.18
- **PnL (Net %):** -0.0540%

### Indicator States at Entry:
- **Current Close:** 529.48
- **Current VWAP_D:** 531.08
- **Previous Close:** 529.37
- **Previous VWAP_D:** 531.09
- **EMA_9:** 529.24
- **EMA_21:** 529.15
- **RSI_14:** 60.78

### Entry Rationale:
Entered long because:
- Previous Close (529.37) was <= Previous VWAP_D (531.09).
- Current Close (529.48) crossed > Current VWAP_D (531.08).
- EMA_9 (529.24) was > EMA_21 (529.15).
- RSI_14 (60.78) was < Overbought threshold (75).

---

## Trade 11: SHORT at 2025-06-17 15:17:00-04:00

- **Entry Time:** 2025-06-17 15:17:00-04:00
- **Entry Price:** 529.16
- **Trade Type:** short
- **Exit Time:** 2025-06-17 15:18:00-04:00
- **Exit Price:** 529.19
- **Exit Reason:** End of Day / Time Exit
- **PnL (Underlying Abs):** -0.03
- **PnL (Net %):** -0.0257%

### Indicator States at Entry:
- **Current Close:** 529.16
- **Current VWAP_D:** 531.07
- **Previous Close:** 529.45
- **Previous VWAP_D:** 531.07
- **EMA_9:** 529.30
- **EMA_21:** 529.22
- **RSI_14:** 49.25

### Entry Rationale:
Entered short because:
- Previous Close (529.45) was >= Previous VWAP_D (531.07).
- Current Close (529.16) crossed < Current VWAP_D (531.07).
- EMA_9 (529.30) was < EMA_21 (529.22).
- RSI_14 (49.25) was > Oversold threshold (25).

---

## Trade 12: LONG at 2025-06-17 15:20:00-04:00

- **Entry Time:** 2025-06-17 15:20:00-04:00
- **Entry Price:** 529.67
- **Trade Type:** long
- **Exit Time:** 2025-06-17 15:21:00-04:00
- **Exit Price:** 529.66
- **Exit Reason:** End of Day / Time Exit
- **PnL (Underlying Abs):** -0.01
- **PnL (Net %):** -0.0219%

### Indicator States at Entry:
- **Current Close:** 529.67
- **Current VWAP_D:** 531.06
- **Previous Close:** 529.25
- **Previous VWAP_D:** 531.06
- **EMA_9:** 529.35
- **EMA_21:** 529.26
- **RSI_14:** 62.03

### Entry Rationale:
Entered long because:
- Previous Close (529.25) was <= Previous VWAP_D (531.06).
- Current Close (529.67) crossed > Current VWAP_D (531.06).
- EMA_9 (529.35) was > EMA_21 (529.26).
- RSI_14 (62.03) was < Overbought threshold (75).

---

## Trade 13: LONG at 2025-06-18 09:39:00-04:00

- **Entry Time:** 2025-06-18 09:39:00-04:00
- **Entry Price:** 529.36
- **Trade Type:** long
- **Exit Time:** 2025-06-18 15:00:00-04:00
- **Exit Price:** 527.74
- **Exit Reason:** End of Day / Time Exit
- **PnL (Underlying Abs):** -1.62
- **PnL (Net %):** -0.3260%

### Indicator States at Entry:
- **Current Close:** 529.36
- **Current VWAP_D:** 529.28
- **Previous Close:** 529.23
- **Previous VWAP_D:** 529.27
- **EMA_9:** 529.15
- **EMA_21:** 529.24
- **RSI_14:** 51.58

### Entry Rationale:
Entered long because:
- Previous Close (529.23) was <= Previous VWAP_D (529.27).
- Current Close (529.36) crossed > Current VWAP_D (529.28).
- EMA_9 (529.15) was > EMA_21 (529.24).
- RSI_14 (51.58) was < Overbought threshold (75).

---

## Trade 14: SHORT at 2025-06-18 15:27:00-04:00

- **Entry Time:** 2025-06-18 15:27:00-04:00
- **Entry Price:** 529.04
- **Trade Type:** short
- **Exit Time:** 2025-06-18 15:28:00-04:00
- **Exit Price:** 528.51
- **Exit Reason:** End of Day / Time Exit
- **PnL (Underlying Abs):** 0.53
- **PnL (Net %):** 0.0802%

### Indicator States at Entry:
- **Current Close:** 529.04
- **Current VWAP_D:** 530.52
- **Previous Close:** 529.63
- **Previous VWAP_D:** 530.53
- **EMA_9:** 529.72
- **EMA_21:** 529.60
- **RSI_14:** 42.75

### Entry Rationale:
Entered short because:
- Previous Close (529.63) was >= Previous VWAP_D (530.53).
- Current Close (529.04) crossed < Current VWAP_D (530.52).
- EMA_9 (529.72) was < EMA_21 (529.60).
- RSI_14 (42.75) was > Oversold threshold (25).

---

## Trade 15: LONG at 2025-06-20 09:30:00-04:00

- **Entry Time:** 2025-06-20 09:30:00-04:00
- **Entry Price:** 532.52
- **Trade Type:** long
- **Exit Time:** 2025-06-20 10:25:00-04:00
- **Exit Price:** 528.26
- **Exit Reason:** Stop Loss
- **PnL (Underlying Abs):** -4.26
- **PnL (Net %):** -0.8200%

### Indicator States at Entry:
- **Current Close:** 532.52
- **Current VWAP_D:** 532.00
- **Previous Close:** 528.96
- **Previous VWAP_D:** 530.36
- **EMA_9:** 529.80
- **EMA_21:** 529.62
- **RSI_14:** 76.91

### Entry Rationale:
Entered long because:
- Previous Close (528.96) was <= Previous VWAP_D (530.36).
- Current Close (532.52) crossed > Current VWAP_D (532.00).
- EMA_9 (529.80) was > EMA_21 (529.62).
- RSI_14 (76.91) was < Overbought threshold (75).

---

## Trade 16: SHORT at 2025-06-20 10:41:00-04:00

- **Entry Time:** 2025-06-20 10:41:00-04:00
- **Entry Price:** 527.83
- **Trade Type:** short
- **Exit Time:** 2025-06-20 15:00:00-04:00
- **Exit Price:** 526.06
- **Exit Reason:** End of Day / Time Exit
- **PnL (Underlying Abs):** 1.77
- **PnL (Net %):** 0.3153%

### Indicator States at Entry:
- **Current Close:** 527.83
- **Current VWAP_D:** 531.01
- **Previous Close:** 528.32
- **Previous VWAP_D:** 531.09
- **EMA_9:** 528.75
- **EMA_21:** 529.07
- **RSI_14:** 32.12

### Entry Rationale:
Entered short because:
- Previous Close (528.32) was >= Previous VWAP_D (531.09).
- Current Close (527.83) crossed < Current VWAP_D (531.01).
- EMA_9 (528.75) was < EMA_21 (529.07).
- RSI_14 (32.12) was > Oversold threshold (25).

---

## Trade 17: SHORT at 2025-06-20 15:28:00-04:00

- **Entry Time:** 2025-06-20 15:28:00-04:00
- **Entry Price:** 525.87
- **Trade Type:** short
- **Exit Time:** 2025-06-20 15:29:00-04:00
- **Exit Price:** 525.98
- **Exit Reason:** End of Day / Time Exit
- **PnL (Underlying Abs):** -0.11
- **PnL (Net %):** -0.0409%

### Indicator States at Entry:
- **Current Close:** 525.87
- **Current VWAP_D:** 528.07
- **Previous Close:** 525.90
- **Previous VWAP_D:** 528.07
- **EMA_9:** 526.05
- **EMA_21:** 526.16
- **RSI_14:** 34.05

### Entry Rationale:
Entered short because:
- Previous Close (525.90) was >= Previous VWAP_D (528.07).
- Current Close (525.87) crossed < Current VWAP_D (528.07).
- EMA_9 (526.05) was < EMA_21 (526.16).
- RSI_14 (34.05) was > Oversold threshold (25).

---
