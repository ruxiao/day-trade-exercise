# Strategy: EMA_CROSS - Trade Rationale and Indicator States

## Strategy Rules:
- Strategy: Simple Fast EMA (5) crossing Slow EMA (10).
- Long Entry: EMA_5 crosses above EMA_10.
- Short Entry: EMA_5 crosses below EMA_10.
- Exits: 1.0% Profit Target, 0.7% Stop Loss, or End-of-Day/Session.

---

## Trade 1: LONG at 2025-06-13 10:34:00-04:00

- **Entry Time:** 2025-06-13 10:34:00-04:00
- **Entry Price:** 527.26
- **Trade Type:** long
- **Exit Time:** 2025-06-13 15:00:00-04:00
- **Exit Price:** 527.20
- **Exit Reason:** End of Day / Time Exit
- **PnL (Underlying Abs):** -0.06
- **PnL (Net %):** -0.0314%

### Indicator States at Entry:
- **Current Close:** 527.26
- **Current VWAP_D:** 528.59
- **Previous Close:** 527.31
- **Previous VWAP_D:** 528.61
- **EMA_9:** 527.01
- **EMA_21:** 527.29
- **RSI_14:** 46.87

### Entry Rationale:
Entered long because:
- Previous Close (527.31) was <= Previous VWAP_D (528.61).
- Current Close (527.26) crossed > Current VWAP_D (528.59).
- EMA_9 (527.01) was > EMA_21 (527.29).
- RSI_14 (46.87) was < Overbought threshold (75).

---

## Trade 2: SHORT at 2025-06-13 15:02:00-04:00

- **Entry Time:** 2025-06-13 15:02:00-04:00
- **Entry Price:** 526.60
- **Trade Type:** short
- **Exit Time:** 2025-06-13 15:03:00-04:00
- **Exit Price:** 527.06
- **Exit Reason:** End of Day / Time Exit
- **PnL (Underlying Abs):** -0.46
- **PnL (Net %):** -0.1074%

### Indicator States at Entry:
- **Current Close:** 526.60
- **Current VWAP_D:** 529.03
- **Previous Close:** 526.77
- **Previous VWAP_D:** 529.05
- **EMA_9:** 526.90
- **EMA_21:** 526.89
- **RSI_14:** 43.74

### Entry Rationale:
Entered short because:
- Previous Close (526.77) was >= Previous VWAP_D (529.05).
- Current Close (526.60) crossed < Current VWAP_D (529.03).
- EMA_9 (526.90) was < EMA_21 (526.89).
- RSI_14 (43.74) was > Oversold threshold (25).

---

## Trade 3: LONG at 2025-06-13 15:03:00-04:00

- **Entry Time:** 2025-06-13 15:03:00-04:00
- **Entry Price:** 527.06
- **Trade Type:** long
- **Exit Time:** 2025-06-13 15:04:00-04:00
- **Exit Price:** 526.93
- **Exit Reason:** End of Day / Time Exit
- **PnL (Underlying Abs):** -0.13
- **PnL (Net %):** -0.0447%

### Indicator States at Entry:
- **Current Close:** 527.06
- **Current VWAP_D:** 529.02
- **Previous Close:** 526.60
- **Previous VWAP_D:** 529.03
- **EMA_9:** 526.93
- **EMA_21:** 526.91
- **RSI_14:** 51.52

### Entry Rationale:
Entered long because:
- Previous Close (526.60) was <= Previous VWAP_D (529.03).
- Current Close (527.06) crossed > Current VWAP_D (529.02).
- EMA_9 (526.93) was > EMA_21 (526.91).
- RSI_14 (51.52) was < Overbought threshold (75).

---

## Trade 4: SHORT at 2025-06-13 15:19:00-04:00

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

## Trade 5: SHORT at 2025-06-16 10:09:00-04:00

- **Entry Time:** 2025-06-16 10:09:00-04:00
- **Entry Price:** 533.62
- **Trade Type:** short
- **Exit Time:** 2025-06-16 15:00:00-04:00
- **Exit Price:** 534.12
- **Exit Reason:** End of Day / Time Exit
- **PnL (Underlying Abs):** -0.50
- **PnL (Net %):** -0.1137%

### Indicator States at Entry:
- **Current Close:** 533.62
- **Current VWAP_D:** 532.76
- **Previous Close:** 533.76
- **Previous VWAP_D:** 532.74
- **EMA_9:** 533.87
- **EMA_21:** 533.45
- **RSI_14:** 59.13

