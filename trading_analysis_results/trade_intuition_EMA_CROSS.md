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
- **Exit Time:** 2025-06-13 15:55:00-04:00
- **Exit Price:** 526.11
- **Exit Reason:** End of Day / Time Exit
- **PnL (Underlying):** -1.15

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

## Trade 2: SHORT at 2025-06-16 10:09:00-04:00

- **Entry Time:** 2025-06-16 10:09:00-04:00
- **Entry Price:** 533.62
- **Trade Type:** short
- **Exit Time:** 2025-06-16 15:55:00-04:00
- **Exit Price:** 534.18
- **Exit Reason:** End of Day / Time Exit
- **PnL (Underlying):** -0.56

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

## Trade 3: SHORT at 2025-06-17 09:30:00-04:00

- **Entry Time:** 2025-06-17 09:30:00-04:00
- **Entry Price:** 532.42
- **Trade Type:** short
- **Exit Time:** 2025-06-17 15:55:00-04:00
- **Exit Price:** 529.33
- **Exit Reason:** End of Day / Time Exit
- **PnL (Underlying):** 3.09

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

## Trade 4: LONG at 2025-06-18 09:31:00-04:00

- **Entry Time:** 2025-06-18 09:31:00-04:00
- **Entry Price:** 529.46
- **Trade Type:** long
- **Exit Time:** 2025-06-18 15:55:00-04:00
- **Exit Price:** 529.05
- **Exit Reason:** End of Day / Time Exit
- **PnL (Underlying):** -0.41

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

## Trade 5: LONG at 2025-06-20 09:30:00-04:00

- **Entry Time:** 2025-06-20 09:30:00-04:00
- **Entry Price:** 532.52
- **Trade Type:** long
- **Exit Time:** 2025-06-20 10:24:00-04:00
- **Exit Price:** 528.79
- **Exit Reason:** Stop Loss
- **PnL (Underlying):** -3.73

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

## Trade 6: LONG at 2025-06-20 10:37:00-04:00

- **Entry Time:** 2025-06-20 10:37:00-04:00
- **Entry Price:** 529.35
- **Trade Type:** long
- **Exit Time:** 2025-06-20 10:54:00-04:00
- **Exit Price:** 525.64
- **Exit Reason:** Stop Loss
- **PnL (Underlying):** -3.71

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

## Trade 7: LONG at 2025-06-20 11:09:00-04:00

- **Entry Time:** 2025-06-20 11:09:00-04:00
- **Entry Price:** 526.01
- **Trade Type:** long
- **Exit Time:** 2025-06-20 15:55:00-04:00
- **Exit Price:** 526.84
- **Exit Reason:** End of Day / Time Exit
- **PnL (Underlying):** 0.83

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