### Entry Rationale:
Entered short because:
- Previous Close (533.76) was >= Previous VWAP_D (532.74).
- Current Close (533.62) crossed < Current VWAP_D (532.76).
- EMA_9 (533.87) was < EMA_21 (533.45).
- RSI_14 (59.13) was > Oversold threshold (25).

---

## Trade 6: SHORT at 2025-06-16 15:05:00-04:00

- **Entry Time:** 2025-06-16 15:05:00-04:00
- **Entry Price:** 533.87
- **Trade Type:** short
- **Exit Time:** 2025-06-16 15:06:00-04:00
- **Exit Price:** 533.88
- **Exit Reason:** End of Day / Time Exit
- **PnL (Underlying Abs):** -0.01
- **PnL (Net %):** -0.0219%

### Indicator States at Entry:
- **Current Close:** 533.87
- **Current VWAP_D:** 533.90
- **Previous Close:** 533.97
- **Previous VWAP_D:** 533.90
- **EMA_9:** 533.96
- **EMA_21:** 533.93
- **RSI_14:** 47.13

### Entry Rationale:
Entered short because:
- Previous Close (533.97) was >= Previous VWAP_D (533.90).
- Current Close (533.87) crossed < Current VWAP_D (533.90).
- EMA_9 (533.96) was < EMA_21 (533.93).
- RSI_14 (47.13) was > Oversold threshold (25).

---

## Trade 7: LONG at 2025-06-16 15:16:00-04:00

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

## Trade 8: SHORT at 2025-06-16 15:18:00-04:00

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

## Trade 9: LONG at 2025-06-16 15:21:00-04:00

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

## Trade 10: SHORT at 2025-06-17 09:30:00-04:00

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

## Trade 11: SHORT at 2025-06-17 15:05:00-04:00

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

## Trade 12: LONG at 2025-06-17 15:11:00-04:00

- **Entry Time:** 2025-06-17 15:11:00-04:00
- **Entry Price:** 529.37
- **Trade Type:** long
- **Exit Time:** 2025-06-17 15:12:00-04:00
- **Exit Price:** 529.48
- **Exit Reason:** End of Day / Time Exit
- **PnL (Underlying Abs):** 0.11
- **PnL (Net %):** 0.0008%

### Indicator States at Entry:
- **Current Close:** 529.37
- **Current VWAP_D:** 531.09
- **Previous Close:** 529.06
- **Previous VWAP_D:** 531.09
- **EMA_9:** 529.18
- **EMA_21:** 529.12
- **RSI_14:** 58.26

### Entry Rationale:
Entered long because:
- Previous Close (529.06) was <= Previous VWAP_D (531.09).
- Current Close (529.37) crossed > Current VWAP_D (531.09).
- EMA_9 (529.18) was > EMA_21 (529.12).
- RSI_14 (58.26) was < Overbought threshold (75).

---

## Trade 13: SHORT at 2025-06-17 15:18:00-04:00

- **Entry Time:** 2025-06-17 15:18:00-04:00
- **Entry Price:** 529.19
- **Trade Type:** short
- **Exit Time:** 2025-06-17 15:19:00-04:00
- **Exit Price:** 529.25
- **Exit Reason:** End of Day / Time Exit
- **PnL (Underlying Abs):** -0.06
- **PnL (Net %):** -0.0313%

### Indicator States at Entry:
- **Current Close:** 529.19
- **Current VWAP_D:** 531.06
- **Previous Close:** 529.16
- **Previous VWAP_D:** 531.07
- **EMA_9:** 529.28
- **EMA_21:** 529.22
- **RSI_14:** 50.11

### Entry Rationale:
Entered short because:
- Previous Close (529.16) was >= Previous VWAP_D (531.07).
- Current Close (529.19) crossed < Current VWAP_D (531.06).
- EMA_9 (529.28) was < EMA_21 (529.22).
- RSI_14 (50.11) was > Oversold threshold (25).

---

## Trade 14: LONG at 2025-06-17 15:20:00-04:00

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

## Trade 15: LONG at 2025-06-18 09:31:00-04:00

- **Entry Time:** 2025-06-18 09:31:00-04:00
- **Entry Price:** 529.46
- **Trade Type:** long
- **Exit Time:** 2025-06-18 15:00:00-04:00
- **Exit Price:** 527.74
- **Exit Reason:** End of Day / Time Exit
- **PnL (Underlying Abs):** -1.72
- **PnL (Net %):** -0.3449%

### Indicator States at Entry:
- **Current Close:** 529.46
- **Current VWAP_D:** 529.81
- **Previous Close:** 529.83
- **Previous VWAP_D:** 529.84
- **EMA_9:** 529.39
- **EMA_21:** 529.46
- **RSI_14:** 49.67

### Entry Rationale:
Entered long because:
- Previous Close (529.83) was <= Previous VWAP_D (529.84).
- Current Close (529.46) crossed > Current VWAP_D (529.81).
- EMA_9 (529.39) was > EMA_21 (529.46).
- RSI_14 (49.67) was < Overbought threshold (75).

---

## Trade 16: LONG at 2025-06-18 15:06:00-04:00

- **Entry Time:** 2025-06-18 15:06:00-04:00
- **Entry Price:** 529.09
- **Trade Type:** long
- **Exit Time:** 2025-06-18 15:07:00-04:00
- **Exit Price:** 528.85
- **Exit Reason:** End of Day / Time Exit
- **PnL (Underlying Abs):** -0.24
- **PnL (Net %):** -0.0654%

### Indicator States at Entry:
- **Current Close:** 529.09
- **Current VWAP_D:** 530.63
- **Previous Close:** 529.09
- **Previous VWAP_D:** 530.63
- **EMA_9:** 528.82
- **EMA_21:** 529.21
- **RSI_14:** 45.65

### Entry Rationale:
Entered long because:
- Previous Close (529.09) was <= Previous VWAP_D (530.63).
- Current Close (529.09) crossed > Current VWAP_D (530.63).
- EMA_9 (528.82) was > EMA_21 (529.21).
- RSI_14 (45.65) was < Overbought threshold (75).

---

## Trade 17: SHORT at 2025-06-18 15:08:00-04:00

- **Entry Time:** 2025-06-18 15:08:00-04:00
- **Entry Price:** 528.59
- **Trade Type:** short
- **Exit Time:** 2025-06-18 15:09:00-04:00
- **Exit Price:** 528.61
- **Exit Reason:** End of Day / Time Exit
- **PnL (Underlying Abs):** -0.02
- **PnL (Net %):** -0.0238%

### Indicator States at Entry:
- **Current Close:** 528.59
- **Current VWAP_D:** 530.62
- **Previous Close:** 528.85
- **Previous VWAP_D:** 530.62
- **EMA_9:** 528.78
- **EMA_21:** 529.12
- **RSI_14:** 39.62

### Entry Rationale:
Entered short because:
- Previous Close (528.85) was >= Previous VWAP_D (530.62).
- Current Close (528.59) crossed < Current VWAP_D (530.62).
- EMA_9 (528.78) was < EMA_21 (529.12).
- RSI_14 (39.62) was > Oversold threshold (25).

---

## Trade 18: LONG at 2025-06-18 15:11:00-04:00

- **Entry Time:** 2025-06-18 15:11:00-04:00
- **Entry Price:** 528.94
- **Trade Type:** long
- **Exit Time:** 2025-06-18 15:12:00-04:00
- **Exit Price:** 528.45
- **Exit Reason:** End of Day / Time Exit
- **PnL (Underlying Abs):** -0.49
- **PnL (Net %):** -0.1126%

### Indicator States at Entry:
- **Current Close:** 528.94
- **Current VWAP_D:** 530.60
- **Previous Close:** 528.74
- **Previous VWAP_D:** 530.60
- **EMA_9:** 528.78
- **EMA_21:** 529.03
- **RSI_14:** 45.87

### Entry Rationale:
Entered long because:
- Previous Close (528.74) was <= Previous VWAP_D (530.60).
- Current Close (528.94) crossed > Current VWAP_D (530.60).
- EMA_9 (528.78) was > EMA_21 (529.03).
- RSI_14 (45.87) was < Overbought threshold (75).

---

## Trade 19: SHORT at 2025-06-18 15:12:00-04:00

- **Entry Time:** 2025-06-18 15:12:00-04:00
- **Entry Price:** 528.45
- **Trade Type:** short
- **Exit Time:** 2025-06-18 15:13:00-04:00
- **Exit Price:** 529.68
- **Exit Reason:** End of Day / Time Exit
- **PnL (Underlying Abs):** -1.23
- **PnL (Net %):** -0.2528%

### Indicator States at Entry:
- **Current Close:** 528.45
- **Current VWAP_D:** 530.59
- **Previous Close:** 528.94
- **Previous VWAP_D:** 530.60
- **EMA_9:** 528.72
- **EMA_21:** 528.98
- **RSI_14:** 39.49

### Entry Rationale:
Entered short because:
- Previous Close (528.94) was >= Previous VWAP_D (530.60).
- Current Close (528.45) crossed < Current VWAP_D (530.59).
- EMA_9 (528.72) was < EMA_21 (528.98).
- RSI_14 (39.49) was > Oversold threshold (25).

---

## Trade 20: LONG at 2025-06-20 09:30:00-04:00

- **Entry Time:** 2025-06-20 09:30:00-04:00
- **Entry Price:** 532.52
- **Trade Type:** long
- **Exit Time:** 2025-06-20 10:24:00-04:00
- **Exit Price:** 528.79
- **Exit Reason:** Stop Loss
- **PnL (Underlying Abs):** -3.73
- **PnL (Net %):** -0.7200%

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

## Trade 21: LONG at 2025-06-20 10:37:00-04:00

- **Entry Time:** 2025-06-20 10:37:00-04:00
- **Entry Price:** 529.35
- **Trade Type:** long
- **Exit Time:** 2025-06-20 10:54:00-04:00
- **Exit Price:** 525.64
- **Exit Reason:** Stop Loss
- **PnL (Underlying Abs):** -3.71
- **PnL (Net %):** -0.7200%

### Indicator States at Entry:
- **Current Close:** 529.35
- **Current VWAP_D:** 531.18
- **Previous Close:** 529.04
- **Previous VWAP_D:** 531.21
- **EMA_9:** 529.02
- **EMA_21:** 529.26
- **RSI_14:** 48.89

### Entry Rationale:
Entered long because:
- Previous Close (529.04) was <= Previous VWAP_D (531.21).
- Current Close (529.35) crossed > Current VWAP_D (531.18).
- EMA_9 (529.02) was > EMA_21 (529.26).
- RSI_14 (48.89) was < Overbought threshold (75).

---

## Trade 22: LONG at 2025-06-20 11:09:00-04:00

- **Entry Time:** 2025-06-20 11:09:00-04:00
- **Entry Price:** 526.01
- **Trade Type:** long
- **Exit Time:** 2025-06-20 15:00:00-04:00
- **Exit Price:** 526.06
- **Exit Reason:** End of Day / Time Exit
- **PnL (Underlying Abs):** 0.05
- **PnL (Net %):** -0.0105%

### Indicator States at Entry:
- **Current Close:** 526.01
- **Current VWAP_D:** 529.61
- **Previous Close:** 525.88
- **Previous VWAP_D:** 529.62
- **EMA_9:** 525.86
- **EMA_21:** 526.19
- **RSI_14:** 43.61

### Entry Rationale:
Entered long because:
- Previous Close (525.88) was <= Previous VWAP_D (529.62).
- Current Close (526.01) crossed > Current VWAP_D (529.61).
- EMA_9 (525.86) was > EMA_21 (526.19).
- RSI_14 (43.61) was < Overbought threshold (75).

---

## Trade 23: LONG at 2025-06-20 15:12:00-04:00

- **Entry Time:** 2025-06-20 15:12:00-04:00
- **Entry Price:** 526.34
- **Trade Type:** long
- **Exit Time:** 2025-06-20 15:13:00-04:00
- **Exit Price:** 526.26
- **Exit Reason:** End of Day / Time Exit
- **PnL (Underlying Abs):** -0.08
- **PnL (Net %):** -0.0352%

### Indicator States at Entry:
- **Current Close:** 526.34
- **Current VWAP_D:** 528.14
- **Previous Close:** 526.22
- **Previous VWAP_D:** 528.14
- **EMA_9:** 526.19
- **EMA_21:** 526.37
- **RSI_14:** 45.05

### Entry Rationale:
Entered long because:
- Previous Close (526.22) was <= Previous VWAP_D (528.14).
- Current Close (526.34) crossed > Current VWAP_D (528.14).
- EMA_9 (526.19) was > EMA_21 (526.37).
- RSI_14 (45.05) was < Overbought threshold (75).

---

## Trade 24: SHORT at 2025-06-20 15:15:00-04:00

- **Entry Time:** 2025-06-20 15:15:00-04:00
- **Entry Price:** 526.08
- **Trade Type:** short
- **Exit Time:** 2025-06-20 15:16:00-04:00
- **Exit Price:** 526.11
- **Exit Reason:** End of Day / Time Exit
- **PnL (Underlying Abs):** -0.03
- **PnL (Net %):** -0.0257%

### Indicator States at Entry:
- **Current Close:** 526.08
- **Current VWAP_D:** 528.12
- **Previous Close:** 526.19
- **Previous VWAP_D:** 528.13
- **EMA_9:** 526.18
- **EMA_21:** 526.32
- **RSI_14:** 37.07

### Entry Rationale:
Entered short because:
- Previous Close (526.19) was >= Previous VWAP_D (528.13).
- Current Close (526.08) crossed < Current VWAP_D (528.12).
- EMA_9 (526.18) was < EMA_21 (526.32).
- RSI_14 (37.07) was > Oversold threshold (25).

---
